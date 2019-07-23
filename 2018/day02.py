"""Day 2: Inventory Management System"""
from aoctools import Data, print_ans

from collections import Counter
from itertools import combinations

data = Data.fetch_by_line(day=2, year=2018)

a, b = 0, 0
for line in data:
    c = Counter(line)
    if 2 in c.values():
        a += 1
    if 3 in c.values():
        b += 1
checksum = a * b
print_ans('2a', checksum)

for a, b in combinations(list(data), 2):
    diff = 0
    common = ''
    for x, y in zip(a, b):
        if x != y:
            diff += 1
        else:
            common += x
        if diff > 1:
            break
    if diff == 1:
        break
print_ans('2b', common)