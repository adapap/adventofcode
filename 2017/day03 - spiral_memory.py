import math

with open('input.txt') as f:
    start = int(f.read())

def manhattan(n):
    if n == 1:
        return 1
    ring = 1
    while ring ** 2 < n:
        ring += 2
    outer_ring = n - (ring - 2) ** 2
    offset = outer_ring % (ring - 1)
    dist = abs((offset) - (ring // 2))
    ans = (ring - 1) // 2 + dist
    print(f'Day 3a: {ans}')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y,))

    def __repr__(self):
        return f'<x: {self.x}, y: {self.y}>'

class Grid:
    def __init__(self):
        self.graph = {}
        self.pos = Point(0, 0)
        self.max = Point(0, 0)
        self.min = Point(0, 0)
        self.dir = 3
        self.graph[Point(0, 0)] = 1

    def move(self):
        # East
        if self.dir == 3:
            self.pos.x += 1
            if self.pos.x > self.max.x:
                self.max.x = self.pos.x
                self.dir = 0
        # North
        elif self.dir == 0:
            self.pos.y -= 1
            if self.pos.y < self.min.y:
                self.min.y = self.pos.y
                self.dir = 1
        # West
        elif self.dir == 1:
            self.pos.x -= 1
            if self.pos.x < self.min.x:
                self.min.x = self.pos.x
                self.dir = 2
        # South
        elif self.dir == 2:
            self.pos.y += 1
            if self.pos.y > self.max.y:
                self.max.y = self.pos.y
                self.dir = 3

    def calc_point(self):
        value = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x != 0 or y != 0:
                    value += self.graph.get(Point(self.pos.x + x, self.pos.y + y), 0)
        self.graph[Point(self.pos.x, self.pos.y)] = value

    def loop(self, inp: int):
        while self.graph.get(Point(self.pos.x, self.pos.y), 0) < inp:
            self.move()
            self.calc_point()
            value = self.graph.get(Point(self.pos.x, self.pos.y), 0)
        print(f'Day 3b: {value}')

manhattan(start)

grid = Grid()
grid.loop(start)