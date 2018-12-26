"""Day 25: Four-Dimensional Adventure"""
from aoctools import Data, print_ans

import re
from collections import defaultdict
data = Data.fetch_by_line(day=25, year=2018)

class Point:
    def __init__(self, coords):
        self.coords = coords
    def manhattan(self, other):
        return sum(abs(x - y) for x, y in zip(self.coords, other.coords))
    def __repr__(self):
        return str(self.coords)

# data = """1,-1,-1,-2
# -2,-2,0,1
# 0,2,1,3
# -2,3,-2,1
# 0,2,3,-2
# -1,-1,1,-2
# 0,-2,-1,0
# -2,2,3,-1
# 1,2,2,0
# -1,-2,0,-2""".split('\n')

points = []
for line in data:
    p = Point(tuple(map(int, re.match(r'(-?\d+),(-?\d+),(-?\d+),(-?\d+)', line.strip()).groups())))
    points.append(p)

graph = defaultdict(list)
for point in points:
    for other in points:
        if point != other and point.manhattan(other) <= 3:
            graph[point].append(other)

seen = set()
constellations = {}
n = 0
for point in points:
    if point in seen:
        continue
    seen.add(point)
    n += 1
    search = True
    point_list = [point]
    while search:
        search = False
        new_points = []
        for point in point_list:
            for child in graph[point]:
                if child not in seen:
                    search = True
                    seen.add(child)
                    new_points.append(child)
        point_list.extend(new_points)
    constellations[n] = point_list

print_ans('25a', n)