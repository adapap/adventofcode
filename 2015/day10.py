"""Day 10: Elves Look, Elves Say"""
from aoctools import *

data = Data.fetch(day=10, year=2015)

def look_and_say(s):
    out = ''
    count, cur = 0, ''
    for c in s:
        if not cur == c:
            out += str(count) + cur if count else ''
            count, cur = 1, c
        else:
            count += 1
    out += str(count) + cur
    return out

s = data
for x in range(40):
    s = look_and_say(s)
print_ans('10a', len(s))

for x in range(10):
    s = look_and_say(s)
print_ans('10b', len(s))