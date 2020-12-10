import aoc
import re
from typing import Dict

puzzle = aoc.Puzzle(day=7, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch_by_line()

class BagNode:
    def __init__(self, color: str, children: Dict[str, int]):
        self.color = color
        self.children = children

    def __repr__(self):
        return f'<{self.color}: {self.children}>'

bags = {}
for line in data:
    matches = re.match(r'(\w+ \w+) bags contain (.+)\.', line).groups()
    parent, children = matches[0], matches[1].split(', ')
    contains = {}
    for child in children:
        if child != 'no other bags':
            tags = child.split(' ')
            contains[' '.join(tags[1:-1])] = int(tags[0])
    bags[parent] = BagNode(parent, contains)

target = {'shiny gold'}
count = 0
while True:
    next_target = target.copy()
    for color in target:
        for bag in bags:
            if color in bags[bag].children:
                if bag not in next_target:
                    count += 1
                    changed = True
                    next_target.add(bag)
    if next_target == target:
        break
    target = next_target
PART_1 = len(target) - 1

memo = {}
def dfs(node: BagNode) -> int:
    if node.color in memo:
        return memo[node.color]
    total = 0
    for child, n in node.children.items():
        total += n + n * dfs(bags[child])
    memo[node.color] = total
    return total
PART_2 = dfs(bags['shiny gold'])
# puzzle.submit(part=1, answer=PART_1)
puzzle.submit(part=2, answer=PART_2)
