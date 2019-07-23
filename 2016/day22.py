import re
from collections import defaultdict
class Node():
    def __init__(self, x, y, size, is_goal = False):
        self.x = x
        self.y = y
        self.size = size
        if self.size == 0:
            self.char = '_'
        elif self.size >= 100:
            self.char = '#'
        else:
            self.char = '-'
        if is_goal:
            self.char = 'G'
def disp_nodes(nodes):
    result = ''
    for y in nodes:
        row = ''
        for x in nodes[y]:
            row += x.char
        row += f' {y}\n'
        result += row
    print(result)

def solve():
    with open('inp.txt') as f:
        inp = f.readlines()
    nodes = defaultdict(list)
    goal = (29,0)
    start_pos = None
    for line in inp[2:]:
        data = list(map(int, re.split(r'\D+',line)[1:-2]))
        is_goal = True if (data[0],data[1]) == goal else False
        if is_goal:
            start_pos = (data[0], data[1])
        nodes[data[1]].append(Node(data[0], data[1], data[3], is_goal))
    disp_nodes(nodes)
    # 44 to left of goal
    # 5 per move left, 29 moves left
    # First move only costs 1, 28 left moves remaining
    print('Day 22b:', 44 + 5 * 28 + 1)
solve()