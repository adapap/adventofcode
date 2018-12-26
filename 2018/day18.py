"""Day 18: Settlers of the North Pole"""
from aoctools import Data, Grid, Geometry, print_ans

class Area:
    OPEN = '.'
    TREE = '|'
    LUMBERYARD = '#'

data = Data.fetch_by_line(day=18, year=2018)
# data = """.#.#...|#.
# .....#|##|
# .|..|...#.
# ..|#.....#
# #.#|||#|#|
# ...#.||...
# .|....|...
# ||...#|.#|
# |.||||..|.
# ...#.|..|.""".split('\n')

grid = Grid()
for y, x, item in Data.double_enum(data):
    grid[x, y] = item

size = (len(data), len(data[0]))
def print_grid():
    for y in range(size[1]):
        for x in range(size[0]):
            print(grid[x, y], end='')
        print()

def resource_value():
    trees = 0
    yards = 0
    for item in grid.points.values():
        if item == Area.TREE:
            trees += 1
        elif item == Area.LUMBERYARD:
            yards += 1
    return trees * yards

time = 650
last_value = 0
part_a = 0
part_b = 0
seen = {}
vals = {}

for t in range(time):
    key = str(grid.points.values())
    if key not in seen:
        seen[key] = t
        vals[t] = resource_value()
    else:
        start = seen[key]
        cycle_len = t - seen[key]
        part_b = vals[start + (1000000000 - start) % cycle_len]
        break
    new_points = grid.points.copy()
    for point, item in grid.points.items():
        adjacent = [grid[n] for n in Geometry.adjacent(point)]
        if item == Area.OPEN and adjacent.count(Area.TREE) >= 3:
            new_points[point] = Area.TREE
        elif item == Area.TREE and adjacent.count(Area.LUMBERYARD) >= 3:
            new_points[point] = Area.LUMBERYARD
        elif item == Area.LUMBERYARD:
            if adjacent.count(Area.LUMBERYARD) < 1 or adjacent.count(Area.TREE) < 1:
                new_points[point] = Area.OPEN
    grid.points.update(new_points)
    if t == 10:
        part_a = resource_value()

print_ans('18a', part_a)
print_ans('18b', part_b)