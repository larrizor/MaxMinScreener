from datetime import datetime, timezone
def get_timeframe_opens(klines):
    opens = {
    "1D": 0,
    "1W": 0,
    "1M": 0
    }
    prev_day = None
    prev_week = None
    prev_month = None
    #"print("enter in getTfOpens")
    #klines.reverse()
    for candle in klines:
        #print(f"enter in for. ts = {candle[0]}")
        ts = candle[0]
        day = datetime.utcfromtimestamp(ts / 1000).day
        #print(day)
        week = week_from_ms(ts)
        #print(week)
        month = datetime.utcfromtimestamp(ts / 1000).month
        #print(month)
        if day != prev_day and prev_day!=None and opens["1D"]==0:
            #print("Новий день:", day)
            opens["1D"]=float(candle[1])
        if week != prev_week and prev_week!=None and opens["1W"]==0:
            #print("Новий week:", week)
            opens["1W"]=float(candle[1])
        if month != prev_month and prev_month!=None and opens["1M"]==0:
            #print("Новий month:", month)
            opens["1M"]=float(candle[1])

        prev_day = day
        prev_week = week
        prev_month = month
    #print(opens)
    return opens
def get_levels(opens: dict):
    values = list(opens.values())
    return max(values), min(values)
def get_last_close(klines):
    klines.reverse()
    return float(klines[-1][4])
def get_last_hl(klines):
    return float(klines[0][2]),float(klines[0][3])
def check_cmaxmin(close_price, max_lvl, min_lvl):
    print(f"c={close_price}, max={max_lvl}, min={min_lvl}")
    if close_price > max_lvl:
        return "UP"
    if close_price < min_lvl:
        return "DOWN"
    return None
def touch_hlmaxmin(h,l, max_lvl, min_lvl):
    print(f"h={h},L={l}, max={max_lvl}, min={min_lvl}")
    if h > max_lvl>l:
        return "UP"
    if l < min_lvl<h:
        return "DOWN"
    return None
def touch_hlom(h,l, om):
    print(f"h={h},L={l}, om={om}")
    if h > om > l:
        return "UP"
    if l < om < h:
        return "DOWN"
    return None
def week_from_ms(timestamp_ms: int) -> int:
    return datetime.fromtimestamp(
    timestamp_ms / 1000, tz=timezone.utc
    ).isocalendar().week