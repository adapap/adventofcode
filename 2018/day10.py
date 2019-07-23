"""Day 10: The Stars Align"""
from aoctools import Data, Vector, print_ans

import re

data = """position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>""".strip().split('\n')
data = Data.fetch_by_line(day=10, year=2018)

class Point:
    def __init__(self, pos, vel):
        self.position = pos
        self.velocity = vel
    def step(self):
        self.position += self.velocity
    def unstep(self):
        self.position -= self.velocity
    @property
    def x(self):
        return self.position.x
    @property
    def y(self):
        return self.position.y
    
    

points = []
for line in data:
    p1, p2, v1, v2 = re.match(r'position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>', line).groups()
    pos = Vector(int(p1), int(p2))
    vel = Vector(int(v1), int(v2))
    point = Point(pos, vel)
    points.append(point)

last_diff = float('inf')
time = 1
while True:
    max_y = max(points, key=lambda p: p.y).y
    min_y = min(points, key=lambda p: p.y).y
    diff = abs(max_y - min_y)
    if diff > last_diff:
        for p in points:
            p.unstep()
        break
    time += 1
    last_diff = diff
    for point in points:
        point.step()

min_x = min(points, key=lambda p: p.x).x
max_x = max(points, key=lambda p: p.x).x
min_y = min(points, key=lambda p: p.y).y
max_y = max(points, key=lambda p: p.y).y

print('Day 10a:')
for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        if any(p.x == x and p.y == y for p in points):
            print('#', end='')
        else:
            print('.', end='')
    print()
print_ans('10b', time - 1)