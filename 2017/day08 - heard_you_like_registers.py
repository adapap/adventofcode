from collections import defaultdict
with open('input.txt') as f:
    data = f.readlines()

registers = defaultdict(int)
highest = -float('inf')
for line in data:
    cmds = line.strip().split(' ')
    reg1 = cmds[0]
    change = cmds[1]
    amt = int(cmds[2])
    cmds[-3] = f'registers["{cmds[-3]}"]'
    cond = eval(''.join(cmds[-3:]))
    if cond:
        registers[reg1] += amt if change == 'inc' else -amt
        if registers[reg1] > highest:
            highest = registers[reg1]
max_reg = max(registers.values())
print(f'Day 8a: {max_reg}')
print(f'Day 8b: {highest}')