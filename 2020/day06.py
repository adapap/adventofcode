import aoc

puzzle = aoc.Puzzle(day=6, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch()
for group in data.split('\n\n'):
    answers = group.split('\n')
    PART_1 += len(set(''.join(answers)))
    seen = set(answers[0])
    for answer in answers:
        seen = seen.intersection(answer)
    PART_2 += len(seen)
print(PART_2)
# puzzle.submit(part=1, answer=PART_1)
# puzzle.submit(part=2, answer=PART_2)
