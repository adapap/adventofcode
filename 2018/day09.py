"""Day 9: Marble Mania"""
from aoctools import Data, IntTuple, print_ans

import re
from collections import defaultdict, deque

data = Data.fetch(day=9, year=2018)
elves, marbles = IntTuple(*re.match(r'(\d+) players; last marble is worth (\d+) points', data).groups())

def game(num_elves, num_marbles):
    players = defaultdict(int)
    marbles = deque([0])
    multiple = 23
    rotation = 7
    for x in range(1, num_marbles + 1):
        if x % multiple == 0:
            marbles.rotate(rotation)
            players[x % num_elves] += x + marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(x)
    return max(players.values())

print_ans('9a', game(elves, marbles))
print_ans('9b', game(elves, marbles * 100))