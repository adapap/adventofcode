from collections import defaultdict

class Face:
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)
    moves = [NORTH, EAST, SOUTH, WEST]

class Grid:
    transform = {
    '.': '#',
    '#': '.'
    }

    def __init__(self, data, b=False):
        self.points = defaultdict(lambda: '.')
        for y, row in enumerate(data):
            for x, char in enumerate(row.strip()):
                self.points[(x, y)] = char
        self.face_index = 0
        size = (len(data[0]) - 1) // 2
        self.pos = (size, size)
        self.infections = 0
        if b:
            Grid.transform = {
            '.': 'W',
            'W': '#',
            '#': 'F',
            'F': '.'
            }

    @property
    def face(self):
        return Face.moves[self.face_index]

    def turn(self, cw=True):
        self.face_index += 1 if cw else -1
        self.face_index %= 4

    def step(self):
        self.pos = tuple(x + y for x, y in zip(self.pos, self.face))

    def tick(self):
        node = self.points[self.pos]
        if node == '.':
            self.turn(cw=False)
        elif node == '#':
            self.turn(cw=True)
        elif node == 'F':
            self.turn(cw=True)
            self.turn(cw=True)
        self.points[self.pos] = Grid.transform[node]
        if Grid.transform[node] == '#':
            self.infections += 1
        self.step()

with open('input.txt') as f:
    data = f.readlines()

grid = Grid(data=data)
bursts = 10000
for _ in range(bursts):
    grid.tick()
print(f'Day 22a: {grid.infections}')

grid = Grid(data=data, b=True)
bursts = 10000000
for _ in range(bursts):
    grid.tick()
print(f'Day 22a: {grid.infections}')