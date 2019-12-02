"""RPG Simulator 20XX"""
from aoctools import *
import re

store = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""
items = {
    'weapon': [],
    'armor': [],
    'ring': [],
}
item_type = 'weapon'
for line in store.split('\n'):
    if line.startswith('Armor'):
        item_type = 'armor'
    elif line.startswith('Rings'):
        item_type = 'ring'
    values = list(map(int, re.findall('\d', line)))
    if len(values) >= 3:
        items[item_type].append(values[-3:])
print(items)
        
data = Data.fetch(day=21, year=2015)
class Player:
    def __init__(self, hp, damage, armor):
        self.hp = hp
        self.damage = damage
        self.armor = armor
    
    def battle(self, other) -> bool:
        a = self.hp
        b = other.hp
        while a > 0 and b > 0:
            a -= other.damage - self.armor
            if a <= 0:
                break
            b -= self.damage - other.armor
        return a <= 0
            
    def __repr__(self):
        return f'[{self.damage} A|{self.armor} D] {self.hp} HP'

hp, damage, armor = list(map(int, re.findall('\d+', data)))
boss = Player(hp, damage, armor)
# print(Player(8, 5, 5).simulate(Player(12, 7, 2)))