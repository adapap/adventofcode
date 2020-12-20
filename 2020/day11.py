import aoc

puzzle = aoc.Puzzle(day=11, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch_by_line()
grid = aoc.Grid2D(default='.')
for pos, item in aoc.nested_enum(data):
    x, y = pos
    grid[x, y] = item
initial = grid.points.copy()

changed = True
while changed:
    changed = False
    points = grid.points.copy()
    for point in points.copy():
        seat = points[point]
        neighbors = [points[point + x] for x in grid.cardinal]
        if seat == 'L' and '#' not in neighbors:
            grid[point] = '#'
            changed = True
        elif seat == '#' and neighbors.count('#') >= 4:
            grid[point] = 'L'
            changed = True
PART_1 = list(grid.points.values()).count('#')
# puzzle.submit(part=1, answer=PART_1)
grid.points = initial
changed = True
while changed:
    changed = False
    points = grid.points.copy()
    for point in points:
        neighbors = []
        for diff in grid.cardinal:
            m = 1
            while True:
                p = point + (diff * m)
                if not (grid.min_x <= p.real <= grid.max_x) or not (grid.min_y <= p.imag <= grid.max_y):
                    neighbors.append('.')
                    break
                if points[p] != '.':
                    neighbors.append(points[p])
                    break
                m += 1
        seat = points[point]
        if seat == 'L' and '#' not in neighbors:
            grid[point] = '#'
            changed = True
        elif seat == '#' and neighbors.count('#') >= 5:
            grid[point] = 'L'
            changed = True
PART_2 = list(grid.points.values()).count('#')
puzzle.submit(part=2, answer=PART_2)
