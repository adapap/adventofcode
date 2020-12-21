import aoc

puzzle = aoc.Puzzle(day=13, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch_by_line()
time = int(data[0])
best = float('inf')
buses = data[1].split(',')
for bus_id in buses:
    if bus_id == 'x':
        continue
    n = int(bus_id)
    t = time // n * n
    wait = t + n - time
    if wait < best:
        best = wait
        PART_1 = best * n
# puzzle.submit(part=1, answer=PART_1)

# Chinese Remainder Theorem
l = [int(b) for b in buses if b != 'x']
p = aoc.Math.prod(*l)
t = 0
for i in range(len(buses)):
    if buses[i] == 'x':
        continue
    n = p // int(buses[i])
    inv = pow(n, -1, int(buses[i]))
    t += i * n * inv
PART_2 = p - t % p
print(PART_2)
# puzzle.submit(part=2, answer=PART_2)
