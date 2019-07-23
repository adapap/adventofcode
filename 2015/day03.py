"""Day 3: Perfectly Spherical Houses in a Vacuum"""
from aoctools import *

data = Data.fetch(day=3, year=2015)
grid = Grid2D(default=0)
pos = grid.convert((0, 0))
grid[pos] = 1
for move in data:
    pos = {
    '^': pos + grid.north,
    'v': pos + grid.south,
    '>': pos + grid.east,
    '<': pos + grid.west
    }.get(move)
    grid[pos] += 1
houses = len(grid.points)
print_ans('3a', houses)

grid2 = Grid2D(default=0)
pos = [grid2.convert((0, 0)), grid2.convert((0, 0))]
grid2[pos[0]] = 2
for i, move in enumerate(data):
    pos[i % 2] = {
    '^': pos[i % 2] + grid2.north,
    'v': pos[i % 2] + grid2.south,
    '>': pos[i % 2] + grid2.east,
    '<': pos[i % 2] + grid2.west
    }.get(move)
    grid2[pos[i % 2]] += 1
houses = len(grid2.points)
print_ans('3b', houses)
# < 4403