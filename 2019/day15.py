"""Day 15: Oxygen Systems"""
from aoctools import *
from intcode import Intcode

data = Data.fetch(day=15, year=2019)
prog = Intcode.from_csv(data)
grid = Grid2D(default=' ')
moves = {
    1: grid.north,
    2: grid.south,
    3: grid.west,
    4: grid.east,
}
backtrack = []
pos = 0j
goal = None
steps = float('inf')
while True:
    for inp, move in moves.items():
        new_pos = pos + move
        if new_pos not in grid:
            prog.execute(inp)
            grid[new_pos] = ['#', '.', '*'][prog.get_output()]
            if grid[new_pos] in '.*':
                pos = new_pos
                backtrack.append({1: 2, 2: 1, 3: 4, 4: 3}[inp])
            if grid[pos] == '*':
                goal = pos
                steps = min(len(backtrack), steps)
            break
    else:
        if len(backtrack) < 1:
            break
        inp = backtrack.pop()
        pos += moves[inp]
        prog.execute(inp)
        _ = prog.get_output()
print_ans('15a', steps)
# grid.render()
def flood_fill(pos, t):
    grid[pos] = 'O'
    time = t
    for move in moves.values():
        new_pos = pos + move
        if grid[new_pos] != '.':
            continue
        time = flood_fill(pos + move, t + 1)
        t = max(time, t)
    return t
time = flood_fill(goal, 0)
print_ans('15b', time)