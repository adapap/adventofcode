import heapq
from collections import defaultdict
from time import time

class PriorityQueue:
    """
    A data structure in which elements get added according to priority values
    """
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]


class AStar:

    def __init__(self, graph):
        self.graph = graph
        self.path = None

    def heuristic(self, state):
        return len(state[2]) ** 2

    def is_valid(self, state):
        x, y = state
        if x < 0 or x > self.graph.size[0] or y < 0 or y > self.graph.size[1]:
            return False
        if self.graph.nodes[state] == '#':
            return False
        return True

    def search(self, start, goal, part_b=False):
        """
        Finds the shortest path, optionally using a heuristic for speed
        """
        self.part_b = part_b
        frontier = PriorityQueue()
        frontier.put(start, 0)
        previous = {}
        previous[start] = None
        costs = {}
        costs[start] = 0
        end_state = None

        while not frontier.empty():
            state = frontier.get()
            
            if len(state[2]) == goal:
                end_state = state
                self.path = previous
                break
            
            directions = [(0, 1,), (0, -1,), (1, 0,), (-1, 0,)]
            for direction in directions:
                next_pos = tuple(sum(x) for x in zip(state[:2], direction))
                if not self.is_valid(next_pos):
                    continue
                collected = state[2]
                char = self.graph.nodes[next_pos]
                if char.isdigit() and char not in collected:
                    collected += (char,)
                    if part_b and len(collected) == goal - 1:
                        self.graph.nodes[self.graph.start] = '9'
                next_state = next_pos + (collected,)
                new_cost = costs[state] + 1
                if next_state not in costs or new_cost < costs[next_state]:
                    costs[next_state] = new_cost
                    priority = new_cost - self.heuristic(next_state)
                    frontier.put(next_state, priority)
                    previous[next_state] = state

        path = self.trace_path(start, goal, end_state)
        return path, len(path)

    def trace_path(self, start, goal, end_state):
        """
        Retraces the steps in the path, if it exists
        """
        if self.path is None:
            print('Path does not exist')
            return None
        current = self.path[end_state]
        path = [end_state]
        while current != start:
            path.append(current)
            current = self.path[current]
        path.append(start)
        path.reverse()
        return path

    def __len__(self):
        if self.path is not None:
            return len(self.path)
        return None

class System:
    def __init__(self, file):
        self.nodes = defaultdict(tuple)
        self.goal = 0
        self.start = None
        self.size = [0, 0]
        with open(file) as f:
            for row, line in enumerate(f.readlines()):
                if row > self.size[0]:
                    self.size[0] = row
                for col, char in enumerate(line):
                    if col > self.size[1]:
                        self.size[1] = col
                    self.nodes[(row, col,)] = char
                    if char.isdigit():
                        self.goal += 1
                        if char == '0':
                            self.start = (row, col,)

def show_path(path):
    for pos in path:
        print(pos[:2])

graph = System('inp.txt')
time_start = time()
finder = AStar(graph)
path = finder.search(graph.start + (('0',),), graph.goal)
time_end = time()
print(f'Time Elapsed: {time_end - time_start:.2f}s')
print('Day 24a:', path[1] - 1)
print('Collect Order:', ' > '.join(path[0][-1][2]))

time_start = time()
finder = AStar(graph)
path = finder.search(graph.start + (('0',),), graph.goal + 1, part_b=True)
time_end = time()
print(f'Time Elapsed: {time_end - time_start:.2f}s')
print('Day 24b:', path[1] - 1)
print('Collect Order:', ' > '.join(path[0][-1][2]))