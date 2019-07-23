"""Day 22: Mode Maze"""
from aoctools import Data, Grid2D, PriorityQueue, print_ans

import re

grid = Grid2D()

mouth_pos = (0, 0)
depth = 510
target_pos = (10, 10)

data = Data.fetch(day=22, year=2018)
depth, tx, ty = map(int, re.match(r'depth: (\d+)\s+target: (\d+),(\d+)', data).groups())
target_pos = tx, ty

class Region:
    ROCKY = 0
    WET = 1
    NARROW = 2
    @staticmethod
    def valid_tools(region):
        return [tool for tool in range(3) if tool != region]

class Tool:
    NEITHER = 0
    TORCH = 1
    GEAR = 2

ero_seen = {}
geo_seen = {}
def erosion_level(x, y):
    if (x, y) not in ero_seen:
        ero_seen[x, y] = (geological_index(x, y) + depth) % 20183
    return ero_seen[x, y]

def geological_index(x, y):
    if (x, y) not in geo_seen:
        if (x, y) == mouth_pos or (x, y) == target_pos:
            geo_seen[x, y] = 0
        elif y == 0:
            geo_seen[x, y] = x * 16807
        elif x == 0:
            geo_seen[x, y] = y * 48271
        else:
            geo_seen[x, y] = erosion_level(x - 1, y) * erosion_level(x, y - 1)
    return geo_seen[x, y]

risk = 0
mx, my = mouth_pos
tx, ty = target_pos

for y in range(my, ty + 1):
    for x in range(mx, tx + 1):
        region_type = erosion_level(x, y) % 3
        grid[x, y] = region_type
        risk += region_type
print_ans('22a', risk)

class AStar:
    @staticmethod
    def search(start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        previous = {}
        previous[start] = None
        costs = {}
        costs[start] = 0
        found = False

        while not frontier.empty():
            state = frontier.get()
            px, py, tool = state
            pos = (px, py)
            
            if state == goal:
                found = True
                break
            
            for move in grid.cardinal + [0]:
                next_pos = grid.convert(pos) + move
                x, y = grid.revert(next_pos)

                if x < 0 or y < 0: # Out of bounds
                    continue

                if next_pos not in grid:
                    grid[next_pos] = erosion_level(x, y) % 3
                region_type = grid[next_pos]

                if move == 0:
                    tools = Region.valid_tools(grid[pos])
                    next_state = (px, py, tools[tools.index(tool) - 1])
                else:
                    if tool == region_type: # Cannot use same tool
                        continue

                    next_state = (x, y, tool)

                new_cost = costs[state] + 1
                if move == 0:
                    new_cost += 6
                if next_state not in costs or new_cost < costs[next_state]:
                    costs[next_state] = new_cost
                    priority = new_cost
                    frontier.put(next_state, priority)
                    previous[next_state] = state

        if found:
            path = AStar.trace_path(previous, start, goal)
            cost = sum(costs[p] - costs.get(previous[p], 0) for p in path)
            return path, cost

    @staticmethod
    def heuristic(state, goal):
        return -grid.manhattan(state[:2], goal)

    @staticmethod
    def trace_path(prev, start, goal):
        """Retraces the steps in the path, if it exists."""
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = prev[current]
        path.append(start)
        path.reverse()
        return path

start = (*mouth_pos, Tool.TORCH)
goal = (*target_pos, Tool.TORCH)
result = AStar.search(start, goal)
path, cost = result
print_ans('22b', cost)

# x < 975