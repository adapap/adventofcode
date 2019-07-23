class Art:
    def __init__(self, state, rules):
        self.rules = {}
        self.state = state
        for rule in rules.split('\n'):
            a, b = [x.split('/') for x in rule.split(' => ')]
            for r in range(4):
                x = self.rotate(a, r)
                for f in range(2):
                    x = self.flip(x, f)
                    self.rules['/'.join(x)] = '/'.join(b)

    @property
    def active_pixels(self):
        return self.state.count('#')

    def fractal(self):
        state = self.state.split('\n')
        size = len(state[0])
        new_state = []
        if size % 2 == 0:
            for y in range(0, size, 2):
                new_row = []
                for x in range(0, size, 2):
                    grid = '/'.join([state[i][x:x+2] for i in range(y, y+2)])
                    new_row.append(self.rules[grid].split('/'))
                unit = '\n'.join([''.join(x) for x in zip(*new_row)])
                new_state.append(unit)
            self.state = '\n'.join(new_state)
        elif size % 3 == 0:
            for y in range(0, size, 3):
                new_row = []
                for x in range(0, size, 3):
                    grid = '/'.join([state[i][x:x+3] for i in range(y, y+3)])
                    new_row.append(self.rules[grid].split('/'))
                unit = '\n'.join(''.join(x) for x in zip(*new_row))
                new_state.append(unit)
            self.state = '\n'.join(new_state)

    def rotate(self, matrix, n=1):
        new = matrix[:]
        for _ in range(n):
            new = list(''.join(x) for x in zip(*new[::-1]))
        return new

    def flip(self, matrix, axis=0):
        """Axis 0: vertical, 1: horizontal"""
        new = matrix[:]
        if axis == 0:
            return new[::-1]
        else:
            return [row[::-1] for row in new]

start = """.#.
..#
###"""

with open('input.txt') as f:
    rules = f.read()
art = Art(start, rules)
ITERATIONS = 5
for _ in range(ITERATIONS):
    art.fractal()
    # print(art.state, end='\n' * 2)
print(f'Day 21a: {art.active_pixels}')
ITERATIONS = 18 - ITERATIONS
for _ in range(ITERATIONS):
    art.fractal()
print(f'Day 21b: {art.active_pixels}')