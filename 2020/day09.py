import aoc

puzzle = aoc.Puzzle(day=9, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch_by_line()
def find_invalid(preamble):
    prev = [int(x) for x in data[:preamble]]
    offset = 0
    while True:
        invalid = True
        num = int(data[preamble + offset])
        # Check if num is valid
        for i in range(preamble):
            for j in range(i, preamble):
                if prev[i] + prev[j] == num:
                    i = preamble
                    invalid = False
                    break
        if invalid:
            return num
        prev = prev[1:] + [num]
        offset += 1
PART_1 = find_invalid(25)
nums = list(map(int, data))
start = 0
size = 2
while True:
    a = nums[start:start + size]
    s = sum(a)
    if s > PART_1:
        start += 1
        size = 2
        continue
    if s == PART_1:
        PART_2 = min(a) + max(a)
        break
    size += 1
print(PART_2)
# puzzle.submit(part=1, answer=PART_1)
# puzzle.submit(part=2, answer=PART_2)
