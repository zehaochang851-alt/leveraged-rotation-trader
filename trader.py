import os, math, requests
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from run_strategy import run_strategy

TICKERS = [
    "AAPX","AGG","AGQ","AMZN","AMZU","AMZZ","BABA","BAM","BIL","BITX","BN","BND",
    "BTAL","BX","COIN","CONL","EDC","EDZ","EEM","FAS","FAZ","FBL","GDXD","GDXU",
    "GGLL","GLD","HOOD","IBKR","IEF","IEI","IGIB","IOO","IUSV","IVW","IWM","KKR",
    "KMLM","MA","META","NVDL","PLTR","PSQ","QLD","QQQ","QQQE","RGTI","SCHW","SH",
    "SHV","SOFI","SOXL","SOXS","SPXL","SPY","SQQQ","SVIX","TECL","TECS","TLT",
    "TMF","TQQQ","TSLA","TSLR","UGL","UPRO","UVXY","V","VIXM","VIXY","VOOG",
    "VOOV","VOX","VTR","VTV","WELL","XLF","XLK","XLP","XLY"
]

W = 220
TEST_ONLY = True
NY = ZoneInfo("America/New_York")

PAPER = "https://paper-api.alpaca.markets"
DATA = "https://data.alpaca.markets"

KEY = os.environ["ALPACA_API_KEY"]
SECRET = os.environ["ALPACA_SECRET_KEY"]

TG_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TG_CHAT = os.environ.get("TELEGRAM_CHAT_ID", "")

HEAD = {
    "APCA-API-KEY-ID": KEY,
    "APCA-API-SECRET-KEY": SECRET
}


class MissingTicker(Exception):
    pass


class GatedPrices(dict):
    def __missing__(self, key):
        raise MissingTicker(
            f"{key} has fewer than {W} real adjusted daily bars"
        )


def api(method, url, **kwargs):
    r = requests.request(
        method,
        url,
        headers=HEAD,
        timeout=30,
        **kwargs
    )

    if not r.ok:
        raise RuntimeError(
            f"{method} {url} -> {r.status_code}: {r.text[:500]}"
        )

    return r.json() if r.text else {}


def telegram(text):
    if not (TG_TOKEN and TG_CHAT):
        return

    for i in range(0, len(text), 3900):
        try:
            r = requests.post(
                f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
                json={
                    "chat_id": TG_CHAT,
                    "text": text[i:i + 3900]
                },
                timeout=20
            )
            r.raise_for_status()

        except Exception as e:
            print("Telegram error:", e)


def clock():
    return api(
        "GET",
        f"{PAPER}/v2/clock"
    )


def fetch_prices(today):
    start = (today - timedelta(days=420)).isoformat()
    # Free SIP mode: request only data older than today's NY midnight.
    # This keeps the query safely outside Alpaca's recent-SIP restriction
    # and ensures today's unfinished bar can never enter the signal.
    end = datetime(today.year, today.month, today.day, tzinfo=NY).astimezone(ZoneInfo("UTC")).isoformat()

    bars = {
        ticker: []
        for ticker in TICKERS
    }

    page_token = None

    while True:

        params = {
            "symbols": ",".join(TICKERS),
            "timeframe": "1Day",
            "start": start,
            "end": end,
            "adjustment": "all",
            "feed": "sip",
            "limit": 10000,
            "sort": "asc"
        }

        if page_token:
            params["page_token"] = page_token

        data = api(
            "GET",
            f"{DATA}/v2/stocks/bars",
            params=params
        )

        for ticker, rows in data.get("bars", {}).items():
            bars[ticker].extend(rows)

        page_token = data.get("next_page_token")

        if not page_token:
            break

    prices = GatedPrices()

    for ticker, rows in bars.items():

        closes = [
            float(row["c"])
            for row in rows
            if "c" in row
        ]

        if len(closes) >= W:
            prices[ticker] = closes[-W:]

    return prices


def positions():
    rows = api(
        "GET",
        f"{PAPER}/v2/positions"
    )

    return {
        row["symbol"]: row
        for row in rows
    }


def account():
    return api(
        "GET",
        f"{PAPER}/v2/account"
    )


def submit(symbol, qty, side):

    if TEST_ONLY:
        return {
            "test_only": True,
            "symbol": symbol,
            "qty": qty,
            "side": side
        }

    if qty <= 0:
        return None

    body = {
        "symbol": symbol,
        "qty": str(int(qty)),
        "side": side,
        "type": "market",
        "time_in_force": "cls",
        "client_order_id":
            f"lr-{datetime.now(NY):%Y%m%d}-{symbol}-{side}"[:48]
    }

    return api(
        "POST",
        f"{PAPER}/v2/orders",
        json=body
    )


def main():

    now = datetime.now(NY)

    acct = account()

    equity = float(acct["equity"])

    today = now.date()

    telegram(
        "SAFE TEST STARTED\n"
        f"Date: {today}\n"
        f"Account equity: ${equity:,.2f}\n"
        "Mode: TEST ONLY - no orders can be submitted."
    )

    prices = fetch_prices(today)

    try:
        weights = run_strategy(prices)

    except (MissingTicker, KeyError) as e:

        telegram(
            "STRATEGY TEST SKIPPED\n"
            f"Date: {today}\n"
            f"Reason: {e}\n"
            "No orders were submitted."
        )

        return

    total_weight = sum(weights.values())

    if not (0.999999 <= total_weight <= 1.000001):
        raise RuntimeError(
            f"Weight sum invalid: {total_weight}"
        )

    current_positions = positions()

    current_qty = {
        ticker: int(float(position["qty"]))
        for ticker, position in current_positions.items()
    }

    reference_price = {
        ticker: float(prices[ticker][-1])
        for ticker in weights
    }

    target_qty = {}

    for ticker, weight in weights.items():

        target_value = equity * weight

        qty = math.floor(
            target_value / reference_price[ticker]
        )

        target_qty[ticker] = max(
            0,
            int(qty)
        )

    all_tickers = (
        set(current_qty)
        | set(target_qty)
    )

    deltas = {
        ticker:
            target_qty.get(ticker, 0)
            - current_qty.get(ticker, 0)

        for ticker in all_tickers
    }

    simulated_orders = []

    for side in ("sell", "buy"):

        for ticker, delta in sorted(deltas.items()):

            qty = (
                -delta
                if side == "sell"
                else delta
            )

            if qty <= 0:
                continue

            simulated_orders.append(
                submit(
                    ticker,
                    qty,
                    side
                )
            )

    lines = [
        "SAFE STRATEGY TEST COMPLETE",
        "",
        f"Date: {today}",
        f"Account equity: ${equity:,.2f}",
        f"Eligible tickers: {len(prices)}/{len(TICKERS)}",
        f"Target assets: {len(weights)}",
        f"Simulated orders: {len(simulated_orders)}",
        "",
        "IMPORTANT",
        "TEST ONLY MODE",
        "NO REAL ORDERS WERE SENT",
        "",
        "TARGET PORTFOLIO"
    ]

    for ticker, weight in sorted(
        weights.items(),
        key=lambda item: -item[1]
    ):

        lines.append(
            f"{ticker}: "
            f"{weight * 100:.2f}% | "
            f"target {target_qty[ticker]} shares | "
            f"current {current_qty.get(ticker, 0)} | "
            f"change {deltas[ticker]:+d}"
        )

    telegram(
        "\n".join(lines)
    )


if __name__ == "__main__":

    try:
        main()

    except Exception as e:

        telegram(
            "SAFE TEST FAILED\n"
            f"{datetime.now(NY):%Y-%m-%d %H:%M ET}\n"
            f"{type(e).__name__}: {e}\n"
            "No orders were submitted."
        )

        raise
