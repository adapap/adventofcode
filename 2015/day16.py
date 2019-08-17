"""Day 16: Aunt Sue"""
from aoctools import *
import re

data = Data.fetch_by_line(day=16, year=2015)
table = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".split('\n')

aunts = {}
for line in table:
    k, v = re.match(r'([a-z]+): (\d+)', line).groups()
    aunts[k] = int(v)
for line in data:
    keys = re.findall(r'[a-z]+', line)[1:]
    sue, *data = map(int, re.findall(r'\d+', line))
    for k, v in zip(keys, data):
        if aunts[k] != v:
            break
    else:
        print_ans('16a', sue)
    
    for k, v in zip(keys, data):
        if k in ('cats', 'trees') and v <= aunts[k]:
            break
        if k in ('pomeranians', 'goldfish') and v >= aunts[k]:
            break
        if k not in ('cats', 'trees', 'pomeranians', 'goldfish') and aunts[k] != v:
            break
    else:
        print_ans('16b', sue)