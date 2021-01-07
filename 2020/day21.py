import aoc
import re
from collections import defaultdict

puzzle = aoc.Puzzle(day=21, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch_by_line()
# data = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)""".split('\n')

labelled = defaultdict(set)
counts = defaultdict(int)
for line in data:
    match = re.match(r'((?:\w+ ?)+) \(contains ((?:\w+,? ?)+)\)', line)
    a, b = match.groups()
    ingredients = a.split(' ')
    allergens = b.split(', ')
    for x in ingredients:
        counts[x] += 1
    for x in allergens:
        if x not in labelled:
            labelled[x] = set(ingredients)
        else:
            labelled[x] = labelled[x].intersection(set(ingredients))
has_allergen = set()
for x in labelled:
    has_allergen = has_allergen.union(labelled[x])
PART_1 = sum(counts[x] for x in counts if x not in has_allergen)
# puzzle.submit(part=1, answer=PART_1)
solved = set()
remove = set()
has = {}
while len(solved) < len(labelled):
    for k in labelled:
        if k in solved:
            continue
        labelled[k].difference_update(remove)
        if len(labelled[k]) == 1:
            solved.add(k)
            ingredient = labelled[k].pop()
            remove.add(ingredient)
            has[ingredient] = k
PART_2 = ','.join(sorted(has.keys(), key=lambda x: has[x]))
puzzle.submit(part=2, answer=PART_2)
