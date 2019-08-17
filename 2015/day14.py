"""Day 14: Reindeer Olympics"""
from aoctools import *
import re

data = Data.fetch_by_line(day=14, year=2015)
time = 2503
# data = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.""".split('\n')

def distance(rate, duration, rest, time):
    cycle_length = duration + rest
    cycles = time // cycle_length
    partial = time % cycle_length
    dist = rate * duration
    return dist * cycles + min(partial * rate, dist)

best = -float('inf')
for line in data:
    params = re.findall(r'\d+', line)
    dist = distance(*map(int, params), time)
    if dist > best:
        best = dist
print_ans('14a', best)

class Reindeer:
    def __init__(self, rate, duration, rest):
        self.rate = rate
        self.duration = duration
        self.rest = rest
        self.distance = 0
        self.points = 0
    
    def tick(self, time):
        self.distance = distance(self.rate, self.duration, self.rest, time)
    
    def __lt__(self, other):
        return self.distance <= other.distance
    
    def __eq__(self, other):
        return self.distance == other.distance
    
racers = []
for line in data:
    params = re.findall(r'\d+', line)
    racers.append(Reindeer(*map(int, params)))
for t in range(1, time + 1):
    for racer in racers:
        racer.tick(t)
    leaders = filter(lambda y: y.distance == max(racers, key=lambda x: x.distance).distance, racers)
    for leader in leaders:
        leader.points += 1
top_points = max(racers, key=lambda x: x.points).points
print_ans('14b', top_points)