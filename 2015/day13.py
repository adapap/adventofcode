"""Day 13: Knights of the Dinner Table"""
from aoctools import *
from collections import defaultdict
import re

data = Data.fetch_by_line(day=13, year=2015)
# data = """Alice would gain 54 happiness units by sitting next to Bob.
# Alice would lose 79 happiness units by sitting next to Carol.
# Alice would lose 2 happiness units by sitting next to David.
# Bob would gain 83 happiness units by sitting next to Alice.
# Bob would lose 7 happiness units by sitting next to Carol.
# Bob would lose 63 happiness units by sitting next to David.
# Carol would lose 62 happiness units by sitting next to Alice.
# Carol would gain 60 happiness units by sitting next to Bob.
# Carol would gain 55 happiness units by sitting next to David.
# David would gain 46 happiness units by sitting next to Alice.
# David would lose 7 happiness units by sitting next to Bob.
# David would gain 41 happiness units by sitting next to Carol.""".split('\n')
def search(start, graph):
    pq = PriorityQueue()
    state = (start,)
    pq.put(state, 0)
    costs = {state: 0}
    
    while not pq.empty():
        state = pq.get()
        if all(k in state for k in graph):
            first = state[0]
            last = state[-1]
            yield costs[state] + graph[first][last] + graph[last][first]
        for guest in graph:
            if guest in state:
                continue
            new_state = state + (guest,)
            prev_delta = graph[state[-1]][guest]
            next_delta = graph[guest][state[-1]]
            new_cost = costs[state] + prev_delta + next_delta
            if new_state not in costs or new_cost > costs[new_state]:
                priority = -new_cost
                pq.put(new_state, priority)
                costs[new_state] = new_cost
graph = defaultdict(dict)
for line in data:
    a, mult, score, b = re.match(r'([a-zA-Z]+) would (gain|lose) ([0-9]+) happiness units by sitting next to ([a-zA-Z]+)\.', line).groups()
    mult = -1 if mult == 'lose' else 1
    graph[a][b] = int(score) * mult
for guest in graph:
    best = max(search(guest, graph))
    break
print_ans('13a', best)
you = {k: 0 for k in graph}
for k in graph:
    graph[k]['You'] = 0
graph['You'] = you
best = max(search('You', graph))
print_ans('13b', best)