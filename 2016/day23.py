from collections import defaultdict
import math
import sys

part_a = 7
part_b = 12
const = (94 * 82)

print('Day 23a:', math.factorial(part_a) + const)
print('Day 23b:', math.factorial(part_b) + const)

sys.exit(0)

def is_number(s):
    try:
        val = int(s)
        return True
    except:
        return False
class Assembunny():
    def __init__(self, *reg_inits):
        self.registers = defaultdict(int)
        for reg in reg_inits:
            self.registers[reg[0]] = reg[1]
    
    def val(self, x):
        try:
            x = int(x)
        except:
            x = self.registers[x]
        return x

    def cpy(self, x, y):
        self.registers[y] = self.val(x)

    def add(self, x, y):
        self.registers[x] += self.val(y)

    def mul(self, x, y):
        self.registers[x] *= self.val(y)

    def inc(self, x):
        self.registers[x] += 1

    def dec(self, x):
        self.registers[x] -= 1

    def jnz(self, x, y):
        return self.val(y) - 1 if self.val(x) != 0 else 0

    def tgl(self, x, i, inp):
        if i + self.val(x) >= len(inp):
            return
        next_cmds = inp[i + self.val(x)].strip().split(' ')
        if next_cmds[0] == 'inc':
            next_cmds[0] = 'dec'
        elif next_cmds[0] == 'dec' or next_cmds[0] == 'tgl':
            if is_number(next_cmds[1]):
                next_cmds = ['jnz','0','0']
            else:
                next_cmds[0] = 'inc'
        elif next_cmds[0] == 'jnz':
            if is_number(next_cmds[2]):
                next_cmds[0] = 'cpy'
            else:
                next_cmds[1] = '0'
        elif next_cmds[0] == 'cpy':
            next_cmds[0] = 'jnz'
        inp[i + self.val(x)] = ' '.join(next_cmds)
asm1 = Assembunny(('a',7))

def solve(asm, part):
    with open('inp.txt') as f:
        inp = f.readlines()
    i = 0
    while 0 <= i < len(inp):
        cmds = inp[i].strip().split(' ')
        if cmds[0] == 'cpy':
            asm.cpy(cmds[1], cmds[2])
        elif cmds[0] == 'inc':
            asm.inc(cmds[1])
        elif cmds[0] == 'dec':
            asm.dec(cmds[1])
        elif cmds[0] == 'jnz':
            i += asm.jnz(cmds[1], cmds[2])
        elif cmds[0] == 'tgl':
            asm.tgl(cmds[1], i, inp)
        elif cmds[0] == 'add':
            asm.add(cmds[1], cmds[2])
        elif cmds[0] == 'mul':
            asm.mul(cmds[1], cmds[2])
        i += 1
    print(f'Day 23{part}: {asm.registers["a"]}')
solve(asm1, 'a')