import aoc
import re
import regex

puzzle = aoc.Puzzle(day=20, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch()
# data = """Tile 2311:
# ..##.#..#.
# ##..#.....
# #...##..#.
# ####.#...#
# ##.##.###.
# ##...#.###
# .#.#.#..##
# ..#....#..
# ###...#.#.
# ..###..###

# Tile 1951:
# #.##...##.
# #.####...#
# .....#..##
# #...######
# .##.#....#
# .###.#####
# ###.##.##.
# .###....#.
# ..#.#..#.#
# #...##.#..

# Tile 1171:
# ####...##.
# #..##.#..#
# ##.#..#.#.
# .###.####.
# ..###.####
# .##....##.
# .#...####.
# #.##.####.
# ####..#...
# .....##...

# Tile 1427:
# ###.##.#..
# .#..#.##..
# .#.##.#..#
# #.#.#.##.#
# ....#...##
# ...##..##.
# ...#.#####
# .#.####.#.
# ..#..###.#
# ..##.#..#.

# Tile 1489:
# ##.#.#....
# ..##...#..
# .##..##...
# ..#...#...
# #####...#.
# #..#.#.#.#
# ...#.#.#..
# ##.#...##.
# ..##.##.##
# ###.##.#..

# Tile 2473:
# #....####.
# #..#.##...
# #.##..#...
# ######.#.#
# .#...#.#.#
# .#########
# .###.#..#.
# ########.#
# ##...##.#.
# ..###.#.#.

# Tile 2971:
# ..#.#....#
# #...###...
# #.#.###...
# ##.##..#..
# .#####..##
# .#..####.#
# #..#.#..#.
# ..####.###
# ..#.#.###.
# ...#.#.#.#

# Tile 2729:
# ...#.#.#.#
# ####.#....
# ..#.#.....
# ....#..#.#
# .##..##.#.
# .#.####...
# ####.#.#..
# ##.####...
# ##..#.##..
# #.##...##.

# Tile 3079:
# #.#.#####.
# .#..######
# ..#.......
# ######....
# ####.#..#.
# .#...#.##.
# #.#####.##
# ..#.###...
# ..#.......
# ..#.###..."""
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
x = {}
tiles = data.split('\n\n')
class Tile:
    def __init__(self, id_, image):
        self.id = id_
        self.image = image
    
    @property
    def edges(self):
        north = self.image[0]
        south = self.image[-1]
        west, east = '', ''
        for row in self.image:
            west += row[0]
            east += row[-1]
        return {
            NORTH: north,
            EAST: east,
            SOUTH: south,
            WEST: west,
        }
    
    @property
    def all_edges(self):
        return [x for x in self.edges.values()] + [x[::-1] for x in self.edges.values()]
        
    def render(self):
        """Prints the tile visualization."""
        for line in self.image:
            print(line)
    
    def flip(self):
        """Flips the tile vertically."""
        self.image = self.image[::-1]
        
    def rotate(self):
        self.image = [''.join(x) for x in zip(*self.image[::-1])]
        
    def __repr__(self):
        return f'<{self.id}>'

tile_map = {}
# Edges holds NESW tuple
for tile in tiles:
    rows = tile.split('\n')
    id_ = rows[0].lstrip('Tile ')[:-1]
    image = rows[1:]
    tile_map[id_] = Tile(id_, image)
neighbors = {}

for id_, tile in tile_map.items():
    edges = set()
    for id2, tile2 in tile_map.items():
        if id_ == id2:
            continue
        if any(x in tile.all_edges for x in tile2.edges.values()):
            edges.add(id2)
    neighbors[id_] = edges
corners = [tile_map[x] for x in neighbors if len(neighbors[x]) == 2]
PART_1 = aoc.Math.prod(*[int(x.id) for x in corners])

# Part 2: Tile Arrangement
size = int(len(tile_map) ** 0.5)
grid = []
for r in range(size):
    grid.append([None] * size)
grid[0][0] = corners[0]
seen = corners[0]
# Arrange corner to be top-left corner
# Needs a neighbor on the south and east border
c = corners[0]
def candidates(e):
    return [t for t in tile_map.values() if e in t.all_edges]
TRANSFORMS = lambda x: [x.rotate] * 4 + [x.flip] + [x.rotate] * 4
for transform in TRANSFORMS(c):
    if len(candidates(c.edges[NORTH])) == 1 and len(candidates(c.edges[WEST])) == 1:
        break
    transform()
# Fill in top row
for x in range(1, size):
    edge = grid[0][x - 1].edges[EAST]
    c = candidates(edge)
    c.remove(grid[0][x - 1])
    for transform in TRANSFORMS(c[0]):
        if c[0].edges[WEST] == edge:
            grid[0][x] = c[0]
            break
        transform()
# Fill in columns, left to right
for x in range(size):
    for y in range(1, size):
        edge = grid[y - 1][x].edges[SOUTH]
        c = candidates(edge)
        c.remove(grid[y - 1][x])
        for transform in TRANSFORMS(c[0]):
            if c[0].edges[NORTH] == edge:
                grid[y][x] = c[0]
                break
            transform()
# Consolidate image into sea monster
image = []
image_size = len(grid[0][0].image[0])
for row in grid:
    subimage = [''] * (image_size - 2)
    for tile in row:
        for i, r in enumerate(tile.image[1:-1]):
            subimage[i] += r[1:-1]
    image.extend(subimage)
image = Tile('final', image)
""" Sea Monster
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
def find_monsters():
    k = len(image.image[0])
    string = '\n'.join(image.image)
    monsters = len(regex.findall('#..{' + str(k - 19) + '}#.{4}##.{4}##.{4}###.{' + str(k - 19) + '}.#.{2}#.{2}#.{2}#.{2}#.{2}#.{3}', string, re.DOTALL, overlapped=True))
    return string.count('#') - (monsters * 15)

t = iter(TRANSFORMS(image))
while True:
    n = find_monsters()
    if n:
        PART_2 = n
        break
    next(t)()
# puzzle.submit(part=1, answer=PART_1)
puzzle.submit(part=2, answer=PART_2)
