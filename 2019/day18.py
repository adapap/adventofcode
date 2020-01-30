"""Day 18: Many-Worlds Interpretation"""
from aoctools import *
from string import ascii_lowercase as alpha
import time

data = Data.fetch_by_line(day=18, year=2019)
# data = """#########
# #b.A.@.a#
# #########""".split('\n')
# data = """########################
# #f.D.E.e.C.b.A.@.a.B.c.#
# ######################.#
# #d.....................#
# ########################""".split('\n')
grid = Grid2D(default='#')
key_count = 0
start_pos = None
for y, x, item in Data.double_enum(data):
    grid[x, y] = item
    if item in alpha:
        key_count += 1
    elif item == '@':
        start_pos = x, y
# grid.render()
# Dijkstra's
start = (start_pos, frozenset())
pq = PriorityQueue()
pq.put(start, 0)
prev = {}
cost = {}
prev[start] = None
cost[start] = 0
end = None
heuristic = lambda s: len(s[1]) ** 3
t0 = time.time()
while not pq.empty():
    state = pq.get()
    pos, keys = state
    if len(keys) == key_count:
        end = state
        break
    for move in grid.cardinal:
        new_pos = tuple(a + int(b) for a, b in zip(pos, grid.revert(move)))
        item = grid[new_pos]
        if item == '#':
            continue
        if item in alpha.upper() and not item.lower() in keys:
            continue
        new_keys = keys
        if item in alpha:
            new_keys = keys.union({item})
        new_cost = cost[state] + 1
        new_state = (new_pos, new_keys)
        if new_state not in cost or new_cost < cost[new_state]:
            cost[new_state] = new_cost
            prev[new_state] = state
            priority = new_cost + heuristic(new_state)
            pq.put(new_state, priority)
print(f'{time.time() - t0:.4f}s')
path_length = cost[end]
print_ans('18a', path_length)