"""Day 24: Immune System Simulator 20XX"""
from aoctools import Data, print_ans

import copy
import re
from itertools import count

immune_id = count(1)
infection_id = count(1)
class Group:
    def __init__(self, units, hp, atk, atk_type, speed, *, team):
        if team == 'Immune':
            self.team = 'Immune'
            self._id = next(immune_id)
        elif team == 'Infection':
            self.team = 'Infection'
            self._id = next(infection_id)
        self.units = int(units)
        self.hp = int(hp)
        self.atk = int(atk)
        self.atk_type = atk_type
        self.speed = int(speed)
        self.immune = []
        self.weak = []

    @property
    def effective_power(self):
        return self.units * self.atk

    def damage_dealt(self, other):
        if self.atk_type in other.immune:
            return 0
        elif self.atk_type in other.weak:
            return 2 * self.effective_power
        else:
            return self.effective_power

    # def __str__(self):
    #     return f'{self.team} Group {self._id}: {self.units} units (HP: {self.hp}, ATK: {self.atk}, SPD: {self.speed})\
    #     \n\tType: {self.atk_type} | Immunities: {", ".join(self.immune)} | Weaknesses: {", ".join(self.weak)}'

    def __repr__(self):
        return f'{self.team} #{self._id}'

class Army:
    units = []
    original_units = []


data = Data.fetch(day=24, year=2018)
# data = """Immune System:
# 17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
# 989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

# Infection:
# 801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
# 4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4""".strip()
army1, army2 = data.split('\n\n')
for line in army1.split('\n')[1:]:
    match = re.match(r'(\d+) units each with (\d+) hit points (?:\([^)]*\))? ?with an attack that does (\d+) (\w+) damage at initiative (\d+)', line)
    group = Group(team='Immune', *match.groups())
    weak = re.search(r'weak to ([^;)]+)', line)
    if weak:
        group.weak = weak.group(1).split(', ')
    immune = re.search(r'immune to ([^;)]+)', line)
    if immune:
        group.immune = immune.group(1).split(', ')
    Army.units.append(group)

for line in army2.split('\n')[1:]:
    match = re.match(r'(\d+) units each with (\d+) hit points (?:\([^)]*\))? ?with an attack that does (\d+) (\w+) damage at initiative (\d+)', line)
    group = Group(team='Infection', *match.groups())
    weak = re.search(r'weak to ([^;)]+)', line)
    if weak:
        group.weak = weak.group(1).split(', ')
    immune = re.search(r'immune to ([^;)]+)', line)
    if immune:
        group.immune = immune.group(1).split(', ')
    Army.units.append(group)

class Combat:
    stalemate = False

    @staticmethod
    def select_targets():
        targets = set()
        attacking = {}
        for group in sorted(Army.units, key=lambda g: (g.effective_power, g.speed), reverse=True):
            if group.units <= 0:
                continue

            enemies = [unit for unit in Army.units if unit.team != group.team and unit not in targets and group.damage_dealt(unit) > 0]
            enemies = sorted(enemies, key=lambda e: (group.damage_dealt(e), e.effective_power, e.speed), reverse=True)

            if not enemies:
                continue

            target = enemies[0]
            targets.add(target)
            attacking[group] = target
        return attacking

    @staticmethod
    def attack(attacks):
        for group in sorted(Army.units, key=lambda g: g.speed, reverse=True):
            if group.units > 0 and group in attacks:
                attack, defend = group, attacks[group]
                damage = attack.damage_dealt(defend)
                units_lost = min(defend.units, damage // defend.hp)
                if units_lost:
                    defend.units -= units_lost
                    Combat.stalemate = False

    @staticmethod
    def simulate(boost):
        Army.units = copy.deepcopy(Army.original_units)
        for unit in Army.units:
            if unit.team == 'Immune':
                unit.atk += boost
        while len(set(u.team for u in Army.units)) > 1:
            attacks = Combat.select_targets()
            Combat.stalemate = True
            Combat.attack(attacks)
            if Combat.stalemate:
                return 'Infection', -1
            Army.units = [u for u in Army.units if u.units > 0]
        return Army.units[0].team, sum(g.units for g in Army.units)

Army.original_units = copy.deepcopy(Army.units)
_, units = Combat.simulate(boost=0)
print_ans('24a', units)

boost = 1
u = None
while True:
    winner, units = Combat.simulate(boost=boost)
    if winner == 'Immune':
        u = units
        break
    boost += 1
print_ans('24b', units)