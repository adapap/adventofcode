"""Day 23: Experimental Emergency Teleporation"""
# Part 2 was adapted from a solution on the AoC subreddit

from aoctools import Data, print_ans

import itertools
import re

data = Data.fetch_by_line(day=23, year=2018)
# data = """pos=<0,0,0>, r=4
# pos=<1,0,0>, r=1
# pos=<4,0,0>, r=3
# pos=<0,2,0>, r=1
# pos=<0,5,0>, r=3
# pos=<0,0,3>, r=1
# pos=<1,1,1>, r=1
# pos=<1,1,2>, r=1
# pos=<1,3,1>, r=1""".split('\n')
# data = """pos=<10,12,12>, r=2
# pos=<12,14,12>, r=2
# pos=<16,12,12>, r=4
# pos=<14,14,14>, r=6
# pos=<50,50,50>, r=200
# pos=<10,10,10>, r=5""".split('\n')

class Nanobot:
    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

    def in_range(self, other):
        return sum(map(abs, [self.x - other.x, self.y - other.y, self.z - other.z])) <= self.r

    @staticmethod
    def convert(point):
        axes = [
            [ 1,  1,  1],
            [-1,  1,  1],
            [ 1, -1,  1],
            [-1, -1,  1],
        ]
        return [sum(p * a for p, a in zip(point, axis)) for axis in axes]

    @staticmethod
    def distance(box):
        dist = 0
        for n, x in zip(box.min, box.max):
            if (n < 0) != (x < 0):
                continue
            d = min(abs(n), abs(x))
            if d > dist:
                dist = d
        return dist

    @property
    def box(self):
        center = self.center
        r = self.r
        return Cuboid(self.convert(center[:-1] + [center[-1] - r]),
                      self.convert(center[:-1] + [center[-1] + r]))

    @property
    def center(self):
        return [self.x, self.y, self.z]


class Cuboid:
    def __init__(self, min_, max_):
        self.min = min_
        self.max = max_

    def __and__(self, other):
        new_min = [max(n1, n2) for n1, n2 in zip(self.min, other.min)]
        new_max = [min(n1, n2) for n1, n2 in zip(self.max, other.max)]
        return Cuboid(new_min, new_max)

    def __bool__(self):
        return all(x >= n for n, x in zip(self.min, self.max))

nanobots = []
for line in data:
    bot = Nanobot(*map(int, re.match(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)', line).groups()))
    nanobots.append(bot)
strongest = max(nanobots, key=lambda x: x.r)
num = sum(map(strongest.in_range, nanobots))
print_ans('23a', num)

# Part 2
boxes = [b.box for b in nanobots]
intersecting = []
for box in boxes:
    count = 0
    for box_2 in boxes:
        if box & box_2:
            count += 1
    intersecting.append(count)

for n, count in enumerate(sorted(intersecting, reverse=True)):
    if n + 1 >= count:
        break

distance = None
for n in range(count, 0, -1):
    possible_indexes = [i for i, count in enumerate(intersecting) if count >= n]
    for indexes in itertools.combinations(possible_indexes, n):
        box = boxes[indexes[0]]
        for index in indexes[1:]:
            box &= boxes[index]
            if not box:
                break
        else:
            dist = Nanobot.distance(box)
            if distance is None or dist < distance:
                distance = dist
    if distance:
        break
print_ans('23b', distance)