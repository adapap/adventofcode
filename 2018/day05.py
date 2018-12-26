"""Day 5: Alchemical Reduction"""
from aoctools import Data, print_ans

import itertools
import re
from string import ascii_lowercase as letters

data = Data.fetch(day=5, year=2018)

def pairwise(x):
    """Returns sequence (s0, s1), (s1, s2)..."""
    a, b = itertools.tee(x)
    next(b, None)
    return zip(a, b)

def react(seq):
    last_polymer = seq
    while True:
        if last_polymer in polymer_dict:
            polymer = polymer_dict[last_polymer]
        else:
            sequence = iter(pairwise(last_polymer))
            reduced = []
            for pair in sequence:
                if pair[0] == pair[1].swapcase():
                    next(itertools.islice(sequence, 1, 1), None)
                else:
                    reduced.append(pair[0])
            else:
                reduced.append(pair[1])
            polymer = ''.join(itertools.chain(*reduced))
            polymer_dict[last_polymer] = polymer
        if polymer == last_polymer:
            break
        last_polymer = polymer
    return len(last_polymer)
result = react(data)
print_ans('5a', result)

min_length = float('inf')
for letter in letters:
    to_remove = letter + letter.upper()
    start = re.sub(f'[{to_remove}]', '', data)
    length = react(start)
    if length < min_length:
        min_length = length
print_ans('5b', min_length)