import client, telegram, time, operation

SYMBOLS = [
"BTCUSDT",
"ETHUSDT",
"SOLUSDT"
]

#print(SYMBOLS)
#SYMBOLS = client.get_binance_futures_tickers()
while True:
    try:
        for symbol in SYMBOLS:
            #print(f"{symbol} start")
            klines = client.get_klines(symbol)
            #klines.reverse()
            opens = operation.get_timeframe_opens(klines)
            max_lvl, min_lvl = operation.get_levels(opens)
            close_price = operation.get_last_close(klines)
            h,l=operation.get_last_hl(klines)
            om=opens["1M"]
            signal = operation.touch_hlom(h,l, om)
            #signal = operation.check_cmaxmin(close_price, max_lvl, min_lvl)
            #signal = operation.touch_hlmaxmin(h,l, max_lvl, min_lvl)
            #print(signal)
            last_signal = {}
            if signal:
                print("i am in signal")
                prev = last_signal.get(symbol)
                if signal != prev:
                    msg = telegram.build_message(
                    symbol, signal,
                    close_price, max_lvl, min_lvl, opens
                    )
                    telegram.send_telegram(msg)
                    last_signal[symbol] = signal
            print(f"{symbol} end {signal}")
        time.sleep(60)

    except Exception as e:
        print(e)
        #telegram.send_telegram(f"❌ Error: {e}")
        time.sleep(60)