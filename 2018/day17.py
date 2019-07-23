"""Day 17: Resevoir Research"""
from aoctools import Data, Grid, Geometry, print_ans

import re
import sys
sys.setrecursionlimit(3000)
data = Data.fetch_by_line(day=17, year=2018)
# data = """x=495, y=2..7
# y=7, x=495..501
# x=501, y=3..7
# x=498, y=2..4
# x=506, y=1..2
# x=498, y=10..13
# x=504, y=10..13
# y=13, x=498..504""".strip().split('\n')

grid = Grid(default='.')
grid[500, 0] = '|'
min_y = float('inf')
max_y = -min_y
min_x = min_y
max_x = max_y
for line in data:
    x = re.search(r'x=(\d+)(?:\.{2})?(\d*)', line).groups()
    y = re.search(r'y=(\d+)(?:\.{2})?(\d*)', line).groups()
    if x[1]:
        xvals = range(int(x[0]), int(x[1]) + 1)
    else:
        xvals = range(int(x[0]), int(x[0]) + 1)
    if y[1]:
        yvals = range(int(y[0]), int(y[1]) + 1)
    else:
        yvals = range(int(y[0]), int(y[0]) + 1)
    for y in yvals:
        for x in xvals:
            grid[x, y] = '#'
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x

def print_grid():
    for y in range(1, max_y + 1):
        for x in range(min_x - 5, max_x + 6):
            print(grid[x, y], end='')
        print()

def is_bounded(p):
    left = False
    right = False
    x, y = p
    while True:
        if grid[x, y + 1] not in '#~':
            break
        x -= 1
        if grid[x, y] == '.':
            break
        if grid[x, y] == '#':
            left = True
            break
    while True:
        if grid[x, y + 1] not in '#~':
            break
        x += 1
        if grid[x, y] == '.':
            break
        if grid[x, y] == '#':
            right = True
            break
    return left and right

def drop(point):
    x, y = point
    if y >= max_y:
        return
    if grid[point] == '|':
        if grid[x, y + 1] == '.':
            grid[x, y + 1] = '|'
            drop((x, y + 1))
        if is_bounded(point):
            fill(point)
    if grid[x, y + 1] in ['#', '~']:
        if grid[x - 1, y] == '.':
            grid[x - 1, y] = '|'
            global min_x, max_x
            if x - 1 < min_x:
                min_x -= 1
            drop((x - 1, y))
        if grid[x + 1, y] == '.':
            grid[x + 1, y] = '|'
            if x + 1 > max_x:
                max_x += 1
            drop((x + 1, y))

def fill(point):
    x, y = point
    grid[x, y] = '~'
    lx, rx = x, x
    while grid[lx, y] != '#':
        grid[lx, y] = '~'
        lx -= 1
    while grid[rx, y] != '#':
        grid[rx, y] = '~'
        rx += 1

start = (500, 0)
drop(start)
# print_grid()
still = 0
flowing = 0
for y in range(2, max_y):
    for x in range(min_x, max_x + 1):
        if grid[x, y] == '~':
            still += 1
        elif grid[x, y] == '|':
            flowing += 1
print_ans('17a', still + flowing)
print_ans('17b', still)