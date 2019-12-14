"""Day 8: Space Image Format"""
from aoctools import *
from collections import defaultdict

data = Data.fetch(day=8, year=2019)
WIDTH = 25
HEIGHT = 6
# data = '123456789012'
# data = '0222112222120000'
image = {}
layers = {}
assert len(data) % (WIDTH * HEIGHT) == 0
for z in range(0, len(data), WIDTH * HEIGHT):
    layer = z // (WIDTH * HEIGHT)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            pixel = data[x + y * WIDTH + z]
            image[x, y, layer] = pixel
            if layer not in layers:
                layers[layer] = defaultdict(int)
            layers[layer][pixel] += 1
best = float('inf')
answer = 0
for k, v in layers.items():
    if v['0'] < best:
        best = v['0']
        answer = v['1'] * v['2']
print_ans('8a', answer)
num_layers = len(layers)
text = '\n'
for y in range(HEIGHT):
    for x in range(WIDTH):
        for z in range(num_layers):
            if image[x, y, z] == '1':
                text += '#'
                break
            elif image[x, y, z] == '0':
                text += ' '
                break
        else:
            text += ' '
    text += '\n'
print_ans('8b', text)