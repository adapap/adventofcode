import aoc

puzzle = aoc.Puzzle(day=25, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch_by_line()
card, door = list(map(int, data))
subject = 7
n = 1
loop = 1
while True:
    n *= subject
    n %= 20201227
    if n == card:
        break
    loop += 1
n = 1
for l in range(loop):
    n *= door
    n %= 20201227
PART_1 = n
puzzle.submit(part=1, answer=PART_1)
# puzzle.submit(part=2, answer=PART_2)
