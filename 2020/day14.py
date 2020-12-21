import aoc
import re
from collections import defaultdict

puzzle = aoc.Puzzle(day=14, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch_by_line()
memory = defaultdict(int)
memory2 = defaultdict(int)
mask = ''
for line in data:
    if line.startswith('mask'):
        mask = line.lstrip('mask = ')
    else:
        addr, value = re.findall(r'\d+', line)
        b = list(bin(int(value))[2:].zfill(36))
        a = list(bin(int(addr))[2:].zfill(36))
        addresses = [a]
        for i, x in enumerate(mask):
            if x == '1':
                for j in range(len(addresses)):
                    addresses[j][i] = '1'
            if x == 'X':
                for j in range(len(addresses)):
                    c = addresses[j].copy()
                    addresses[j][i] = '0'
                    c[i] = '1'
                    addresses.append(c)
        for a in addresses:
            n = int(''.join(a), 2)
            memory2[n] = int(value)
        for i, x in enumerate(mask):
            if x != 'X':
                b[i] = x
        memory[addr] = int(''.join(b), 2)
PART_1 = sum(x for x in memory.values())
# puzzle.submit(part=1, answer=PART_1)
PART_2 = sum(x for x in memory2.values())
puzzle.submit(part=2, answer=PART_2)
