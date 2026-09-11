import argparse
import json
import math
import os
import statistics
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

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
PAPER_START_DATE = os.environ.get("PAPER_START_DATE", "2026-09-11")
NY = ZoneInfo("America/New_York")
UTC = ZoneInfo("UTC")
PAPER = "https://paper-api.alpaca.markets"
DATA = "https://data.alpaca.markets"
KEY = os.environ["ALPACA_API_KEY"]
SECRET = os.environ["ALPACA_SECRET_KEY"]
TG_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TG_CHAT = os.environ.get("TELEGRAM_CHAT_ID", "")
HEAD = {"APCA-API-KEY-ID": KEY, "APCA-API-SECRET-KEY": SECRET}
FAILURE_MARKER = Path(".trader_failure_notified")


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
        r = requests.post(
            f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
            json={"chat_id": TG_CHAT, "text": text[i:i + 3900]},
            timeout=20,
        )
        r.raise_for_status()


def money(value, signed=False):
    value = float(value)
    return f"{value:+,.2f}" if signed else f"{value:,.2f}"


def pct(value):
    return f"{float(value) * 100:+.2f}%"


def pnl_icon(value):
    value = float(value)
    return "🟢" if value > 0 else "🔴" if value < 0 else "⚪"


def notify_failure(title, date_text, stage, reason, order_text, account_text=""):
    parts = [
        f"🚨 {title}",
        date_text,
        "",
        "❌ 執行失敗",
        f"失敗階段：{stage}",
        f"原因：{reason}",
        "",
        "🔄 今日訂單",
        order_text,
    ]
    if account_text:
        parts += ["", "💰 帳戶狀態", account_text]
    parts += [
        "",
        "⚠️ 系統狀態",
        "策略：❌ 未正常完成",
        "交易：❌ 未正常完成",
        "",
        "🔴 系統異常",
    ]
    telegram("\n".join(parts))
    FAILURE_MARKER.write_text("1", encoding="utf-8")


def clock():
    return api("GET", f"{PAPER}/v2/clock")


def account():
    return api("GET", f"{PAPER}/v2/account")


def positions():
    rows = api("GET", f"{PAPER}/v2/positions")
    return {row["symbol"]: row for row in rows}


def calendar_session(today):
    rows = api("GET", f"{PAPER}/v2/calendar", params={"start": today.isoformat(), "end": today.isoformat()})
    return rows[0] if rows else None


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
        closes = [float(row["c"]) for row in rows if "c" in row]
        if len(closes) >= W:
            prices[ticker] = closes[-W:]
    return prices


def latest_iex_prices(symbols):
    symbols = set(symbols)
    if not symbols:
        return {}
    data = api("GET", f"{DATA}/v2/stocks/trades/latest", params={"symbols": ",".join(sorted(symbols)), "feed": "iex"})
    out = {}
    for symbol, row in data.get("trades", {}).items():
        p = row.get("p")
        if p is not None and float(p) > 0:
            out[symbol] = float(p)
    missing = symbols - set(out)
    if missing:
        raise RuntimeError("Missing live IEX price: " + ", ".join(sorted(missing)))
    return out


def today_orders(today):
    start = datetime(today.year, today.month, today.day, tzinfo=NY).astimezone(UTC).isoformat()
    end = (datetime(today.year, today.month, today.day, tzinfo=NY) + timedelta(days=1)).astimezone(UTC).isoformat()
    rows = api("GET", f"{PAPER}/v2/orders", params={"status": "all", "after": start, "until": end, "limit": 500, "direction": "desc"})
    prefix = f"lr-{today:%Y%m%d}-"
    return [row for row in rows if str(row.get("client_order_id", "")).startswith(prefix)]


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
        raise RuntimeError("Alpaca Paper contains positions outside this strategy: " + ", ".join(outside))


def minutes_to_close(market_clock, now):
    close_at = datetime.fromisoformat(market_clock["next_close"]).astimezone(NY)
    return (close_at - now).total_seconds() / 60.0


def account_snapshot(acct, current):
    equity = float(acct["equity"])
    last_equity = float(acct.get("last_equity") or equity)
    cash = float(acct.get("cash") or 0.0)
    market_value = sum(float(row.get("market_value") or 0.0) for row in current.values())
    daily_pnl = equity - last_equity
    daily_pct = daily_pnl / last_equity if last_equity else 0.0
    intraday_unrealized = sum(float(row.get("unrealized_intraday_pl") or 0.0) for row in current.values())
    realized_est = daily_pnl - intraday_unrealized
    return {
        "equity": equity,
        "last_equity": last_equity,
        "cash": cash,
        "market_value": market_value,
        "daily_pnl": daily_pnl,
        "daily_pct": daily_pct,
        "intraday_unrealized": intraday_unrealized,
        "realized_est": realized_est,
    }


def holding_lines(current, equity):
    rows = []
    for symbol, row in current.items():
        qty = int(float(row["qty"]))
        market_value = float(row.get("market_value") or 0.0)
        weight = market_value / equity if equity else 0.0
        day_pl = float(row.get("unrealized_intraday_pl") or 0.0)
        day_pc = float(row.get("unrealized_intraday_plpc") or 0.0)
        rows.append((abs(weight), f"{symbol}  {qty} 股 | {weight * 100:.1f}% | {pnl_icon(day_pl)} {pct(day_pc)} | ${money(day_pl, signed=True)}"))
    rows.sort(reverse=True)
    return [line for _, line in rows] or ["目前無持倉"]


def build_targets(today, equity, current):
    prices = fetch_prices(today)
    weights = run_strategy(prices)
    total = sum(weights.values())
    if not (0.999999 <= total <= 1.000001):
        raise RuntimeError(f"Weight sum invalid: {total}")
    current_qty = {s: int(float(r["qty"])) for s, r in current.items()}
    live_symbols = set(weights) | set(current_qty)
    live = latest_iex_prices(live_symbols)
    target_qty = {
        s: max(0, int(math.floor(equity * w / live[s])))
        for s, w in weights.items()
    }
    all_symbols = set(current_qty) | set(target_qty)
    deltas = {s: target_qty.get(s, 0) - current_qty.get(s, 0) for s in all_symbols}
    current_weights = {s: (current_qty.get(s, 0) * live[s] / equity if equity else 0.0) for s in all_symbols}
    return {
        "eligible_count": len(prices),
        "weights": weights,
        "live": live,
        "target_qty": target_qty,
        "current_qty": current_qty,
        "deltas": deltas,
        "current_weights": current_weights,
    }


def save_state(path, payload):
    Path(path).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def load_state(path):
    p = Path(path)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def send_order_submitted(today, now, snap, target, submitted):
    lines = [
        "📤 PAPER ORDER SUBMITTED",
        f"{today}  {now:%H:%M} ET",
        "",
        "💰 帳戶總資產",
        f"${money(snap['equity'])}",
        "",
        "🔄 今日調倉",
    ]
    for order in submitted:
        symbol = order["symbol"]
        side = order["side"].upper()
        qty = int(float(order["qty"]))
        ref = target["live"][symbol]
        estimate = qty * ref
        current_w = target["current_weights"].get(symbol, 0.0)
        target_w = target["weights"].get(symbol, 0.0)
        lines += [
            f"{side} {symbol}  {qty} 股",
            "掛單方式：MOC（無固定掛單價）",
            f"送單參考價：${money(ref)}",
            f"預估金額：${money(estimate)}",
            f"原因：目前 {current_w * 100:.1f}% → 策略目標 {target_w * 100:.1f}%",
            "",
        ]
    if lines[-1] == "":
        lines.pop()
    lines += [
        "",
        "目前狀態：訂單已送出，等待收盤成交。",
        "實際成交價會在收盤後 Daily Report 顯示。",
    ]
    telegram("\n".join(lines))


def send_partial_failure(today, now, expected, submitted, failed_text):
    lines = [
        "🚨 ALERT — PARTIAL FAILURE",
        f"{today}  {now:%H:%M} ET",
        "",
        "⚠️ 執行中途發生異常",
        f"原本預計：{expected} 筆",
        f"成功送出：{len(submitted)} 筆",
        f"尚未成功：{max(expected - len(submitted), 0)} 筆",
        "",
        "✅ 已送出",
    ]
    lines += [f"{o['side'].upper()} {o['symbol']}  {int(float(o['qty']))} 股" for o in submitted]
    lines += [
        "",
        "❌ 異常原因",
        failed_text,
        "",
        "📦 目前狀態",
        "部分訂單已經送出，目前持倉可能與策略目標不同。",
        "",
        "⚠️ 重要",
        "不要直接重新執行策略，請先確認 Alpaca Paper 訂單與持倉。",
        "",
        "🔴 系統異常",
    ]
    telegram("\n".join(lines))
    FAILURE_MARKER.write_text("1", encoding="utf-8")


def trade(state_file):
    now = datetime.now(NY)
    today = now.date()
    stage = "初始化"
    submitted = []
    try:
        stage = "確認美股交易時間"
        market_clock = clock()
        if not market_clock.get("is_open", False):
            print("Market is not open. No trade check needed.")
            return
        mins = minutes_to_close(market_clock, now)
        if not (15 <= mins <= 30):
            print(f"{mins:.1f} minutes to close. Outside approved trade window.")
            return

        stage = "確認今天是否已經送過策略訂單"
        existing = today_orders(today)
        if existing:
            print(f"Found {len(existing)} strategy orders already submitted today. Duplicate blocked.")
            return

        stage = "取得 Alpaca 帳戶與持倉"
        acct = account()
        current = positions()
        assert_dedicated_account(current)
        if acct.get("trading_blocked"):
            raise RuntimeError("Alpaca account is trading_blocked")
        snap = account_snapshot(acct, current)

        stage = "計算今日策略目標"
        target = build_targets(today, snap["equity"], current)
        nonzero = {s: d for s, d in target["deltas"].items() if d != 0}
        state = {
            "date": today.isoformat(),
            "status": "NO_TRADE" if not nonzero else "TRADE_REQUIRED",
            "equity_before": snap["equity"],
            "eligible_count": target["eligible_count"],
            "weights": target["weights"],
            "target_qty": target["target_qty"],
            "current_qty_before": target["current_qty"],
            "current_weights_before": target["current_weights"],
            "reference_prices": target["live"],
            "deltas": target["deltas"],
        }
        if not nonzero:
            save_state(state_file, state)
            print("Strategy completed normally. No rebalance required.")
            return

        stage = "檢查 Buying Power"
        buying_power = float(acct.get("buying_power") or 0.0)
        estimated_buys = sum(max(d, 0) * target["live"][s] for s, d in target["deltas"].items())
        if estimated_buys > buying_power + 1e-6:
            raise RuntimeError(f"Estimated buys ${estimated_buys:,.2f} exceed buying power ${buying_power:,.2f}")

        expected_orders = sum(1 for d in target["deltas"].values() if d != 0)
        stage = "送出 Alpaca Paper MOC 訂單"
        for side in ("sell", "buy"):
            for symbol, delta in sorted(target["deltas"].items()):
                qty = -delta if side == "sell" else delta
                if qty <= 0:
                    continue
                try:
                    submitted.append(submit(symbol, qty, side, today))
                except Exception as e:
                    send_partial_failure(today, now, expected_orders, submitted, f"{symbol} {side.upper()} {qty} 股：{e}")
                    raise

        state["status"] = "ORDERS_SUBMITTED"
        state["submitted_order_ids"] = [o.get("id") for o in submitted]
        save_state(state_file, state)
        send_order_submitted(today, now, snap, target, submitted)

    except Exception as e:
        if FAILURE_MARKER.exists():
            raise
        order_text = f"已送出 {len(submitted)} 筆訂單。請先確認 Alpaca Paper。" if submitted else "送出訂單：0 筆\n沒有任何訂單被送出。"
        acct_text = ""
        try:
            acct_text = f"總資產：${money(float(account()['equity']))}"
        except Exception:
            pass
        notify_failure("ALERT — FAILED", f"{today}  {now:%H:%M} ET", stage, str(e), order_text, acct_text)
        raise



def portfolio_history_series(today, current_equity):
    start_date = datetime.strptime(PAPER_START_DATE, "%Y-%m-%d").date()
    data = api(
        "GET",
        f"{PAPER}/v2/account/portfolio/history",
        params={
            "start": start_date.isoformat(),
            "end": datetime.now(UTC).isoformat(),
            "timeframe": "1D",
            "cashflow_types": "NONE",
        },
    )

    pairs = []
    for ts, eq in zip(data.get("timestamp", []), data.get("equity", [])):
        if eq is None:
            continue
        eq = float(eq)
        if eq <= 0:
            continue
        day = datetime.fromtimestamp(int(ts), UTC).astimezone(NY).date()
        if day >= start_date and day <= today:
            pairs.append((day, eq))

    by_day = {}
    for day, eq in pairs:
        by_day[day] = eq

    # At report time Alpaca may not have published the newest 1D point yet.
    # Use the live account equity as today's closing snapshot.
    by_day[today] = float(current_equity)

    return sorted(by_day.items())


def spy_history_series(today):
    start_date = datetime.strptime(PAPER_START_DATE, "%Y-%m-%d").date()
    query_start = start_date - timedelta(days=10)
    # Free SIP requires the requested data to be outside the recent-data window.
    safe_end = datetime.now(UTC) - timedelta(minutes=16)

    data = api(
        "GET",
        f"{DATA}/v2/stocks/SPY/bars",
        params={
            "timeframe": "1Day",
            "start": query_start.isoformat(),
            "end": safe_end.isoformat(),
            "adjustment": "all",
            "feed": "sip",
            "limit": 10000,
            "sort": "asc",
        },
    )

    rows = []
    for bar in data.get("bars", []):
        if "c" not in bar or "t" not in bar:
            continue
        stamp = str(bar["t"]).replace("Z", "+00:00")
        day = datetime.fromisoformat(stamp).astimezone(NY).date()
        if start_date <= day <= today:
            rows.append((day, float(bar["c"])))

    by_day = {}
    for day, close in rows:
        by_day[day] = close

    return sorted(by_day.items())


def series_returns(series):
    out = []
    for i in range(1, len(series)):
        prev = float(series[i - 1][1])
        cur = float(series[i][1])
        if prev > 0:
            out.append(cur / prev - 1.0)
    return out


def max_drawdown(values):
    if not values:
        return None, None
    peak = float(values[0])
    worst = 0.0
    for value in values:
        value = float(value)
        peak = max(peak, value)
        if peak > 0:
            worst = min(worst, value / peak - 1.0)
    current = float(values[-1]) / peak - 1.0 if peak > 0 else 0.0
    return worst, current


def calc_metrics(series, today):
    if not series:
        return None

    values = [float(v) for _, v in series]
    start_value = values[0]
    end_value = values[-1]
    returns = series_returns(series)
    trading_days = len(series)

    cumulative = end_value / start_value - 1.0 if start_value else 0.0
    cumulative_pnl = end_value - start_value

    current_year = today.year
    year_indices = [i for i, (d, _) in enumerate(series) if d.year == current_year]
    if year_indices:
        first_i = year_indices[0]
        ytd_base = values[first_i - 1] if first_i > 0 else values[first_i]
        ytd_return = end_value / ytd_base - 1.0 if ytd_base else 0.0
    else:
        ytd_return = 0.0

    max_dd, current_dd = max_drawdown(values)

    sample_ready = len(returns) >= 30
    sharpe = None
    cagr = None

    if sample_ready:
        if len(returns) >= 2:
            stdev = statistics.stdev(returns)
            if stdev > 0:
                sharpe = statistics.mean(returns) / stdev * math.sqrt(252)

        elapsed_days = max((series[-1][0] - series[0][0]).days, 1)
        if start_value > 0 and end_value > 0:
            cagr = (end_value / start_value) ** (365.25 / elapsed_days) - 1.0

    return {
        "start_date": series[0][0],
        "trading_days": trading_days,
        "start_value": start_value,
        "end_value": end_value,
        "cumulative_pnl": cumulative_pnl,
        "cumulative_return": cumulative,
        "ytd_return": ytd_return,
        "cagr": cagr,
        "sharpe": sharpe,
        "max_drawdown": max_dd,
        "current_drawdown": current_dd,
        "today_return": returns[-1] if returns else 0.0,
        "sample_ready": sample_ready,
    }


def performance_bundle(today, acct):
    strategy_series = portfolio_history_series(today, float(acct["equity"]))
    spy_series = spy_history_series(today)

    strategy = calc_metrics(strategy_series, today)
    benchmark = calc_metrics(spy_series, today)

    return {
        "strategy": strategy,
        "benchmark": benchmark,
    }


def metric_or_sample(value, as_pct=False):
    if value is None:
        return "樣本不足"
    if as_pct:
        return pct(value)
    return f"{value:.2f}"


def account_snapshot(acct, current):
    equity = float(acct["equity"])
    last_equity = float(acct.get("last_equity") or equity)
    cash = float(acct.get("cash") or 0.0)
    market_value = sum(float(row.get("market_value") or 0.0) for row in current.values())
    daily_pnl = equity - last_equity
    daily_pct = daily_pnl / last_equity if last_equity else 0.0
    intraday_unrealized = sum(
        float(row.get("unrealized_intraday_pl") or 0.0)
        for row in current.values()
    )
    # Alpaca open positions expose intraday unrealized P/L but not a single
    # exact closed-position realized-P/L field, so this is an account-level estimate.
    realized_est = daily_pnl - intraday_unrealized

    return {
        "equity": equity,
        "last_equity": last_equity,
        "cash": cash,
        "market_value": market_value,
        "invested_pct": market_value / equity if equity else 0.0,
        "daily_pnl": daily_pnl,
        "daily_pct": daily_pct,
        "intraday_unrealized": intraday_unrealized,
        "realized_est": realized_est,
    }


def holding_lines(current, equity):
    rows = []
    for symbol, row in current.items():
        qty = int(float(row["qty"]))
        market_value = float(row.get("market_value") or 0.0)
        weight = market_value / equity if equity else 0.0
        day_pl = float(row.get("unrealized_intraday_pl") or 0.0)
        day_pc = float(row.get("unrealized_intraday_plpc") or 0.0)
        rows.append((
            abs(weight),
            f"{symbol:<6} {weight * 100:>5.1f}%  "
            f"{pnl_icon(day_pl)} {pct(day_pc):>7}  ${money(day_pl, signed=True)}"
        ))
    rows.sort(reverse=True)
    return [line for _, line in rows] or ["目前無持倉"]


def dashboard_common(today, acct, current, perf):
    snap = account_snapshot(acct, current)
    strategy = perf.get("strategy")
    benchmark = perf.get("benchmark")

    lines = [
        "💰 帳戶",
        f"總資產          ${money(snap['equity'])}",
        f"昨日總資產      ${money(snap['last_equity'])}",
        f"現金            ${money(snap['cash'])}",
        f"持倉比例        {snap['invested_pct'] * 100:.1f}%",
        "",
        "━━━━━━━━━━━━━━",
        "💵 今日績效",
        f"今日損益        {pnl_icon(snap['daily_pnl'])} ${money(snap['daily_pnl'], signed=True)}",
        f"今日報酬        {pnl_icon(snap['daily_pct'])} {pct(snap['daily_pct'])}",
        f"已實現損益(推算) {pnl_icon(snap['realized_est'])} ${money(snap['realized_est'], signed=True)}",
        f"未實現損益變化  {pnl_icon(snap['intraday_unrealized'])} ${money(snap['intraday_unrealized'], signed=True)}",
    ]

    lines += ["", "━━━━━━━━━━━━━━", "🏆 策略績效"]
    if strategy:
        lines += [
            f"Paper 開始日     {strategy['start_date']}",
            f"交易天數         {strategy['trading_days']} 天",
            f"累積損益        {pnl_icon(strategy['cumulative_pnl'])} ${money(strategy['cumulative_pnl'], signed=True)}",
            f"累積報酬        {pnl_icon(strategy['cumulative_return'])} {pct(strategy['cumulative_return'])}",
            f"YTD             {pct(strategy['ytd_return'])}",
            f"CAGR            {metric_or_sample(strategy['cagr'], as_pct=True)}",
            f"Sharpe Ratio    {metric_or_sample(strategy['sharpe'])}",
            f"Max Drawdown    {pct(strategy['max_drawdown'] or 0.0)}",
            f"目前 Drawdown   {pct(strategy['current_drawdown'] or 0.0)}",
        ]
    else:
        lines += ["績效資料        暫時無法取得"]

    lines += ["", "━━━━━━━━━━━━━━", "🥊 Benchmark"]
    if strategy and benchmark:
        excess = strategy["cumulative_return"] - benchmark["cumulative_return"]
        lines += [
            "                 策略       SPY",
            f"今日             {pct(strategy['today_return']):>8}   {pct(benchmark['today_return']):>8}",
            f"YTD              {pct(strategy['ytd_return']):>8}   {pct(benchmark['ytd_return']):>8}",
            f"累積             {pct(strategy['cumulative_return']):>8}   {pct(benchmark['cumulative_return']):>8}",
            f"CAGR             {metric_or_sample(strategy['cagr'], True):>8}   {metric_or_sample(benchmark['cagr'], True):>8}",
            f"Sharpe           {metric_or_sample(strategy['sharpe']):>8}   {metric_or_sample(benchmark['sharpe']):>8}",
            f"Max DD           {pct(strategy['max_drawdown'] or 0.0):>8}   {pct(benchmark['max_drawdown'] or 0.0):>8}",
            f"累積超額報酬     {pnl_icon(excess)} {pct(excess)}",
        ]
    else:
        lines += ["Benchmark 資料  暫時無法取得"]

    return snap, lines


def order_fill_lines(orders):
    lines = []
    for order in sorted(orders, key=lambda x: (x.get("side", ""), x.get("symbol", ""))):
        side = str(order.get("side", "")).upper()
        symbol = order.get("symbol", "")
        filled_qty = int(float(order.get("filled_qty") or order.get("qty") or 0))
        avg = order.get("filled_avg_price")
        status = order.get("status", "unknown")
        avg_text = f"${money(float(avg))}" if avg else "-"
        marker = "🟢" if side == "BUY" else "🔴"
        status_mark = "✅" if status == "filled" else "⚠️"
        lines.append(f"{marker} {side} {symbol}")
        lines.append(f"{filled_qty} 股 @ {avg_text}  {status_mark} {status}")
    return lines or ["今日沒有交易。"]


def append_risk_and_system(lines, perf, trade_status, order_status):
    strategy = perf.get("strategy")
    lines += ["", "━━━━━━━━━━━━━━", "🛡️ 風險"]
    if strategy:
        lines += [
            f"目前 Drawdown   {pct(strategy['current_drawdown'] or 0.0)}",
            f"歷史 Max DD     {pct(strategy['max_drawdown'] or 0.0)}",
        ]
    else:
        lines += [
            "目前 Drawdown   資料不足",
            "歷史 Max DD     資料不足",
        ]
    lines += [
        "帳戶交易狀態    ✅ 正常",
        f"今日訂單狀態    {order_status}",
        "",
        "━━━━━━━━━━━━━━",
        "⚙️ 系統",
        "策略計算        ✅ 正常",
        "市場資料        ✅ 正常",
        "Alpaca          ✅ 正常",
        f"今日調倉        {trade_status}",
        "GitHub 排程     ✅ 正常",
        "",
        "🟢 系統正常",
    ]


def send_success_report(today, acct, current, orders, state):
    perf = performance_bundle(today, acct)
    snap, lines = dashboard_common(today, acct, current, perf)
    lines = [
        "📊 美股策略｜每日結算 — SUCCESS",
        str(today),
        "",
        *lines,
        "",
        "━━━━━━━━━━━━━━",
        "📦 持倉",
        *holding_lines(current, snap["equity"]),
        "",
        "━━━━━━━━━━━━━━",
        "🔄 今日交易",
        *order_fill_lines(orders),
    ]
    append_risk_and_system(
        lines,
        perf,
        "✅ 完成",
        f"✅ 全部成交（{sum(1 for o in orders if o.get('status') == 'filled')}/{len(orders)}）",
    )
    telegram("\n".join(lines))


def send_no_trade_report(today, acct, current, state):
    perf = performance_bundle(today, acct)
    snap, lines = dashboard_common(today, acct, current, perf)
    lines = [
        "📊 美股策略｜每日結算 — NO TRADE",
        str(today),
        "",
        *lines,
        "",
        "━━━━━━━━━━━━━━",
        "📦 持倉",
        *holding_lines(current, snap["equity"]),
        "",
        "━━━━━━━━━━━━━━",
        "🔄 今日交易",
        "今日沒有交易。",
        "原因：策略已正常重新計算，目前持倉不需要調整。",
    ]
    append_risk_and_system(
        lines,
        perf,
        "✅ 不需要調倉",
        "✅ 0 筆",
    )
    telegram("\n".join(lines))


def send_market_closed_report(today, acct, current):
    snap = account_snapshot(acct, current)
    lines = [
        "📊 美股策略｜每日結算 — MARKET CLOSED",
        str(today),
        "",
        "今日美股休市。",
        "沒有執行策略交易，也沒有送出任何訂單。",
        "",
        "━━━━━━━━━━━━━━",
        "💰 帳戶",
        f"總資產          ${money(snap['equity'])}",
        f"現金            ${money(snap['cash'])}",
        f"持倉比例        {snap['invested_pct'] * 100:.1f}%",
        "",
        "━━━━━━━━━━━━━━",
        "📦 持倉",
        *holding_lines(current, snap["equity"]),
        "",
        "━━━━━━━━━━━━━━",
        "⚙️ 系統",
        "GitHub 排程     ✅ 正常",
        "Alpaca          ✅ 正常",
        "市場狀態        ✅ 今日休市",
        "",
        "🟢 系統正常",
    ]
    telegram("\n".join(lines))


def send_order_failure_report(today, acct, current, orders):
    snap = account_snapshot(acct, current)
    filled = [o for o in orders if o.get("status") == "filled"]
    bad = [o for o in orders if o.get("status") != "filled"]
    title = "🚨 ALERT — PARTIAL FAILURE" if filled and bad else "🚨 ALERT — FAILED"

    lines = [
        title,
        str(today),
        "",
        "⚠️ 收盤成交檢查異常",
        f"策略訂單：{len(orders)} 筆",
        f"完整成交：{len(filled)} 筆",
        f"未完整成交：{len(bad)} 筆",
        "",
        "━━━━━━━━━━━━━━",
        "🔄 今日訂單",
    ]

    for order in sorted(orders, key=lambda x: x.get("symbol", "")):
        status = order.get("status", "unknown")
        marker = "✅" if status == "filled" else "❌"
        avg = order.get("filled_avg_price")
        avg_text = f"${money(float(avg))}" if avg else "-"
        lines.append(
            f"{marker} {str(order.get('side','')).upper()} {order.get('symbol')}  "
            f"{order.get('qty')} 股 | {status} | 成交 {order.get('filled_qty','0')} @ {avg_text}"
        )

    lines += [
        "",
        "━━━━━━━━━━━━━━",
        "💰 帳戶",
        f"總資產          ${money(snap['equity'])}",
        f"現金            ${money(snap['cash'])}",
        f"持倉比例        {snap['invested_pct'] * 100:.1f}%",
        "",
        "━━━━━━━━━━━━━━",
        "📦 實際持倉",
        *holding_lines(current, snap["equity"]),
        "",
        "━━━━━━━━━━━━━━",
        "⚠️ 重要",
        "目前持倉可能與策略目標不同。",
        "不要直接重新執行策略，請先確認 Alpaca Paper 訂單與持倉。",
        "",
        "🔴 系統異常",
    ]
    telegram("\n".join(lines))
    FAILURE_MARKER.write_text("1", encoding="utf-8")


def verify(state_file):
    now = datetime.now(NY)
    today = now.date()
    stage = "收盤後確認"
    try:
        session = calendar_session(today)

        if session is None:
            if now.hour < 16:
                print("Market holiday. Waiting for the later daily report run.")
                return
            acct = account()
            current = positions()
            assert_dedicated_account(current)
            send_market_closed_report(today, acct, current)
            return

        close_time = datetime.strptime(session["close"], "%H:%M").time()
        close_dt = datetime.combine(today, close_time, tzinfo=NY)
        after_close = (now - close_dt).total_seconds() / 60.0

        if not (10 <= after_close <= 45):
            print(f"{after_close:.1f} minutes after close. Outside report window.")
            return

        stage = "讀取今日策略執行紀錄"
        state = load_state(state_file)

        stage = "取得收盤後帳戶與訂單"
        acct = account()
        current = positions()
        assert_dedicated_account(current)
        orders = today_orders(today)

        if state is None:
            notify_failure(
                "ALERT — FAILED",
                f"{today}  {now:%H:%M} ET",
                "今日自動交易執行確認",
                "找不到今天的策略成功執行紀錄。可能是排程漏跑或交易程式未完成。",
                f"Alpaca 今日找到 {len(orders)} 筆策略訂單。",
                f"總資產：${money(float(acct['equity']))}",
            )
            raise RuntimeError("Missing daily strategy state")

        if state.get("date") != today.isoformat():
            raise RuntimeError(
                f"Strategy state date mismatch: {state.get('date')} != {today}"
            )

        if state.get("status") == "NO_TRADE":
            if orders:
                raise RuntimeError(
                    "State says NO_TRADE but Alpaca has strategy orders today"
                )
            send_no_trade_report(today, acct, current, state)
            return

        if not orders:
            notify_failure(
                "ALERT — FAILED",
                f"{today}  {now:%H:%M} ET",
                "收盤成交確認",
                "策略紀錄顯示今天需要交易，但 Alpaca 找不到今天的策略訂單。",
                "送出訂單：0 筆",
                f"總資產：${money(float(acct['equity']))}",
            )
            raise RuntimeError("Expected strategy orders were not found")

        bad = [o for o in orders if o.get("status") != "filled"]
        if bad:
            send_order_failure_report(today, acct, current, orders)
            raise RuntimeError("One or more strategy orders were not fully filled")

        send_success_report(today, acct, current, orders, state)

    except Exception as e:
        if FAILURE_MARKER.exists():
            raise

        acct_text = ""
        try:
            acct_text = f"總資產：${money(float(account()['equity']))}"
        except Exception:
            pass

        notify_failure(
            "ALERT — FAILED",
            f"{today}  {now:%H:%M} ET",
            stage,
            str(e),
            "無法確認今日訂單結果。",
            acct_text,
        )
        raise


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["trade", "verify"])
    parser.add_argument("--state-file", default=".strategy_state.json")
    args = parser.parse_args()

    FAILURE_MARKER.unlink(missing_ok=True)

    if args.mode == "trade":
        trade(args.state_file)
    else:
        verify(args.state_file)


if __name__ == "__main__":
    main()
