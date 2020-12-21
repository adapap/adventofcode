import aoc
import re
from collections import defaultdict

puzzle = aoc.Puzzle(day=16, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch()
rule, ticket, other = data.split('\n\n')
rules = defaultdict(set)
for line in rule.split('\n'):
    match = re.match(r'(.+): (\d+\-\d+) or (\d+\-\d+)', line)
    field, r1, r2 = match.groups()
    for g in [r1, r2]:
        a, b = map(int, g.split('-'))
        for x in range(a, b + 1):
            rules[field].add(x)
all_values = set()
for v in rules.values():
    all_values = all_values.union(v)
tickets = []
for t in other.split('\n')[1:]:
    valid = True
    for x in map(int, t.split(',')):
        if x not in all_values:
            PART_1 += x
            valid = False
    if valid:
        tickets.append(t)
# puzzle.submit(part=1, answer=PART_1)
possible = [set(rules.keys()) for _ in range(len(rules))]
for t in tickets:
    for i, k in enumerate(map(int, t.split(','))):
        for field in possible[i].copy():
            if k not in rules[field]:
                possible[i].remove(field)
while any(len(x) > 1 for x in possible):
    for i in range(len(possible)):
        if len(possible[i]) == 1:
            for j in range(len(possible)):
                if j == i:
                    continue
                possible[j].difference_update(possible[i])
            i = 0
fields = [x.pop() for x in possible]
my_ticket = list(map(int, ticket.split('\n')[1].split(',')))
PART_2 = 1
for i in range(len(fields)):
    if fields[i].startswith('departure'):
        PART_2 *= my_ticket[i]
puzzle.submit(part=2, answer=PART_2)
