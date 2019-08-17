"""Day 8: Matchsticks"""
from aoctools import *

import re

data = Data.fetch_by_line(day=8, year=2015)
#data = ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']
raw = 0
parsed = 0
encoded = 0
for line in data:
    raw += len(line)
    regex = r'(\\x[0-9a-f]{2}|\\\\|\\\")'
    groups = re.findall(regex, line)
    string = re.sub(regex + r'|(")', '', line)
    parsed += len(string) + len(groups)

    string = re.sub(r'("|\\)', r'\\\1', line)
    encoded += len(string) + 2
print_ans('8a', raw - parsed)
print_ans('8b', encoded - raw)