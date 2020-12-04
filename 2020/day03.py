import aoc

data = aoc.Data.fetch_by_line(day=3, year=2020)
grid = aoc.Grid2D()
# Populate grid
for x in aoc.nested_enum(data):
    pos, item = x
    grid[pos] = item
def slope(dx: int, dy: int) -> int:
    x, y = 0, 0
    trees = 0
    while y < grid.max_y:
        x += dx
        y += dy
        pos = x % (grid.max_x + 1), y
        if grid[pos] == '#':
            trees += 1
    return trees
    
a = slope(3, 1)
aoc.print_ans('3a', a)
b = aoc.Math.prod(
    slope(1, 1),
    a,
    slope(5, 1),
    slope(7, 1),
    slope(1, 2),
)
aoc.print_ans('3b', b)
