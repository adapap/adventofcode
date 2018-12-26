from functools import reduce

with open('input.txt') as f:
    data = f.read()

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
    _hex = ''.join([hex(x)[2:] for x in dense_hash])
    return _hex

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

# lst = list(range(5))
# lengths = [3, 4, 1, 5]
lst = list(range(256))
data = [227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144]
new_lst = knot_round(lst, data)[0]
prod = new_lst[0] * new_lst[1]
print(f'Day 10a: {prod}')

# Part 2
data = '227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144'
knot = knot_hash(data)
print(f'Day 10b: {knot}')