import aoc

puzzle = aoc.Puzzle(day=5, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch_by_line()

puzzle.submit(part=1, answer=PART_1)
puzzle.submit(part=2, answer=PART_2)
