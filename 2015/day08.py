"""Day 8: Matchsticks"""
from aoctools import *

import re

data = Data.fetch_by_line(day=8, year=2015)
raw = 0
parsed = 0
for line in data:
    raw += len(line)
    groups = re.findall(r'(\\x[0-9a-f]{2}|\\\\|\\\")', line)
    print(groups)