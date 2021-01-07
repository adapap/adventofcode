import aoc
from collections import defaultdict
from copy import deepcopy

puzzle = aoc.Puzzle(day=17, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch_by_line()
# data = """.#.
# ..#
# ###""".split('\n')

class Scale:
    xmin = -1
    xmax = 1
    ymin = -1
    ymax = 1
    zmin = -1
    zmax = 1
    wmin = -1
    wmax = 1
    
    @staticmethod
    def expand(x, y, z, w=0):
        if x <= Scale.xmin:
            Scale.xmin = x - 1
        if y <= Scale.ymin:
            Scale.ymin = y - 1
        if z <= Scale.zmin:
            Scale.zmin = z - 1
        if w <= Scale.wmin:
            Scale.wmin = w - 1
        if x >= Scale.xmax:
            Scale.xmax = x + 1
        if y >= Scale.ymax:
            Scale.ymax = y + 1
        if z >= Scale.zmax:
            Scale.zmax = z + 1
        if w >= Scale.wmax:
            Scale.wmax = w + 1
    
    @staticmethod
    def show_size():
        return f'<{Scale.xmin} {Scale.ymin} {Scale.zmin} {Scale.wmin}> : ' + \
               f'<{Scale.xmax} {Scale.ymax} {Scale.zmax} {Scale.wmax}>'

grid = defaultdict(lambda: '.')
for pos, item in aoc.nested_enum(data):
    x, y = pos
    grid[x, y, 0] = item
    Scale.expand(x, y, 0)

def find_neighbors_3D(x, y, z):
    neighbors = {'#': 0, '.': 0}
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if i == j == k == 0:
                    continue
                neighbors[grid[x + i, y + j, z + k]] += 1
    return neighbors

def find_neighbors_4D(x, y, z, w):
    neighbors = {'#': 0, '.': 0}
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if i == j == k == l == 0:
                        continue
                    neighbors[grid[x + i, y + j, z + k, w + l]] += 1
    return neighbors

cycles = 6
for _ in range(cycles):
    next_grid = deepcopy(grid)
    for x in range(Scale.xmin, Scale.xmax + 1):
        for y in range(Scale.ymin, Scale.ymax + 1):
            for z in range(Scale.zmin, Scale.zmax + 1):
                neighbors = find_neighbors_3D(x, y, z)
                state = grid[x, y, z]
                if state == '#' and not (2 <= neighbors['#'] <= 3):
                    next_grid[x, y, z] = '.'
                elif state == '.' and neighbors['#'] == 3:
                    next_grid[x, y, z] = '#'
                    Scale.expand(x, y, z)
    grid = next_grid
    # print(Scale.show_size())
occupied = lambda: sum(1 if x == '#' else 0 for x in grid.values())
PART_1 = occupied()
# puzzle.submit(part=1, answer=PART_1)

grid = defaultdict(lambda: '.')
Scale.xmin = -1
Scale.xmax = 1
Scale.ymin = -1
Scale.ymax = 1
Scale.zmin = -1
Scale.zmax = 1

for pos, item in aoc.nested_enum(data):
    x, y = pos
    grid[x, y, 0, 0] = item
    Scale.expand(x, y, 0, 0)
for _ in range(cycles):
    next_grid = deepcopy(grid)
    for x in range(Scale.xmin, Scale.xmax + 1):
        for y in range(Scale.ymin, Scale.ymax + 1):
            for z in range(Scale.zmin, Scale.zmax + 1):
                for w in range(Scale.wmin, Scale.wmax + 1):
                    neighbors = find_neighbors_4D(x, y, z, w)
                    state = grid[x, y, z, w]
                    if state == '#' and not (2 <= neighbors['#'] <= 3):
                        next_grid[x, y, z, w] = '.'
                    elif state == '.' and neighbors['#'] == 3:
                        next_grid[x, y, z, w] = '#'
                        Scale.expand(x, y, z, w)
    grid = next_grid
PART_2 = occupied()
puzzle.submit(part=2, answer=PART_2)
