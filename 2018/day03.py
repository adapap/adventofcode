"""Day 3: No Matter How You Slice It"""
from aoctools import Data, Grid, IntTuple, print_ans

import re

def make_rect(a, b):
    """Generator for points from a (topleft) to b (topright)."""
    x1, y1 = a
    x2, y2 = b
    for x in range(x1, x2):
        for y in range(y1, y2):
            yield (x, y)

grid = Grid(default=0)
data = Data.fetch_by_line(day=3, year=2018)
shared = 0

rect_data = []

for line in data:
    match = re.match(r'#(\d+) @ (\d+,\d+): (\d+x\d+)', line)
    claim_id = match.group(1)
    point = IntTuple(*match.group(2).split(','))
    dimensions = tuple(int(x) + y for x, y in zip(match.group(3).split('x'), point))
    rect_data.append({'rect': make_rect(point, dimensions), 'id': claim_id})
    for p in make_rect(point, dimensions):
        grid[p] += 1
for count in grid.points.values():
    if count > 1:
        shared += 1
print_ans('3a', shared)

for data in rect_data:
    if all(grid[point] == 1 for point in data['rect']):
        print_ans('3b', data['id'])