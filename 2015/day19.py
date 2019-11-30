"""Day 19: Medicine for Rudolph"""
from aoctools import *
from collections import defaultdict
import random
import re

data = Data.fetch_by_line(day=19, year=2015)
# data = """H => HO
# H => OH
# O => HH
# e => O
# e => H

# HOHOHO""".split('\n')
start = data[-1]

replace = defaultdict(list)
compress = {}
for line in data[:-2]:
    k, _, v = line.split()
    replace[k].append(v)
    compress[v] = k

combs = set()
for k in replace:
    for v in replace[k]:
        for result in re.finditer(k, start):
            combs.add(start[:result.start()] + v + start[result.end():])
print_ans('19a', len(combs))
goal = 'e'
while True:
    curr = data[-1]
    steps = 0
    keys = list(compress.keys())
    random.shuffle(keys)
    prev = ''
    while prev != curr:
        prev = curr
        for key in keys:
            while key in curr:
                steps += curr.count(key)
                curr = curr.replace(key, compress[key])
    if curr == goal:
        break
print_ans('19b', steps)