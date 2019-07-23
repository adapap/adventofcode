"""Day 12: Subterranean Sustainability"""
from aoctools import Data, print_ans

import re
from collections import defaultdict

data = Data.fetch_by_line(day=12, year=2018)
# data = """initial state: #..#.#..##......###...###

# ...## => #
# ..#.. => #
# .#... => #
# .#.#. => #
# .#.## => #
# .##.. => #
# .#### => #
# #.#.# => #
# #.### => #
# ##.#. => #
# ##.## => #
# ###.. => #
# ###.# => #
# ####. => #""".strip().split('\n')

initial_state = re.match(r'initial state: (.+)', data[0]).group(1)
pots = {}
for i, pot in enumerate(initial_state):
    pots[i] = pot

rules = {}
for line in data[2:]:
    k, v = line.split(' => ')
    rules[k] = v

def game_of_life(generations, pots, part_b=False):
    last_num = 0
    last_delta = 0
    for n in range(generations):
        new_pots = {}
        min_pot = min(pots) - 2
        max_pot = max(pots) + 3
        for pot in range(min_pot, max_pot):
            pattern = ''.join(pots.get(x, '.') for x in range(pot - 2, pot + 3))
            new_pots[pot] = rules.get(pattern, '.')
        pots = new_pots
        if part_b:
            num_pots = sum(p for p in new_pots if new_pots[p] == '#')
            if last_delta == num_pots - last_num:
                final = last_delta * (generations - n - 1) + num_pots
                return final
            last_delta = num_pots - last_num
            last_num = num_pots
    return pots

new_pots = game_of_life(20, pots.copy())
num_pots = sum(p for p in new_pots if new_pots[p] == '#')
print_ans('12a', num_pots)

num_pots = game_of_life(int(50E9), pots.copy(), True)
print_ans('12b', num_pots)