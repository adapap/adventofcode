import aoc
import regex

puzzle = aoc.Puzzle(day=19, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch()
ruleset, messages = data.split('\n\n')
rules = {}
reduced = set()
for r in ruleset.split('\n'):
    id_, rule = r.split(': ')
    if rule in ('"a"', '"b"'):
        rules[id_] = rule[1]
        reduced.add(id_)
    else:
        rules[id_] = rule.split(' ')
unreduced = rules.copy()
# Reduce rules to regular expressions
def reduce_rules(rules):
    while True:
        reduce = False
        for rule in rules:
            if rule in reduced:
                continue
            if not any(x.isdigit() for x in rules[rule]):
                reduced.add(rule)
                reduce = True
            new_rule = []
            for x in rules[rule]:
                if x in reduced:
                    if '|' in rules[x]:
                        new_rule += '(' + ''.join(rules[x]) + ')'
                    else:
                        new_rule += rules[x]
                    reduce = True
                else:
                    new_rule.append(x)
            rules[rule] = new_rule
        if not reduce:
            break
    return '^' + r''.join(rules['0']) + '$'
patt = reduce_rules(rules)
for msg in messages.split('\n'):
    if match := regex.match(patt, msg):
        PART_1 += 1
# puzzle.submit(part=1, answer=PART_1)

# Update rules 8 and 11
rules = unreduced
reduced = set()
rules['8'] = ['42', '+']
rules['11'] = ['?P<R>', '42', '(?&R)?', '31']
patt = reduce_rules(rules)
for msg in messages.split('\n'):
    if match := regex.match(patt, msg):
        PART_2 += 1
# 261 < x < 309
puzzle.submit(part=2, answer=PART_2)
