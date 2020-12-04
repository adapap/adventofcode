import aoc

puzzle = aoc.Puzzle(day=1, year=2020)
data = puzzle.fetch_by_line()
comp = set()
for x in map(int, data):
    if x in comp:
        p = x * (2020 - x)
        aoc.print_ans('1a', p)
        puzzle.submit(part=1, answer=p)
    comp.add(2020 - x)

nums = list(map(int, data))
result = 0
for x in nums:
    remain = 2020 - x
    for y in nums:
        if y != x and remain - y in nums:
            result = aoc.Math.prod(x, y, remain - y)
aoc.print_ans('1b', result)
