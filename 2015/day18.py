"""Day 18: Like a GIF For Your Yard"""
from aoctools import *

data = Data.fetch_by_line(day=18, year=2015)
# data = """##.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####.#""".split('\n')
steps = 100
def print_grid(grid):
    for y in range(grid.min_y, grid.max_y + 1):
        for x in range(grid.min_x, grid.max_x + 1):
            print(grid[grid.convert((x, y))], end='')
        print()
    print()
grid = Grid2D(default='.')
for row, col, char in Data.double_enum(data):
    grid[col, row] = char
orig = grid.points.copy()
for _ in range(steps):
    new_grid = Grid2D(default='.')
    for point in grid.points.copy():
        state = grid[point]
        neighbors = sum(grid[x + point] == '#' for x in Grid2D.intercardinal)
        if state == '#' and neighbors in (2, 3):
            new_grid[point] = '#'
        elif state == '.' and neighbors == 3:
            new_grid[point] = '#'
        else:
            new_grid[point] = '.'
    grid = new_grid
lights = sum(grid[x] == '#' for x in grid.points)
print_ans('18a', lights)
grid.points = orig
for _ in range(steps):
    new_grid = Grid2D(default='.')
    for point in grid.points.copy():
        if grid.revert(point) in map(lambda x: (max(x[0], 0), x[1]), grid.corners):
            new_grid[point] = '#'
        else:
            state = grid[point]
            neighbors = sum(grid[x + point] == '#' for x in Grid2D.intercardinal)
            if state == '#' and neighbors in (2, 3):
                new_grid[point] = '#'
            elif state == '.' and neighbors == 3:
                new_grid[point] = '#'
            else:
                new_grid[point] = '.'
    grid = new_grid
lights = sum(grid[x] == '#' for x in grid.points)
print_ans('18b', lights)
# x < 934