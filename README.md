# Leveraged Rotation Trader (Paper Only)

Frozen strategy: **81 / 28 / 90-70 / 70-75**.

This package is for Alpaca **Paper Trading**. It preserves the generated strategy tree and 220-real-bar gate. Signals use Alpaca adjusted daily bars through the prior completed day. Orders use whole-share market-on-close (`time_in_force=cls`).

Required GitHub Actions secrets:
- `ALPACA_API_KEY`
- `ALPACA_SECRET_KEY`
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`

Important: default market-data feed is `sip`. The script intentionally fails instead of silently switching to IEX if SIP is unavailable, because changing the feed can change signals.
