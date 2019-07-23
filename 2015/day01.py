"""Day 1: Not Quite Lisp"""
from aoctools import *
data = Data.fetch(day=1, year=2015)
floor = data.count('(') - data.count(')')
print_ans('1a', floor)

floor = 0
for i, c in enumerate(data):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    if floor < 0:
        print_ans('1b', i + 1)
        break