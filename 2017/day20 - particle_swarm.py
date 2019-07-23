from itertools import count
uid = count()

class Vector:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    @property
    def coords(self):
        return (self.x, self.y, self.z)

    def __add__(self, other):
        return Vector(*tuple(a + b for a, b in zip(self.coords, other.coords)))
    
    def __eq__(self, other):
        return self.coords == other.coords

    def __repr__(self):
        return f'<{self.x}, {self.y}, {self.z}>'

class Particle:
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a
        self.id = next(uid)

    def tick(self):
        self.v += self.a
        self.p += self.v

    @property
    def center_distance(self):
        return sum(abs(x) for x in self.p.coords)
    

    @classmethod
    def from_str(cls, s):
        params = []
        for x in s.split(', '):
            params.append(Vector(*x[3:-1].split(',')))
        return cls(*params)

    def __eq__(self, other):
        return self.p == other.p

    def __repr__(self):
        return f'<{self.id}: P:{self.p}> V:{self.v} A:{self.a}>'

with open('input.txt') as f:
    data = f.readlines()
particles = []
for line in data:
    particles.append(Particle.from_str(line.strip()))

SIMULATE = 1000
# Part A
for _ in range(SIMULATE):
    for p in particles:
        p.tick()
closest_particle = min(particles, key=lambda p: p.center_distance)
print(f'Day 20a: {closest_particle.id}')

# Part B
particles = []
for line in data:
    particles.append(Particle.from_str(line.strip()))
for _ in range(SIMULATE):
    positions = [p.p.coords for p in particles]
    particles = [p for p in particles if positions.count(p.p.coords) == 1]
    for p in particles:
        p.tick()
print(f'Day 20b: {len(particles)}')