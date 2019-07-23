"""Day 7: The Sum of Its Parts"""
from aoctools import Data, print_ans

import re
from string import ascii_uppercase as letters

data = Data.fetch_by_line(day=7, year=2018)
# data = """Step C must be finished before step A can begin.
# Step C must be finished before step F can begin.
# Step A must be finished before step B can begin.
# Step A must be finished before step D can begin.
# Step B must be finished before step E can begin.
# Step D must be finished before step E can begin.
# Step F must be finished before step E can begin.""".strip().split('\n')
class Node:
    def __init__(self, value):
        self.parents = []
        self.children = []
        self.value = value
    def __str__(self):
        return self.value
    __repr__ = __str__

    def __gt__(self, other):
        return self.value > other.value
    def __lt__(self, other):
        return self.value < other.value

nodes = {}

for line in data:
    match = re.match(r'Step (\w) must be finished before step (\w) can begin\.', line)
    parent, child = match.groups()
    if parent not in nodes:
        nodes[parent] = Node(parent)
    if child not in nodes:
        nodes[child] = Node(child)
    nodes[parent].children.append(nodes[child])
    nodes[child].parents.append(nodes[parent])

done = []
start = [node for node in nodes.values() if node.parents == []]
queue = start[:]

while queue:
    next_node = min(n for n in queue if all(p in done for p in n.parents))
    for child in next_node.children:
        if child not in queue:
            queue.append(child)
    queue.remove(next_node)
    done.append(next_node)

seq = ''.join(map(str, done))
print_ans('7a', seq)

times = {v: k + 1 for k, v in enumerate(letters)}
workers = 5
step_time = 60

class Worker:
    def __init__(self, item='', time=0):
        self.item = item
        self.time = time
    def __str__(self):
        return f'<{self.item}: {self.time}>'
    __repr__ = __str__

done = []
queue = start[:]
workers = [Worker() for _ in range(workers)]
working = []
total_time = 0

while queue:
    for worker in workers:
        if worker.time == 0:
            if worker.item == '':
                pass
            else:
                queue.remove(worker.item)
                working.remove(worker.item)
                done.append(worker.item)
                worker.item = ''
            valid = [n for n in queue if all(p in done for p in n.parents) and n not in working]
            if valid:
                next_node = min(valid)
                for child in next_node.children:
                    if child not in queue:
                        queue.append(child)
            else:
                continue
            worker.item = next_node
            worker.time = step_time + times[worker.item.value] - 1
            working.append(next_node)
        else:
            worker.time -= 1
    total_time += 1

print_ans('7b', total_time - 1)