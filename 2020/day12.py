import aoc

puzzle = aoc.Puzzle(day=12, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch_by_line()
x, y = 0, 0
face = 1
for line in data:
    op, num = line[:1], int(line[1:])
    if op == 'N' or (op == 'F' and face == 0):
        y += num
    elif op == 'E' or (op == 'F' and face == 1):
        x += num
    elif op == 'S' or (op == 'F' and face == 2):
        y -= num
    elif op == 'W' or (op == 'F' and face == 3):
        x -= num
    elif op == 'L':
        face = (face - num // 90) % 4
    elif op == 'R':
        face = (face + num // 90) % 4
PART_1 = aoc.Geometry.manhattan((0, 0), (x, y))
# puzzle.submit(part=1, answer=PART_1)
import math
def rotate(origin, point, angle):
    """Rotate a point counterclockwise by a given angle around a given origin.
    The angle should be given in radians."""
    ox, oy = origin
    px, py = point
    angle = math.radians(angle)

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return int(qx) - ox, int(qy) - oy
x, y = 0, 0
face = 1
wx, wy = 10, 1
for line in data:
    op, num = line[:1], int(line[1:])
    if op == 'N':
        wy += num
    elif op == 'E':
        wx += num
    elif op == 'S':
        wy -= num
    elif op == 'W':
        wx -= num
    elif op == 'F':
        x += wx * num
        y += wy * num
    elif op == 'L':
        wx, wy = rotate((x, y), (x + wx, y + wy), num)
    elif op == 'R':
        wx, wy = rotate((x, y), (x + wx, y + wy), -num)
PART_2 = aoc.Geometry.manhattan((0, 0), (x, y))
puzzle.submit(part=2, answer=PART_2)
