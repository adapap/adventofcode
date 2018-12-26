from collections import defaultdict
class Assembunny():
    def __init__(self, *reg_inits):
        self.registers = defaultdict(int)
        for reg in reg_inits:
            self.registers[reg[0]] = reg[1]
    
    def xval(self, x):
        try:
            x = int(x)
        except:
            x = self.registers[x]
        return x

    def cpy(self, x, y):
        self.registers[y] = self.xval(x)

    def inc(self, x):
        self.registers[x] += 1

    def dec(self, x):
        self.registers[x] -= 1

    def jnz(self, x, y):
        return int(y) - 1 if self.xval(x) != 0 else 0
asm1 = Assembunny()
asm2 = Assembunny(('c',1))

def solve(asm, part):
    with open('inp.txt') as f:
        inp = f.readlines()
    
    i = 0
    while i < len(inp):
        cmds = inp[i].strip().split(' ')
        if cmds[0] == 'cpy':
            asm.cpy(cmds[1], cmds[2])
        elif cmds[0] == 'inc':
            asm.inc(cmds[1])
        elif cmds[0] == 'dec':
            asm.dec(cmds[1])
        elif cmds[0] == 'jnz':
            i += asm.jnz(cmds[1], cmds[2])
        i += 1
    print(f'Day 12{part}: {asm.registers["a"]}')
solve(asm1, 'a')
solve(asm2, 'b')