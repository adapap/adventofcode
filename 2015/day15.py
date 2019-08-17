"""Day 15: Science for Hungry People"""
from aoctools import *
from itertools import combinations_with_replacement as combs
import re

data = Data.fetch_by_line(day=15, year=2015)
size = 100
# data = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3""".split('\n')

class Ingredient:
    def __init__(self, capacity, durability, flavor, texture, calories):
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

ingredients = []
for line in data:
    params = map(int, re.findall(r'\-?\d+', line))
    ingredients.append(Ingredient(*params))

def get_score(ingredients, calories=False):
    cap = max(sum(x.capacity for x in ingredients), 0)
    dur = max(sum(x.durability for x in ingredients), 0)
    fla = max(sum(x.flavor for x in ingredients), 0)
    tex = max(sum(x.texture for x in ingredients), 0)
    cal = max(sum(x.calories for x in ingredients), 0)
    it = [cap, dur, fla, tex]
    if calories and cal != 500:
        return -1
    return prod(it)

best = get_score(max(combs(ingredients, size), key=get_score))
print_ans('15a', best)
best = get_score(max(combs(ingredients, size), key=lambda x: get_score(x, calories=True)))
print_ans('15b', best)