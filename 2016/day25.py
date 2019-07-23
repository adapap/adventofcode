import re, sys
bin_const = 2730
with open('inp.txt') as f:
    nums = []
    for line in f.readlines()[1:3]:
        nums.append(int(re.findall(r'\d+', line)[0]))
    print(nums)
    print(f'Day 25a: {bin_const - (nums[0] * nums[1])}')
    sys.exit(0)

from collections import defaultdict

goal_str = '01' * 10
class Assembunny:
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

    def inc(self, x):
        self.registers[x] += 1

    def dec(self, x):
        self.registers[x] -= 1

    def add(self, x, y):
        self.registers[x] += self.val(y)

    def mul(self, x, y):
        self.registers[x] *= self.val(y)

    def out(self, reg):
        print(self.registers[reg], end='')

    def jnz(self, x, y):
        return int(y) - 1 if self.val(x) != 0 else 0

def solve():
    with open('inp.txt') as f:
        inp = f.readlines()

    a_reg = 0
    while a_reg < 500:
        asm = Assembunny(['a', a_reg])
        out_str = ''
        i = 0
        while i < len(inp) and len(out_str) < 30:
            cmds = inp[i].strip().split(' ')
            if cmds[0] == 'cpy':
                asm.cpy(cmds[1], cmds[2])
            elif cmds[0] == 'inc':
                asm.inc(cmds[1])
            elif cmds[0] == 'dec':
                asm.dec(cmds[1])
            elif cmds[0] == 'jnz':
                i += asm.jnz(cmds[1], cmds[2])
            elif cmds[0] == 'add':
                asm.add(cmds[1], cmds[2])
            elif cmds[0] == 'mul':
                asm.mul(cmds[1], cmds[2])
            elif cmds[0] == 'out':
                # asm.out(cmds[1])
                out_str += str(asm.registers['b'])
            elif cmds[0] == 'nop':
                i += 1
                continue
            i += 1
        if goal_str in out_str:
            print('Day 25a:', a_reg)
            break
        a_reg += 1

solve()