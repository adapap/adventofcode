"""Day 2: I Was Told There Would Be No Math"""
from aoctools import *
data = Data.fetch_by_line(day=2, year=2015)
total = 0
ribbon = 0
for line in data:
    l, w, h = map(int, line.split('x'))
    dims = [l, w, h]
    faces = [l * w, l * h, w * h]
    slack = min(faces)
    sqft = sum(map(lambda x: x * 2, faces))
    total += sqft + slack
    perimeter = 2 * sum(nsmallest(2, dims))
    bow = prod(dims)
    ribbon += perimeter + bow
print_ans('2a', total)
print_ans('2b', ribbon)