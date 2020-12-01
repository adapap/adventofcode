import aoc

data = aoc.Data.fetch_by_line(day=1, year=2020)
comp = set()
for x in map(int, data):
    if x in comp:
        p = x * (2020 - x)
        aoc.print_ans('1a', p)
    comp.add(2020 - x)

nums = list(map(int, data))
result = 0
for x in nums:
    remain = 2020 - x
    for y in nums:
        if y != x and remain - y in nums:
            result = aoc.Math.prod([x, y, remain - y])
aoc.print_ans('1b', result)
