import aoc

puzzle = aoc.Puzzle(day=5, year=2020)
PART_1 = PART_2 = 0
keys = {
    'F': '0',
    'B': '1',
    'L': '0',
    'R': '1',
}
data = puzzle.fetch_by_line()
best = -1
seats = set()
for line in data:
    b = ''.join(keys[x] for x in line)
    boarding_id = int(b, 2)
    best = max(best, boarding_id)
    seats.add(boarding_id)
PART_1 = best
# puzzle.submit(part=1, answer=PART_1)
for seat in seats:
    if seat + 2 in seats and seat + 1 not in seats:
        PART_2 = seat + 1
        break
# puzzle.submit(part=2, answer=PART_2)
