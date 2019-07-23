"""Day 1: Chronical Calibration"""
from aoctools import Data, print_ans
data = Data.fetch_by_line(day=1, year=2018)
freq = 0

for line in data:
    freq += int(line)
print_ans('1a', freq)

freq = 0
repeat = True
seen_freq = set()
duplicate = None

while repeat:
    for line in data:
        freq += int(line)
        if freq in seen_freq:
            repeat = False
            duplicate = freq
            break
        seen_freq.add(freq)
print_ans('1b', duplicate)