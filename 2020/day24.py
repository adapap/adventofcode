import aoc
from collections import defaultdict

puzzle = aoc.Puzzle(day=24, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch_by_line()
grid = aoc.Grid2D(default=0)
neighbors = {
    'e': 1 + 0j,
    'ne': 0 + 1j,
    'nw': -1 + 1j,
    'w': -1 + 0j,
    'sw': 0 - 1j,
    'se': 1 - 1j,
}
def flip_tile(moves, grid):
    p = 0 + 0j
    while moves:
        for k, v in neighbors.items():
            if moves.startswith(k):
                p += v
                moves = moves[len(k):]
    grid[p] ^= 1
                
for line in data:
    flip_tile(line, grid)
PART_1 = sum(grid.points.values())
# puzzle.submit(part=1, answer=PART_1)

def adjacent(p):
    return (p + x for x in neighbors.values())

def tick(grid):
    new_grid = aoc.Grid2D(default=0)
    white_tiles = aoc.Grid2D(default=0)
    black_tiles = [k for k, v in grid.points.items() if v == 1]
    for x in black_tiles:
        n = 0
        for p in adjacent(x):
            if grid[p] == 1:
                n += 1
            else:
                white_tiles[p] += 1
        if n == 0 or n > 2:
            new_grid[x] = 0
        else:
            new_grid[x] = 1
    for x, n in white_tiles.points.items():
        if n == 2:
            new_grid[x] = 1
    grid.points = new_grid.points
for _ in range(100):
    tick(grid)
PART_2 = sum(grid.points.values())
puzzle.submit(part=2, answer=PART_2)
