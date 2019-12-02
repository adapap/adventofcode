from aoctools import *

data = Data.fetch_by_line(day=1, year=2019)
s = 0
for line in data:
    s += (int(line) // 3) - 2
print_ans('1a', s)
s = 0
for line in data:
    n = int(line)
    while n > 0:
        n = (n // 3) - 2
        s += max(n, 0)
print_ans('1b', s)