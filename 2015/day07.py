"""Day 7: Some Assembly Required"""
from aoctools import *
from collections import deque

data = Data.fetch_by_line(day=7, year=2015)
PART_B = True
class Op:
    NOT = lambda a: ~a
    OR = lambda a, b: a | b
    AND = lambda a, b: a & b
    LSHIFT = lambda a, b: a << b
    RSHIFT = lambda a, b: a >> b
wires = {}
if PART_B:
    wires['b'] = 3176
def wire(x):
    if x in wires:
        return wires.get(x)
    elif x.isdigit():
        return int(x)

lines = deque(data)
while len(lines) > 0:
    args = lines[0].split()
    reg = args[-1]
    if len(args) == 3 and wire(args[0]) != None:
        wires[reg] = wire(args[0])
    elif len(args) == 4 and wire(args[1]) != None:
        wires[reg] = getattr(Op, args[0])(wire(args[1]))
    elif len(args) == 5 and wire(args[0]) != None and wire(args[2]) != None:
        wires[reg] = getattr(Op, args[1])(wire(args[0]), wire(args[2]))
    else:
        lines.rotate()
        continue
    lines.popleft()
part = '7b' if PART_B else PART_A
print_ans(part, wires.get('a'))