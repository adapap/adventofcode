import aoc
import re

data = aoc.Data.fetch_by_line(day=4, year=2020)
passports = []
p = {}
for line in data:
    if line.strip() == '':
        passports.append(p)
        p = {}
    else:
        fields = line.strip().split(' ')
        for x in fields:
            k, v = x.split(':')
            p[k] = v
passports.append(p)
valid = 0
valid2 = 0
KEYS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
for p in passports:
    if KEYS.intersection(set(p.keys())) == KEYS:
        valid += 1
    else:
        continue
    rules = [
        1920 <= int(p['byr']) <= 2002,
        2010 <= int(p['iyr']) <= 2020,
        2020 <= int(p['eyr']) <= 2030,
        bool(re.match(r'^#[0-9a-f]{6}$', p['hcl'])),
        p['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        bool(re.match(r'^[0-9]{9}$', p['pid'])),
    ]
    hgt, unit = p['hgt'][:-2], p['hgt'][-2:]
    if hgt == '':
        continue
    if unit == 'cm':
        rules.append(150 <= int(hgt) <= 193)
    elif unit == 'in':
        rules.append(59 <= int(hgt) <= 76)
    else:
        continue
    if all(rules):
        valid2 += 1   
aoc.print_ans('4a', valid)
aoc.print_ans('4b', valid2)
