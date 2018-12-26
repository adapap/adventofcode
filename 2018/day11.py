"""Day 11: Chronal Charge"""
from aoctools import Data, Grid, print_ans

from collections import defaultdict

grid = Grid(bounds={'x': (1, 300), 'y': (1, 300)})

data = Data.fetch(day=11, year=2018)
# data = '42'
serial = int(data)

class Cell:
    """Fuel cell in grid with power calculation."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def power(self):
        """Calculate cell power."""
        rack_id = self.x + 10
        power = rack_id * self.y
        power += serial
        power *= rack_id
        power = (power // 100) % 10
        power -= 5
        return power

    def __repr__(self):
        return f'<{self.x}, {self.y}: {self.power}>'

powers = defaultdict(int)

for x in range(1, 301):
    for y in range(1, 301):
        cell = Cell(x, y)
        grid[x, y] = cell
        powers[x, y] = cell.power

best_power = -float('inf')
coord = None
for x in range(2, 300):
    for y in range(2, 300):
        total_power = None
        for i in range(-1, 2):
            for j in range(-1, 2):
                if total_power is None:
                    total_power = powers[x + i, y + j]
                else:
                    total_power += powers[x + i, y + j]
        if total_power > best_power:
            coord = ','.join([str(p) for p in (x - 1, y - 1)])
            best_power = total_power
print_ans('11a', coord)

def region_power(x0, y0, size):
    total = None
    for x in range(x0, x0 + size):
        for y in range(y0, y0 + size):
            if total is None:
                total = powers[x, y]
            else:
                total += powers[x, y]
    return total

best_power = region_power(1, 1, 300)
best_size = 0
ans = ''

size = 1
tries = 2
while tries:
    run = False
    for x in range(1, 301):
        for y in range(1, 301):
            p = region_power(x, y, size)
            if p >= best_power:
                run = True
                best_power = p
                best_size = size
                ans = f'{x},{y},{size}'
    size += 1
    if not run:
        tries -= 1
print_ans('11b', ans)