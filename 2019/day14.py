"""Day 14: Space Stoichiometry"""
from aoctools import *
from collections import defaultdict
import re

data = Data.fetch_by_line(day=14, year=2019)
# data = """10 ORE => 10 A
# 1 ORE => 1 B
# 7 A, 1 B => 1 C
# 7 A, 1 C => 1 D
# 7 A, 1 D => 1 E
# 7 A, 1 E => 1 FUEL""".split('\n')

# data = """9 ORE => 2 A
# 8 ORE => 3 B
# 7 ORE => 5 C
# 3 A, 4 B => 1 AB
# 5 B, 7 C => 1 BC
# 4 C, 1 A => 1 CA
# 2 AB, 3 BC, 4 CA => 1 FUEL""".split('\n')

# data = """157 ORE => 5 NZVS
# 165 ORE => 6 DCFZ
# 44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
# 12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
# 179 ORE => 7 PSHF
# 177 ORE => 5 HKGWZ
# 7 DCFZ, 7 PSHF => 2 XJWVT
# 165 ORE => 2 GPVTF
# 3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT""".split('\n')

# data = """2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
# 17 NVRVD, 3 JNWZP => 8 VPVL
# 53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
# 22 VJHF, 37 MNCFX => 5 FWMGM
# 139 ORE => 4 NVRVD
# 144 ORE => 7 JNWZP
# 5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
# 5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
# 145 ORE => 6 MNCFX
# 1 NVRVD => 8 CXFTF
# 1 VJHF, 6 MNCFX => 4 RFSQX
# 176 ORE => 6 VJHF""".split('\n')

class Recipe:
    def __init__(self, inputs: dict, output: int):
        self.inputs = inputs
        self.output = output
    def __repr__(self):
        return '{} => {}'.format(self.inputs, self.output)
graph = {}
for line in data:
    inp, out = line.split(' => ')
    counts = list(map(int, re.findall('\d+', inp)))
    names = re.findall('[A-Z]+', inp)
    inputs = {}
    for name, count in zip(names, counts):
        inputs[name] = count
    count = int(re.search('\d+', out).group(0))
    name = re.search('[A-Z]+', out).group(0)
    graph[name] = Recipe(inputs, count)
def substitute(want, have):
    while True:
        try:
            k = next(x for x in want if x != 'ORE')
        except StopIteration:
            break
        if k == 'ORE':
            continue
        recipe = graph[k]
        repeat, left = divmod(want[k], recipe.output)
        del want[k]
        # Check how many of reactant we need
        if left > 0:
            have[k] = recipe.output - left
            repeat += 1
        # Add all prerequisites to want, less what we have
        # `num` is amount required in recipe
        for x, num in recipe.inputs.items():
            want[x] = want.get(x, 0) + repeat * num - have[x]
            del have[x]
    return want['ORE']
fuel = {'FUEL': 1}
ore = substitute(fuel, defaultdict(int))
print_ans('14a', ore)
TRILLION = int(1e12)
def binary_search(n, step):
    fuel = {'FUEL': n}
    x = substitute(fuel, defaultdict(int))
    # print('Guess:', n, 'Step:', step, 'Ore:', x)
    if x > TRILLION:
        if n - step > 1:
            return binary_search(step + (n - step) // 2, step)
        else:
            return step + (n - step) // 2
    else:
        return binary_search(n * 2, n)
fuel = binary_search(2, 1)
print_ans('14b', fuel)