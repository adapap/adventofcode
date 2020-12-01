"""Day 18: Many-Worlds Interpretation"""
from aoctools import *

# data = Data.fetch_by_line(day=18, year=2019)

# data = """#########
# #b.A.@.a#
# #########""".split('\n')

# data = """########################
# #f.D.E.e.C.b.A.@.a.B.c.#
# ######################.#
# #d.....................#
# ########################""".split('\n')

# data = """########################
# #...............b.C.D.f#
# #.######################
# #.....@.a.B.c.d.A.e.F.g#
# ########################""".split('\n')

# data = """#######
# #a.#Cd##
# ##...##
# ##.@.##
# ##...##
# #cB#Ab#
# #######""".split('\n')

data = """#############
#DcBa.#.GhKl#
#.###...#I###
#e#d#.@.#j#k#
###C#...###J#
#fEbA.#.FgHi#
#############""".split('\n')

# data = """###############
# #d.ABC.#.....a#
# ######...######
# ######.@.######
# ######...######
# #b.....#.....c#
# ###############""".split('\n')

grid = Grid2D(default='#')
key_count = 0
key = {}
item_pos = []
start_pos = None
for y, x, item in Data.double_enum(data):
    grid[x, y] = item
    if item.islower():
        item_pos.append((x, y))
        key[item] = 1 << key_count
        key[item.upper()] = 1 << key_count
        key_count += 1
    elif item == '@':
        start_pos = x, y
        item_pos.append(start_pos)
# grid.render()
graph = defaultdict(dict)
# heuristic = lambda x: x[1] * 10
def get_cost(start_pos, goal_pos):
    start = (start_pos, 0b0)
    pq = PriorityQueue()
    pq.put(start, 0)
    costs = {}
    costs[start] = 0
    while not pq.empty():
        state = pq.get()
        pos, need = state
        if pos == goal_pos:
            graph[start_pos][goal_pos] = (costs[state], need)
            graph[goal_pos][start_pos] = (costs[state], need)
            return
        for move in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            new_pos = pos[0] + move[0], pos[1] + move[1]
            new_need = need
            item = grid[new_pos]
            if item == '#':
                continue
            if item.isupper():
                new_need = new_need | key[item]
            cost = costs[state] + 1
            new_state = (new_pos, new_need)
            if new_state not in costs or cost < costs[new_state]:
                costs[new_state] = cost
                priority = cost
                pq.put(new_state, priority)
# Build graph of edges (pos: {pos2: (cost, keys)})
# for i, x in enumerate(item_pos):
#     print(f'{i + 1}/{len(item_pos)}')
#     for y in item_pos[i + 1:]:
#         get_cost(x, y)
# Dijkstra's: pos is tuple (x, y), keys is bitmask 1 << key_count
def dijkstra(skip=[]):
    start = (start_pos, 0b0)
    pq = PriorityQueue()
    pq.put(start, 0)
    prev = {}
    costs = {}
    prev[start] = None
    costs[start] = 0
    end = None
    while not pq.empty():
        state = pq.get()
        pos, keys = state
        if keys == 2 ** key_count - 1:
            end = state
            break
        for new_pos, (new_cost, need) in graph[pos].items():
            if not keys & need == need:
                continue
            item = grid[new_pos]
            new_keys = keys
            if item.islower():
                new_keys = keys | key[item]
            cost = costs[state] + new_cost
            new_state = (new_pos, new_keys)
            if new_state not in costs or cost < costs[new_state]:
                costs[new_state] = cost
                prev[new_state] = state
                priority = cost
                pq.put(new_state, priority)
    if skip == []:
        return costs[end]
    path = []
    while end is not None:
        pos, _ = end
        path.append(pos)
        end = prev[end]
    return path[::-1]
# path_length = dijkstra()
# print_ans('18a', path_length)
# Part 2
graph = defaultdict(dict)
item_pos.remove(start_pos)
starts = []
for p in grid.diagonal:
    pos = tuple(map(int, grid.revert(grid.convert(start_pos) + p)))
    starts.append(pos)
    grid[pos] = '@'
    item_pos.append(pos)
for p in grid.cardinal:
    pos = tuple(map(int, grid.revert(grid.convert(start_pos) + p)))
    grid[pos] = '#'
grid[start_pos] = '#'
start_pos = starts[0]
for i, x in enumerate(item_pos):
    print(f'{i + 1}/{len(item_pos)}')
    for y in item_pos[i + 1:]:
        get_cost(x, y)
    for start in starts:
        graph[x][start] = (0, 0)
for i, x in enumerate(starts):
    for y in starts[i + 1:]:
        graph[x][y] = (0, 0)
        graph[y][x] = (0, 0)
# Keep track of position of robots, calculate steps
path = dijkstra(skip=starts)
print(' '.join(grid[p] for p in path))
# print_ans('18b', path_length)
# x < 5221