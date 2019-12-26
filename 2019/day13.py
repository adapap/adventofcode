"""Day 13: Care Package"""
from aoctools import *
from intcode import Intcode

data = Data.fetch(day=13, year=2019)
prog = Intcode.from_csv(data)
prog.evaluate()
grid = Grid2D()
while (chunk := prog.get_output(n=3)) != []:
    x, y, tile = chunk
    grid[x, y] = tile
blocks = sum(1 for x in grid.points.values() if x == 2)
print_ans('13a', blocks)
prog = Intcode.from_csv(data)
prog.memory[0] = 2
score = 0
ball = 0
paddle = 0
steps = 0
while not prog.halted:
    prog.evaluate()
    steps += 1
    while (chunk := prog.get_output(n=3)) != []:
        x, y, tile = chunk
        if (x, y) == (-1, 0):
            score = tile
        else:
            if tile == 4:
                ball = x
            elif tile == 3:
                paddle = x
            grid[x, y] = tile
    prog.add_inputs(cmp(ball, paddle))
print_ans('13b', score)