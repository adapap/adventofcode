import aoc
from collections import defaultdict

puzzle = aoc.Puzzle(day=10, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch_by_line(numeric=True)
data = sorted(data)
counts = defaultdict(int)
for a, b in zip(data[:-1], data[1:]):
    counts[b - a] += 1
counts[data[0]] += 1
counts[3] += 1
PART_1 = counts[1] * counts[3]
# puzzle.submit(part=1, answer=PART_1)
memo = {data[-1]: 1}
def search(lst):
    n = lst[0]
    if n in memo:
        return memo[n]
    total = 0
    for i in range(1, 4):
        if i < len(lst) and lst[i] - n <= 3:
            total += search(lst[i:])
    memo[n] = total
    return total
search([0] + data)
PART_2 = memo[0]
# puzzle.submit(part=2, answer=PART_2)
