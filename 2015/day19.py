"""Day 19: Medicine for Rudolph"""
from aoctools import *
from collections import defaultdict
import re

data = Data.fetch_by_line(day=19, year=2015)
# data = """H => HO
# H => OH
# O => HH

# HOH""".split('\n')
start = data[-1]

replace = defaultdict(list)
for line in data[:-2]:
    k, _, v = line.split()
    replace[k].append(v)

combs = set()
for k in replace:
    for v in replace[k]:
        for result in re.finditer(k, start):
            combs.add(start[:result.start()] + v + start[result.end():])
print_ans('19a', len(combs))