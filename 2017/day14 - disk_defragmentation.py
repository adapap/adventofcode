from functools import reduce

def reverse_sublist(lst, i, n):
    rev = []
    _i, _n = i, n
    while n > 0:
        rev.append(lst[i])
        i = (i + 1) % len(lst)
        n -= 1
    while n < _n:
        lst[_i] = rev.pop()
        n += 1
        _i = (_i + 1) % len(lst)
    return lst

def knot_round(elements, lengths, i=0, skip=0):
    while lengths:
        elements = reverse_sublist(elements, i, lengths[0])
        i = (i + lengths[0] + skip) % len(elements)
        skip += 1
        lengths = lengths[1:]
    return (elements, i, skip)

def knot_hash(data):
    lst = list(range(256))
    lengths = [ord(x) for x in data] + [17, 31, 73, 47, 23]
    i, skip = 0, 0
    for _ in range(64):
        lst, i, skip = knot_round(lst, lengths, i, skip)
    sparse_hash = lst
    dense_hash = [reduce(lambda x, y: x ^ y, sparse_hash[i:i+16]) for i in range(0, 256, 16)]
    _hex = ''.join([hex(x)[2:].zfill(2) for x in dense_hash])
    return _hex

key = 'wenycdww'
total_used = 0

class Grid:
    def __init__(self):
        self.squares = {}
        self.seen = {}
        self.grid_size = 128

    def find_regions(self):
        regions = 0
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                if self.squares[(x, y)] == '1' and (x, y) not in self.seen:
                    regions += 1
                    self.flood_fill(x, y)
        return regions

    def flood_fill(self, x, y):
        if (x, y) in self.seen or self.squares[(x, y)] == '0':
            return
        self.seen[(x, y)] = True
        if x > 0:
            self.flood_fill(x - 1, y)
        if x < self.grid_size - 1:
            self.flood_fill(x + 1, y)
        if y > 0:
            self.flood_fill(x, y - 1)
        if y < self.grid_size - 1:
            self.flood_fill(x, y + 1)

grid = Grid()
for y in range(128):
    knot_hex = knot_hash(f'{key}-{y}')
    binary = ''.join([bin(int(x, 16))[2:].zfill(4) for x in knot_hex])
    for x in range(128):
        grid.squares[(x, y)] = binary[x]
    total_used += binary.count('1')

print(f'Day 14a: {total_used}')
print(f'Day 14b: {grid.find_regions()}')