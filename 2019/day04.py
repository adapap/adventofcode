"""Day 4: Secure Container"""
from aoctools import *

data = Data.fetch(day=4, year=2019)
def valid(s, part_b=False):
    prev = s[0]
    for char in s[1:]:
        if char < prev:
            return False
        prev = char
    if part_b:
        return any(x * 2 in s and not x * 3 in s for x in '0123456789')
    return any(x * 2 in s for x in '0123456789')
start, end = map(int, data.split('-'))
total = sum(valid(str(n)) for n in range(start, end + 1))
print_ans('4a', total)
total = sum(valid(str(n), part_b=True) for n in range(start, end + 1))
print_ans('4b', total)