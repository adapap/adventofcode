"""Day 19: Go With The Flow"""
from aoctools import Data, print_ans
import elfcode

import re
from collections import defaultdict

data = Data.fetch_by_line(day=19, year=2018)
# data = """#ip 0
# seti 5 0 1
# seti 6 0 2
# addi 0 1 0
# addr 1 2 3
# setr 1 0 0
# seti 8 0 4
# seti 9 0 5""".split('\n')

elfcode.registers = registers = {}
for i in range(6):
    registers[i] = 0
pointer = int(re.match(r'#ip (\d+)', data[0]).group(1))
commands = []
for line in data[1:]:
    cmd, a, b, c = re.match(r'(.+) (\d+) (\d+) (\d+)', line).groups()
    func = getattr(elfcode, cmd)
    commands.append([func, *map(int, (a, b, c))])

while 0 <= registers[pointer] < len(commands):
    f, a, b, c = commands[registers[pointer]]
    # print(f.__name__, a, b, c)
    registers[c] = f(a, b)
    registers[pointer] += 1
r0 = registers[0]
print_ans('19a', r0)

a = 0
b = 909 + 10550400 # Remove second number for part A
for d in range(1, b + 1):
    if b % d == 0:
        a += d
print_ans('19b', a)