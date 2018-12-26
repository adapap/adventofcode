"""Day 4: Repose Record"""
from aoctools import Data, IntTuple, print_ans

import datetime
import re
from collections import defaultdict

data = Data.fetch_by_line(day=4, year=2018)

def iterate_timerange(start, end):
    """Generator which yields the number of days between two times, followed by each remaining minute."""
    day_diff = (end - start).days
    yield day_diff
    start += datetime.timedelta(days=day_diff)
    while start != end:
        yield start
        start += datetime.timedelta(minutes=1)

schedule = defaultdict(dict)
minute_dict = {m: 0 for m in range(60)}
last_guard_id = 0
last_time = None
awake = True
for line in sorted(data):
    match = re.match(r'\[(\d+)-(\d+)-(\d+) (\d+):(\d+)] (.+)', line)
    year, month, day = IntTuple(match.group(1), match.group(2), match.group(3))
    hour, minute = IntTuple(match.group(4), match.group(5))
    date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute)
    info = match.group(6).split(' ')
    if info[0] == 'Guard':
        last_guard_id = info[1][1:]
        last_time = date
        if last_guard_id not in schedule:
            schedule[last_guard_id] = minute_dict.copy()
    elif info[0] == 'falls':
        last_time = date
    elif info[0] == 'wakes':
        cur_time = date
        for time in iterate_timerange(last_time, cur_time):
            if type(time) == int:
                for m in range(60):
                    schedule[last_guard_id][m] += time
            else:
                key = (time.minute)
                schedule[last_guard_id][key] += 1

best_guard_id = max(schedule, key=lambda gid: sum(schedule[gid].values()))
best_minute = max(schedule[best_guard_id], key=lambda minute: schedule[best_guard_id][minute])
total = int(best_guard_id) * best_minute
print_ans('4a', total)

best_guard = None
best_minute = None
best_val = 0
for guard, times in schedule.items():
    for minute, amount in times.items():
        if amount > best_val:
            best_val = amount
            best_minute = minute
            best_guard = guard
total = int(best_guard) * best_minute
print_ans('4b', total)