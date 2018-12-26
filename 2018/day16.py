"""Day 16: Chronal Classification"""
from aoctools import Data, print_ans
import elfcode
from elfcode import *

import re
from collections import defaultdict
data = Data.fetch_by_line(day=16, year=2018)
divider = [(i, i+3) for i in range(len(data)) if data[i:i+3] == ['', '', '']][0]
opcode_tests = '\n'.join(data[:divider[0]])
sample_prog = data[divider[1]:]

elfcode.registers = defaultdict(int)

OPCODES = (addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr)
class Opcodes:
    def __init__(self):
        self.codes = {i: OPCODES for i in range(16)}

    def __getitem__(self, code):
        return self.codes.get(code, None)

    def __setitem__(self, code, value):
        self.codes[code] = value

    def __repr__(self):
        result = ''
        for key in self.codes:
            if type(self.codes[key]) == list:
                result += f'{key}: {[f.__name__ for f in self.codes[key]]}\n'
            else:
                result += f'{key}: {self.codes[key].__name__}\n'
        return result

opcodes = Opcodes()

total = 0
for test in opcode_tests.split('\n\n'):
    original, instruction, result = test.split('\n')
    elfcode.registers = defaultdict(int)
    registers = elfcode.registers
    for i, r in enumerate(re.findall(r'\d+', original)):
        registers[i] = int(r)
    opcode, a, b, c = [int(x) for x in re.findall(r'\d+', instruction)]
    new_registers = defaultdict(int)
    for i, r in enumerate(re.findall(r'\d+', result)):
        new_registers[i] = int(r)

    valid = []
    for OP in OPCODES:
        if new_registers[c] == OP(a, b):
            valid.append(OP)
    if valid:
        opcodes[opcode] = [o for o in valid if o in opcodes[opcode]]
    if len(valid) >= 3:
        total += 1
print_ans('16a', total)

complete = []

while any(type(x) == list for x in opcodes.codes.values()):
    for op, values in opcodes.codes.items():
        if type(values) == list and len(values) == 1:
            complete.append(values[0])
            opcodes[op] = values[0]
        elif type(values) == list:
            opcodes[op] = [o for o in values if o not in complete]

elfcode.registers = defaultdict(int)
registers = elfcode.registers
for line in sample_prog:
    op, a, b, c = [int(x) for x in re.findall(r'\d+', line)]
    registers[c] = opcodes[op](a, b)
print_ans('16b', registers[0])