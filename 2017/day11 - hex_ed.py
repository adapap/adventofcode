with open('input.txt') as f:
    data = f.read()

class Point:
    def __init__(self, *coords):
        self.coords = coords
        self.x, self.y, self.z = coords

    def __add__(self, other):
        return Point(*tuple(a + b for a, b in zip(self.coords, other.coords)))

    def __repr__(self):
        return f'<Point: {self.coords}>'

class HexCoords:
    nw = Point(-1, 1, 0)
    n = Point(0, 1, -1)
    ne = Point(1, 0, -1)
    se = Point(1, -1, 0)
    s = Point(0, -1, 1)
    sw = Point(-1, 0, 1)

class HexGrid:
    def __init__(self):
        self.pos = Point(0, 0, 0)
        self.max_distance = 0

    def move(self, direction):
        self.pos += getattr(HexCoords, direction)
        dist = self.distance
        if dist > self.max_distance:
            self.max_distance = dist

    @property
    def distance(self):
        dist = max(abs(p) for p in self.pos.coords)
        return int(dist)

grid = HexGrid()
moves = data.split(',')
for move in moves:
    grid.move(move)
print(f'Day 11a: {grid.distance}')
print(f'Day 11b: {grid.max_distance}')