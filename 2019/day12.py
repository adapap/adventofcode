"""Day 12: The N-Body Problem"""
from aoctools import *
from functools import reduce
from itertools import permutations
import copy
import math
import re

data = Data.fetch_by_line(day=12, year=2019)
# data = """<x=-1, y=0, z=2>
# <x=2, y=-10, z=-7>
# <x=4, y=-8, z=8>
# <x=3, y=5, z=-1>""".split('\n')

# data = """<x=-8, y=-10, z=0>
# <x=5, y=5, z=10>
# <x=2, y=-7, z=3>
# <x=9, y=-8, z=-3>""".split('\n')
moons = []
class Moon:
    def __init__(self, pos):
        self.pos = pos
        self.vel = Vector(0, 0, 0)
    
    @property
    def energy(self):
        return sum(map(abs, self.pos.sequence)) * sum(map(abs, self.vel.sequence))
    
    def update_velocity(self, other):
        a, b = self.pos, other.pos
        self.vel += Vector(
            cmp(b.x, a.x),
            cmp(b.y, a.y),
            cmp(b.z, a.z)
        )
    
    def update_position(self):
        self.pos += self.vel
    
    def __repr__(self):
        return repr(self.pos)

def simulate(moons):
    for a, b in permutations(moons, 2):
        a.update_velocity(b)
    for a in moons:
        a.update_position()

for line in data:
    match = re.match('<x=(-?\d+), y=(-?\d+), z=(-?\d+)>', line)
    moon = Moon(Vector(*map(int, match.groups())))
    moons.append(moon)
time = 0
steps = 1000
state = copy.deepcopy(moons)
for _ in range(steps):
    simulate(moons)
energy = sum(m.energy for m in moons)
print_ans('12a', energy)
moons = copy.deepcopy(state)
cycles = [0, 0, 0]
orig = [(), (), ()]
for i in range(len(state)):
    orig[0] += (state[i].pos.x, state[i].vel.x,)
    orig[1] += (state[i].pos.y, state[i].vel.y,)
    orig[2] += (state[i].pos.z, state[i].vel.z,)
time = 0
while 0 in cycles:
    simulate(moons)
    time += 1
    curr = [(), (), ()]
    for i in range(len(moons)):
        curr[0] += (moons[i].pos.x, moons[i].vel.x,)
        curr[1] += (moons[i].pos.y, moons[i].vel.y,)
        curr[2] += (moons[i].pos.z, moons[i].vel.z,)
    for i in range(3):
        if cycles[i] == 0 and curr[i] == orig[i]:
            cycles[i] = time
    
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)
period = reduce(lcm, cycles)
print_ans('12b', period)