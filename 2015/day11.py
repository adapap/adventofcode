"""Day 11: Corporate Policy"""
from aoctools import *

data = Data.fetch(day=11, year=2015)
letters = list(map(ord, 'abcdefghklmnpqrstuvwxyz'))
def is_valid(a):
    seq = any(a[x + 2] == a[x] + 2 and a[x + 1] == a[x] + 1 for x in range(len(a) - 2))
    pairs = list(a[i] for i in filter(lambda x: a[x] == a[x + 1], range(len(a) - 1)))
    return seq and len(set(pairs)) >= 2

def next_password(s):
    chars = list(map(ord, s))
    while True:
        for i in range(len(s) - 1, -1, -1):
            if chars[i] != letters[-1]:
                chars[i] += 1
                if chars[i] not in letters:
                    chars[i] += 1
                break
            else:
                chars[i] = letters[0]
        if is_valid(chars):
            return ''.join(list(map(chr, chars)))

password = next_password(data)
print_ans('11a', password)
print_ans('11b', next_password(password))