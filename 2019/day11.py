"""Day 11: Space Police"""
from aoctools import *
from intcode import Intcode

data = Data.fetch(day=11, year=2019)
def paint(start=0):
    prog = Intcode.from_csv(data)
    grid = Grid2D(default=0)
    pos = 0j
    grid[pos] = start
    face = 0
    moves = grid.cardinal
    prog.add_inputs(grid[pos])
    prog.evaluate()
    while not prog.halted:
        color, turn = prog.get_output(n=2)
        grid[pos] = color
        face = (face + [1, -1][turn]) % 4
        pos += moves[face]
        prog.add_inputs(grid[pos])
        prog.evaluate()
    return grid
grid = paint(start=0)
colored = len(grid.points)
# print_ans('11a', colored)
grid = paint(start=1)
print_ans('11b', '')
grid.render(keys={0: ' ', 1: '#'})