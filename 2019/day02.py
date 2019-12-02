"""Day 2: 1202 Program Alarm"""
from aoctools import *

data = Data.fetch(day=2, year=2019)
# data = '1,9,10,3,2,3,11,0,99,30,40,50'
codes = list(map(int, data.split(',')))
def evaluate(x, y, codes):
    pos = 0
    codes[1:3] = x, y
    while (op := codes[pos]) != 99:
        a, b, r = codes[pos + 1:pos + 4]
        if op == 1:
            codes[r] = codes[a] + codes[b]
        elif op == 2:
            codes[r] = codes[a] * codes[b]
        else:
            break
        pos += 4
    return codes[0]
print_ans('2a', evaluate(12, 2, codes[:]))
goal = 19690720
for noun in range(100):
    flag = False
    for verb in range(100):
        if evaluate(noun, verb, codes[:]) == goal:
            flag = True
            break
    if flag:
        print_ans('2b', 100 * noun + verb)
        break