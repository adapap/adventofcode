import aoc
from collections import defaultdict
from typing import DefaultDict, List

puzzle = aoc.Puzzle(day=15, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch()
nums = list(map(int, data.split(',')))
def simulate(turns):
    prev: DefaultDict[int, List[int]] = defaultdict(list)
    last = 0
    for turn, n in enumerate(nums):
        prev[n].append(turn + 1)
        last = n
    for turn in range(turns - len(nums)):
        if len(prev[last]) == 1:
            prev[0].append(turn + len(nums) + 1)
            last = 0
        else:
            n = prev[last][-1] - prev[last][-2]
            prev[n].append(turn + len(nums) + 1)
            last = n
    return last
PART_1 = simulate(2020)
# puzzle.submit(part=1, answer=PART_1)
PART_2 = simulate(30000000)
# Takes about 20s to run
# puzzle.submit(part=2, answer=PART_2)
