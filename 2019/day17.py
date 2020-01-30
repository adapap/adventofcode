"""Day 17: Set and Forget"""
from aoctools import *
from intcode import Intcode

data = Data.fetch(day=17, year=2019)
grid = Grid2D(default='.')
prog = Intcode.from_csv(data)
prog.execute()
out = prog.get_output(all_output=True)
def update_grid(out):
    x, y = 0, 0
    for c in map(chr, out):
        if c == '\n':
            y += 1
            x = 0
            continue
        grid[x, y] = c
        x += 1
update_grid(out)
# grid.render()
robot = None
face = 0
alignment_sum = 0
for x in grid.points.copy():
    if grid[x] == '#' and all(grid[x + y] == '#' for y in grid.cardinal):
        alignment_sum += int(prod(grid.revert(x)))
    elif grid[x] == '^':
        robot = x
print_ans('17a', alignment_sum)
# Part 2
path = ''
while True:
    if grid[robot + grid.cardinal[face]] == '#':
        if path and not path[-1].isdigit():
            path += '1'
        elif path:
            path = path[:-1] + str(int(path[-1]) + 1)
        robot += grid.cardinal[face]
    elif grid[robot + grid.cardinal[(face - 1) % 4]] == '#':
        face = (face - 1) % 4
        path += ',R,'
    elif grid[robot + grid.cardinal[(face + 1) % 4]] == '#':
        face = (face + 1) % 4
        path += ',L,'
    else:
        break
path = path.strip(',')
# print(path)
prog = Intcode.from_csv(data)
prog.memory[0] = 2
# Split path into 3 repeating substrings
main = 'A,C,A,C,B,A,B,A,B,C\n'
fun_a = 'R,12,L,8,L,4,L,4\n'
fun_b = 'L,8,L,4,R,12,L,6,L,4\n'
fun_c = 'L,8,R,6,L,6\n'
continuous = 'n\n'
for instruction in [main, fun_a, fun_b, fun_c, continuous]:
    steps = list(map(ord, instruction))
    prog.execute(*steps)
out = prog.get_output(all_output=True)
print_ans('17b', out[-1])