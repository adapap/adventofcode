"""Day 10: Monitoring Station"""
from aoctools import *
import math

data = Data.fetch_by_line(day=10, year=2019)
# data = """.#..#
# .....
# #####
# ....#
# ...##""".split('\n') # n = 8

# data = """......#.#.
# #..#.#....
# ..#######.
# .#.#.###..
# .#..#.....
# ..#....#.#
# #..#....#.
# .##.#..###
# ##...#..#.
# .#....####""".split('\n') # n = 33

# data = """.#..##.###...#######
# ##.############..##.
# .#.######.########.#
# .###.#######.####.#.
# #####.##.#.##.###.##
# ..#####..#.#########
# ####################
# #.####....###.#.#.##
# ##.#################
# #####.##.###..####..
# ..######..##.#######
# ####.##.####...##..#
# .#####..#.######.###
# ##...#.##########...
# #.##########.#######
# .####.#.###.###.#.##
# ....##.##.###..#####
# .#.#.###########.###
# #.#.#.#####.####.###
# ###.##.####.##.#..##""".split('\n') # n = 210
grid = Grid2D(default='/')
for y, x, item in Data.double_enum(data):
    grid[x, y] = item
def get_angle(a, b):
    dy = b.imag - a.imag
    dx = b.real - a.real
    deg = math.degrees(math.atan2(dx, dy))
    return deg

def find_asteroids(a):
    points = {}
    for b in asteroids:
        angle = get_angle(a, b)
        if angle not in points or grid.manhattan(a, b) < grid.manhattan(a, points[angle]):
            points[angle] = b
    return points
# Assume detection station is on an asteroid
asteroids = [p for p, x in grid.points.items() if x == '#']
best = 0
pts = None
for a in asteroids:
    points = find_asteroids(a)
    if len(points) > best:
        best = len(points)
        pts = [points[k] for k in sorted(points)]
print_ans('10a', best)
point = pts[-200]
score = int(point.real * 100 + point.imag)
print_ans('10b', score)