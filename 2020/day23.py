import aoc
from collections import deque

puzzle = aoc.Puzzle(day=23, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch()
# data = '389125467'
class LinkedNode:
    def __init__(self, value: int, next: int):
        self.value = value
        self.next = next

    def __repr__(self):
        return f'{self.value} -> {self.next}'

def run_game(cups, moves):
    nodes = [None] * len(cups) + [None]
    for i, cup in enumerate(cups):
        nodes[cup] = LinkedNode(cup, cups[(i + 1) % len(cups)])
    curr = nodes[cups[0]]
    result = ''
    for move in range(moves):
        if move % 100_000 == 0:
            print(f'{move / moves * 100:.0f}%')
        a = nodes[curr.next]
        b = nodes[a.next]
        c = nodes[b.next]
        # Fill gaps between 
        curr.next = nodes[c.next].value
        # Select destination cup
        dest = None
        n = curr.value
        while True:
            n = (n - 1) or len(cups)
            if n not in (a.value, b.value, c.value):
                dest = nodes[n]
                break
        # Move cups after destination cup
        c.next = dest.next
        dest.next = a.value
        curr = nodes[curr.next]
    x = nodes[1]
    for _ in range(len(nodes)):
        if x.value != 1:
            result += str(x.value)
        x = nodes[x.next]
    return nodes, result
_, PART_1 = run_game(list(map(int, data)), 100)
# puzzle.submit(part=1, answer=PART_1)
result, _ = run_game(list(map(int, data)) + list(range(10, 1_000_001)), 10_000_000)
a = result[1].next
b = result[a].next
PART_2 = a * b
# puzzle.submit(part=2, answer=PART_2)
