"""Day 6: Chronal Coordinates"""
from aoctools import Data, Geometry, IntTuple, print_ans

data = Data.fetch_by_line(day=6, year=2018)
# data = """1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9""".strip().split('\n')

INF = float('inf')

bounds = {
    'x': [INF, -INF],
    'y': [INF, -INF]
}
points = {}
for line in data:
    x, y = IntTuple(*line.split(', '))
    points[(x, y)] = 1
    if x < bounds['x'][0]:
        bounds['x'][0] = x
    if x > bounds['x'][1]:
        bounds['x'][1] = x
    if y < bounds['y'][0]:
        bounds['y'][0] = y
    if y > bounds['y'][1]:
        bounds['y'][1] = y

add_one = IntTuple(0, 1)
for x in range(*IntTuple(*bounds['x']) + add_one):
    for y in range(*IntTuple(*bounds['y']) + add_one):
        c = (x, y)
        if c in points:
            continue
        vals = [(Geometry.manhattan(c, p), p) for p in points]
        dists = [v[0] for v in vals]
        if dists.count(min(dists)) == 1:
            points[min(vals)[1]] += 1
largest_area = max(points.values())
print_ans('6a', largest_area)

threshold = 10000
valid = 0
seen = set()

def in_threshold(point):
    if point in seen:
        return 0
    else:
        seen.add(point)
        return sum(Geometry.manhattan(point, p) for p in points) < threshold

avg = int(round(sum(p[0] for p in points) / len(points), 0)), int(round((sum(p[1] for p in points)) / len(points), 0))
xmin, xmax = avg[0] - 1, avg[0] + 1
ymin, ymax = avg[1] - 1, avg[1] + 1
valid += in_threshold(avg)
while True:
    spirals = 0
    for x in range(xmin, xmax):
        spirals += in_threshold((x, ymin))
        spirals += in_threshold((x, ymax))
    for y in range(ymin, ymax + 1):
        spirals += in_threshold((xmin, y))
        spirals += in_threshold((xmax, y))
    if spirals == 0:
        break
    valid += spirals
    xmin -= 1
    xmax += 1
    ymin -= 1
    ymax += 1

print_ans('6b', valid)