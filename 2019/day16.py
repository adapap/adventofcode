"""Day 16: Flawed Frequency Transmission"""
from aoctools import *

data = Data.fetch(day=16, year=2019)
# data = '12345678'
# data = '11111111'
# data = '80871224585914546619083218645595'
data = '03036732577212944063491565474664'
seq = list(map(int, data))
def next_seq(seq):
    new_seq = [0] * len(seq)
    size = 1
    for i in range(len(seq)):
        n = 0
        for x in range(size - 1, len(seq), 4 * size):
            # print('+', seq[x:x + size])
            n += sum(seq[x:x + size])
        for x in range(3 * size - 1, len(seq), 4 * size):
            # print('-', seq[x:x + size])
            n -= sum(seq[x:x + size])
        new_seq[i] = abs(n) % 10
        size += 1
    return new_seq

def next_partial(seq):
    new_seq = []
    partial = sum(seq)
    for x in seq:
        new_seq += [((partial % 10) + 10) % 10]
        partial -= x
    return new_seq
    
steps = 100
for _ in range(steps):
    seq = next_seq(seq)
print_ans('16a', ''.join(map(str, seq[:8])))
offset = int(data[:7])
seq = list(map(int, data * 10000))[offset:]
for _ in range(steps):
    seq = next_partial(seq)
print_ans('16b', ''.join(map(str, seq[:8])))