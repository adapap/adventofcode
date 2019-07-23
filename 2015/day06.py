"""Day 6: Probably a Fire Hazard"""
from aoctools import *
import re

data = Data.fetch_by_line(day=6, year=2015)
grid = Grid2D(default=0)
grid2 = Grid2D(default=0)
for line in data:
    groups = re.match(r'(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)', line).groups()
    cmd = groups[0]
    x1, y1, x2, y2 = map(int, groups[1:])
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if cmd == 'toggle':
                grid[(x, y)] ^= 1
                grid2[(x, y)] += 2
            elif cmd == 'turn off':
                grid[(x, y)] = 0
                grid2[(x, y)] = max(0, grid2[(x, y)] - 1)
            elif cmd == 'turn on':
                grid[(x, y)] = 1
                grid2[(x, y)] += 1
on = 0
bright = 0
for x in range(1000):
    for y in range(1000):
        on += grid[(x, y)]
        bright += grid2[(x, y)]
print_ans('6a', on)
print_ans('6b', bright)