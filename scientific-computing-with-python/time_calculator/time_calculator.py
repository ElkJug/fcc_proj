def add_time(start: str, duration: str, week: str = '') -> str:
    # a start time in the 12-hour clock format (ending in AM or PM)
    # a duration time that indicates the number of hours and minutes
    return _tstamp(_ttick(start) + _ttick(duration), week)


# 11:06 PM -> 23:06 -> 23 x 60 + 6 = 1386
def _ttick(timestamp: str) -> int:
    mtime_str = timestamp.split()[0].split(':')
    mtime = [int(each) for each in mtime_str]
    ampm = 12 if "pm" in timestamp.lower() else 0
    ticks = (mtime[0] + ampm) * 60 + mtime[1]
    return ticks


# 1440/ticks = (hh):(mm) (AM/PM)(/, Mondays)){ (next day)/(x day later)}
def _tstamp(ticks: int, weekdays: str) -> str:
    # ticks -> dd(0-inf) hh(0-12) mm(0-60)
    days = ticks // 1440
    hours = (ticks % 1440) // 60
    minutes = (ticks % 1440) % 60
    #format
    r_ampm = _format_ampm(hours)
    r_hours = _format_twelvehour(hours)
    r_minutes =_format_minutes(minutes)
    r_days = _format_day_announcer(days)
    r_weekdays = _format_weekdays(weekdays, days)
    return f'{r_hours}:{r_minutes} {r_ampm}{r_weekdays}{r_days}'


def _format_minutes(minutes: int) -> str:
    return f'{minutes:02}'


def _format_ampm(hours: int) -> str:
    return 'AM' if hours < 12 else 'PM'


def _format_twelvehour(hours: int) -> int:
    _f_hours = hours if hours <= 12 else hours - 12
    if _f_hours == 0: _f_hours = 12
    return _f_hours


def _format_day_announcer(days:int)-> str:
    if days <= 0:
        return ''
    else:
        return f' ({"next day" if days < 2 else str(days) +" days later"})'


def _format_weekdays(weekdays:str, days:int)-> str:
    if weekdays == '':
        return ''
    else:
        total = _swap_weekdays(weekdays) + days
        local_week = total%7
        if local_week == 0: local_week = 7
        return f', {_swap_weekdays(local_week)}'

def _swap_weekdays(_input):
    selectweek = {
        1: 'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday',
        7:'Sunday'
    }
    if isinstance(_input, int):
        return selectweek.get(_input)
    elif isinstance(_input, str):
        _input = _input[:1].capitalize() + _input[1:].lower()
        for key, val in selectweek.items():
            if _input == val:
                return key
    else:
        return ''