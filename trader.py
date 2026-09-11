import os
import sys
import math
import requests
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
MANAGED = set(TICKERS)
W = 220
NY = ZoneInfo("America/New_York")
UTC = ZoneInfo("UTC")
PAPER = "https://paper-api.alpaca.markets"
DATA = "https://data.alpaca.markets"

KEY = os.environ["ALPACA_API_KEY"]
SECRET = os.environ["ALPACA_SECRET_KEY"]
TG_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TG_CHAT = os.environ.get("TELEGRAM_CHAT_ID", "")
HEAD = {"APCA-API-KEY-ID": KEY, "APCA-API-SECRET-KEY": SECRET}

class MissingTicker(Exception):
    pass

class GatedPrices(dict):
    def __missing__(self, key):
        raise MissingTicker(f"{key} has fewer than {W} real adjusted daily bars")

def api(method, url, **kwargs):
    r = requests.request(method, url, headers=HEAD, timeout=30, **kwargs)
    if not r.ok:
        raise RuntimeError(f"{method} {url} -> {r.status_code}: {r.text[:500]}")
    return r.json() if r.text else {}

def telegram(text):
    if not (TG_TOKEN and TG_CHAT):
        print(text)
        return
    for i in range(0, len(text), 3900):
        try:
            r = requests.post(
                f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
                json={"chat_id": TG_CHAT, "text": text[i:i+3900]},
                timeout=20,
            )
            r.raise_for_status()
        except Exception as e:
            print("Telegram error:", e)

def clock():
    return api("GET", f"{PAPER}/v2/clock")

def account():
    return api("GET", f"{PAPER}/v2/account")

def positions():
    rows = api("GET", f"{PAPER}/v2/positions")
    return {r["symbol"]: r for r in rows}

def fetch_prices(today):
    start = (today - timedelta(days=420)).isoformat()
    end = datetime(today.year, today.month, today.day, tzinfo=NY).astimezone(UTC).isoformat()
    bars = {ticker: [] for ticker in TICKERS}
    token = None
    while True:
        params = {
            "symbols": ",".join(TICKERS),
            "timeframe": "1Day",
            "start": start,
            "end": end,
            "adjustment": "all",
            "feed": "sip",
            "limit": 10000,
            "sort": "asc",
        }
        if token:
            params["page_token"] = token
        data = api("GET", f"{DATA}/v2/stocks/bars", params=params)
        for ticker, rows in data.get("bars", {}).items():
            bars[ticker].extend(rows)
        token = data.get("next_page_token")
        if not token:
            break

    prices = GatedPrices()
    for ticker, rows in bars.items():
        closes = [float(r["c"]) for r in rows if "c" in r]
        if len(closes) >= W:
            prices[ticker] = closes[-W:]
    return prices

def latest_iex_prices(symbols):
    if not symbols:
        return {}
    data = api(
        "GET",
        f"{DATA}/v2/stocks/trades/latest",
        params={"symbols": ",".join(sorted(symbols)), "feed": "iex"},
    )
    out = {}
    for symbol, row in data.get("trades", {}).items():
        p = row.get("p")
        if p is not None and float(p) > 0:
            out[symbol] = float(p)
    missing = set(symbols) - set(out)
    if missing:
        raise RuntimeError("Missing live IEX price: " + ", ".join(sorted(missing)))
    return out

def today_orders(today):
    start = datetime(today.year, today.month, today.day, tzinfo=NY).astimezone(UTC).isoformat()
    end = (datetime(today.year, today.month, today.day, tzinfo=NY) + timedelta(days=1)).astimezone(UTC).isoformat()
    rows = api("GET", f"{PAPER}/v2/orders", params={
        "status": "all", "after": start, "until": end, "limit": 500, "direction": "desc"
    })
    prefix = f"lr-{today:%Y%m%d}-"
    return [r for r in rows if str(r.get("client_order_id", "")).startswith(prefix)]

def submit(symbol, qty, side, today):
    return api("POST", f"{PAPER}/v2/orders", json={
        "symbol": symbol,
        "qty": str(int(qty)),
        "side": side,
        "type": "market",
        "time_in_force": "cls",
        "client_order_id": f"lr-{today:%Y%m%d}-{symbol}-{side}"[:48],
    })

def assert_dedicated_account(current):
    outside = sorted(set(current) - MANAGED)
    if outside:
        raise RuntimeError(
            "Safety stop: Alpaca Paper contains positions outside this strategy: "
            + ", ".join(outside)
        )

def minutes_to_close(market_clock, now):
    close_at = datetime.fromisoformat(market_clock["next_close"]).astimezone(NY)
    return (close_at - now).total_seconds() / 60.0

def build_targets(today, equity, current):
    prices = fetch_prices(today)
    weights = run_strategy(prices)
    total = sum(weights.values())
    if not (0.999999 <= total <= 1.000001):
        raise RuntimeError(f"Weight sum invalid: {total}")

    # Strategy signal remains prior-day adjusted SIP data.
    # Live IEX is used only to convert target dollars into whole-share quantities.
    live = latest_iex_prices(set(weights))
    target_qty = {
        s: max(0, int(math.floor(equity * w / live[s])))
        for s, w in weights.items()
    }
    current_qty = {s: int(float(r["qty"])) for s, r in current.items()}
    all_symbols = set(current_qty) | set(target_qty)
    deltas = {s: target_qty.get(s, 0) - current_qty.get(s, 0) for s in all_symbols}
    return prices, weights, live, target_qty, current_qty, deltas

def trade():
    now = datetime.now(NY)
    today = now.date()
    c = clock()

    if not c.get("is_open", False):
        print("Scheduled check: market is not open. No trade.")
        return

    # Dynamic close-time guard also handles US early-close sessions.
    mins = minutes_to_close(c, now)
    if not (15 <= mins <= 30):
        print(f"Scheduled check: {mins:.1f} minutes to close. Outside trade window.")
        return

    existing = today_orders(today)
    if existing:
        telegram(
            "PAPER RUN BLOCKED\n"
            f"Date: {today}\n"
            f"Found {len(existing)} strategy order(s) already submitted today.\n"
            "No duplicate orders were sent."
        )
        return

    acct = account()
    if acct.get("trading_blocked"):
        raise RuntimeError("Alpaca account is trading_blocked")

    equity = float(acct["equity"])
    buying_power = float(acct.get("buying_power", 0))
    current = positions()

    # Fail closed rather than accidentally touching holdings outside this strategy.
    assert_dedicated_account(current)

    prices, weights, live, target_qty, current_qty, deltas = build_targets(
        today, equity, current
    )

    # MOC sells do not fill until the close, so do not assume their proceeds are
    # available first. Require existing buying power to cover all opening buys.
    estimated_buys = sum(max(d, 0) * live[s] for s, d in deltas.items())
    if estimated_buys > buying_power + 1e-6:
        telegram(
            "PAPER RUN SAFETY STOP\n"
            f"Date: {today}\n"
            f"Estimated buys: ${estimated_buys:,.2f}\n"
            f"Current buying power: ${buying_power:,.2f}\n"
            "No orders were submitted."
        )
        return

    telegram(
        "ALPACA PAPER RUN STARTED\n"
        f"Date: {today}\n"
        f"Account equity: ${equity:,.2f}\n"
        f"Minutes to market close: {mins:.1f}"
    )

    submitted = []
    errors = []

    # Submit closing-auction sells first, then buys. They all await the close.
    for side in ("sell", "buy"):
        for symbol, delta in sorted(deltas.items()):
            qty = -delta if side == "sell" else delta
            if qty <= 0:
                continue
            try:
                submitted.append(submit(symbol, qty, side, today))
            except Exception as e:
                errors.append(f"{symbol} {side} {qty}: {e}")
                break
        if errors:
            break

    lines = [
        "ALPACA PAPER RUN SUBMITTED" if not errors else "ALPACA PAPER RUN PARTIAL/FAILED",
        "",
        f"Date: {today}",
        f"Eligible tickers: {len(prices)}/{len(TICKERS)}",
        f"Target assets: {len(weights)}",
        f"Orders accepted by API: {len(submitted)}",
        "",
        "TARGET PORTFOLIO",
    ]
    for s, w in sorted(weights.items(), key=lambda x: -x[1]):
        lines.append(
            f"{s}: {w*100:.2f}% | target {target_qty[s]} | "
            f"current {current_qty.get(s,0)} | change {deltas[s]:+d}"
        )

    if errors:
        lines += ["", "ERROR", *errors, "", "Review Alpaca Paper before any rerun."]
    else:
        lines += [
            "",
            "Orders were submitted for the closing auction.",
            "Final fills will be checked automatically after the close.",
        ]
    telegram("\n".join(lines))

    if errors:
        raise RuntimeError(errors[0])

def verify():
    now = datetime.now(NY)
    today = now.date()

    cal = api(
        "GET",
        f"{PAPER}/v2/calendar",
        params={"start": today.isoformat(), "end": today.isoformat()},
    )

    # On holidays, report once at the normal 16:20 ET check only.
    if not cal:
        if now.hour == 16 and 10 <= now.minute <= 40:
            telegram(
                "DAILY PAPER STATUS\n"
                f"Date: {today}\n"
                "US market holiday / no trading session today.\n"
                "No strategy trade expected."
            )
        else:
            print("No trading session today. Waiting for the single daily status window.")
        return

    close_text = cal[0]["close"]
    close_time = datetime.strptime(close_text, "%H:%M").time()
    close_dt = datetime.combine(today, close_time, tzinfo=NY)
    after_close = (now - close_dt).total_seconds() / 60.0

    # Tight window prevents duplicate post-close Telegram reports.
    if not (10 <= after_close <= 45):
        print(f"Scheduled verify check: {after_close:.1f} minutes after close. Skip.")
        return

    orders = today_orders(today)
    current = positions()
    assert_dedicated_account(current)

    if not orders:
        telegram(
            "DAILY PAPER STATUS\n"
            f"Date: {today}\n"
            "No strategy orders were found today.\n"
            "This can mean no rebalance was needed or the trade run was missed.\n"
            "Check GitHub Actions if you expected orders."
        )
        return

    counts = {}
    for o in orders:
        status = str(o.get("status", "unknown"))
        counts[status] = counts.get(status, 0) + 1

    lines = [
        "ALPACA PAPER CLOSE CHECK",
        "",
        f"Date: {today}",
        f"Strategy orders: {len(orders)}",
        "Order status: " + ", ".join(
            f"{k}={v}" for k, v in sorted(counts.items())
        ),
        "",
        "ORDERS",
    ]

    for o in sorted(orders, key=lambda x: x.get("symbol", "")):
        lines.append(
            f"{o.get('symbol')} {o.get('side')} {o.get('qty')} | "
            f"{o.get('status')} | filled {o.get('filled_qty','0')} "
            f"@ {o.get('filled_avg_price') or '-'}"
        )

    bad = [o for o in orders if o.get("status") != "filled"]
    if bad:
        lines += [
            "",
            "ATTENTION",
            "One or more orders were not fully filled. Review Alpaca Paper.",
        ]
    else:
        lines += ["", "All strategy orders were filled."]

    telegram("\n".join(lines))

def main():
    mode = (sys.argv[1] if len(sys.argv) > 1 else "trade").lower()
    if mode == "trade":
        trade()
    elif mode == "verify":
        verify()
    else:
        raise ValueError("Usage: python trader.py [trade|verify]")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        telegram(
            "ALPACA PAPER AUTOMATION FAILED\n"
            f"{datetime.now(NY):%Y-%m-%d %H:%M ET}\n"
            f"{type(e).__name__}: {e}"
        )
        raise
