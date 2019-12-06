"""Day 5: Sunny with a Chance of Asteroids"""
from aoctools import *

data = Data.fetch(day=5, year=2019)
# data = '1002,4,3,4,33'
# data = '3,0,4,0,99'
# data = '3,9,8,9,10,9,4,9,99,-1,8' # Compare input to 8
# data = '3,9,7,9,10,9,4,9,99,-1,8'
# data = '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9' # Jump test position mode
# data = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'
class Op:
    ADD = 1
    MUL = 2
    INP = 3
    OUT = 4
    JNZ = 5
    JEZ = 6
    JLT = 7
    JEQ = 8
    STP = 99
values = list(map(int, data.split(',')))
def evaluate(values, inputs):
    pos = 0
    while True:
        ins = str(values[pos]).zfill(5)
        a, b, c, op = map(int, (*ins[:3], ins[-2:]))
        if op == Op.ADD:
            x, y, z = values[pos + 1:pos + 4]
            values[z] = (x if c else values[x]) + (y if b else values[y])
            pos += 4
        elif op == Op.MUL:
            x, y, z = values[pos + 1:pos + 4]
            values[z] = (x if c else values[x]) * (y if b else values[y])
            pos += 4
        elif op == Op.INP:
            n = next(inputs)
            x = values[pos + 1]
            values[x] = n
            pos += 2
        elif op == Op.OUT:
            x = values[pos + 1]
            out = x if c else values[x]
            if out:
                return out
            pos += 2
        elif op == Op.JNZ:
            x, y = values[pos + 1:pos + 3]
            if (x if c else values[x]) != 0:
                pos = y if b else values[y]
            else:
                pos += 3
        elif op == Op.JEZ:
            x, y = values[pos + 1:pos + 3]
            if (x if c else values[x]) == 0:
                pos = y if b else values[y]
            else:
                pos += 3
        elif op == Op.JLT:
            x, y, z = values[pos + 1:pos + 4]
            if (x if c else values[x]) < (y if b else values[y]):
                values[z] = 1
            else:
                values[z] = 0
            pos += 4
        elif op == Op.JEQ:
            x, y, z = values[pos + 1:pos + 4]
            if (x if c else values[x]) == (y if b else values[y]):
                values[z] = 1
            else:
                values[z] = 0
            pos += 4
        elif op == Op.STP:
            break
        else:
            raise ValueError('No-op:', op)
    return 0
a = evaluate(values[:], iter([1]))
print_ans('5a', a)
b = evaluate(values[:], iter([5]))
print_ans('5b', b)