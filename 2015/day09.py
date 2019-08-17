"""Day 9: All in a Single Night"""
from aoctools import *
from collections import defaultdict
import re

data = Data.fetch_by_line(day=9, year=2015)
# data = """London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141""".split('\n')

class Node:
    def __init__(self):
        self.visited = False
        self.neighbors = []

def search(graph, start, longest=False):
    costs = {}
    costs[(start,)] = 0
    pq = PriorityQueue()
    pq.put((start,), 0)
    while not pq.empty():
        state = pq.get()
        if all(u in state for u in graph):
            return costs[state]
        moves = graph[state[-1]]
        for move, dist in moves.items():
            if move in state:
                continue
            next_state = state + (move,)
            new_cost = costs[state] + int(dist)
            if next_state not in costs or new_cost < costs[next_state]:
                costs[next_state] = new_cost
                priority = -new_cost if longest else new_cost
                pq.put(next_state, priority)
    return False

# Initialize node graph
nodes = defaultdict(dict)
for line in data:
    a, b, d = re.match(r'(.+) to (.+) = (\d+)', line).groups()
    nodes[a][b] = d
    nodes[b][a] = d
shortest = min(search(nodes, x) for x in nodes)
longest = max(search(nodes, x, longest=True) for x in nodes)
print_ans('9a', shortest)
print_ans('9b', longest)