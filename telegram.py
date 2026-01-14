import requests
TG_TOKEN="8393755630:AAGUVUVIZ1u19ah10VZb1SDUhU7xXEG4XDU"
TG_CHAT_ID = 5127514691
def send_telegram(text):
    url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    data = {
    "chat_id": TG_CHAT_ID,
    "text": text,
    "parse_mode": "HTML"
    }
    requests.post(url, data=data)
def build_message(symbol, direction, close_price, max_lvl, min_lvl, opens):
    emoji = "🚀" if direction == "UP" else "🔻"
    text = (
        f"<b>{emoji} {symbol} BREAKOUT</b>\n\n"
        f"<b>Close:</b> <code>{close_price}</code>\n"
        f"<b>Max HTF Open:</b> <code>{max_lvl}</code>\n"
        f"<b>Min HTF Open:</b> <code>{min_lvl}</code>\n\n"
        "<b>HTF Opens:</b>\n"
    )
    for tf, price in opens.items():
        text += f"{tf}: <code>{price}</code>\n"
    text += (
        f"\n<a href='https://www.tradingview.com/chart/?symbol=BINANCE:{symbol}'>"
        "📊 TradingView</a>"
    )
    return text