"""Day 15: Beverage Bandits"""
from aoctools import Data, Grid, PriorityQueue, Geometry, print_ans

data = Data.fetch_by_line(day=15, year=2018)

class Unit:
    """Handles all tiles in game."""
    def __init__(self, *, atk=0, obj=None):
        self.obj = obj
        self.atk = atk
        self.hp = '-'

    def __eq__(self, other):
        if not isinstance(other, Unit):
            return self.obj == other

    def __repr__(self):
        if self.hp == '-':
            return self.obj
        return f'{self.obj} [{self.hp}]'

class AStar:
    @staticmethod
    def search(start, goal):
        """Finds the shortest path, optionally using a heuristic for speed."""
        frontier = PriorityQueue()
        frontier.put(start, 0)
        previous = {}
        previous[start] = None
        costs = {}
        costs[start] = (0, 0, 0)
        found = False

        while not frontier.empty():
            state = frontier.get()
            
            if state == goal:
                found = True
                break # Add goal response
            
            for move in Geometry.cardinal: # Replace with some form of valid moves
                dx, dy = move
                x, y = state
                next_state = (x + dx, y + dy)
                
                if Combat.grid[next_state] != '.':
                    continue

                new_cost = (costs[state][0] + 1, next_state[1], next_state[0])
                if next_state not in costs or new_cost < costs[next_state]:
                    costs[next_state] = new_cost
                    priority = new_cost
                    frontier.put(next_state, priority)
                    previous[next_state] = state

        if found:
            path = AStar.trace_path(previous, start, goal)
            return path, len(path)

    @staticmethod
    def trace_path(prev, start, goal):
        """Retraces the steps in the path, if it exists."""
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = prev[current]
        path.append(start)
        path.reverse()
        return path

class Combat:
    goblins = 0
    elves = 0
    grid = None
    @staticmethod
    def all_units():
        return [(loc, unit) for loc, unit in sorted(Combat.grid.points.items(),
            key=lambda p: p[0][::-1]) if unit == 'G' or unit == 'E']

    @staticmethod
    def step(point, unit):
        targets = Combat.find_targets(unit)
        candidates = []
        # print(f'{point}: {unit} - Targets: {targets}')
        for t in targets:
            x, y = t
            for pos in [(x + dx, y + dy) for dx, dy in Geometry.cardinal]:
                if pos == point:
                    candidates.append(t)
                    break
        if candidates:
            target = min(candidates, key=lambda t: (Combat.grid[t].hp, t[1], t[0]))
            Combat.attack(unit, target)
            # print(f'{unit} attacking {target}')
        else:
            best_path = Combat.best_path(point, targets)
            if best_path:
                new_pos = best_path[1]
                Combat.grid[new_pos] = unit
                Combat.grid[point] = Unit(obj='.')
                # print(f'Moved to {new_pos}')
                targets = Combat.find_targets(unit)
                candidates = []
                # print(f'{point}: {unit} - Targets: {targets}')
                for t in targets:
                    x, y = t
                    for pos in [(x + dx, y + dy) for dx, dy in Geometry.cardinal]:
                        if pos == new_pos:
                            candidates.append(t)
                            break
                if candidates:
                    target = min(candidates, key=lambda t: (Combat.grid[t].hp, t[1], t[0]))
                    Combat.attack(unit, target)
                    # print(f'{unit} attacking {target}')


    @staticmethod
    def find_targets(unit):
        if unit == 'G':
            enemy = 'E'
        if unit == 'E':
            enemy = 'G'
        return [loc for loc, unit in Combat.all_units() if unit == enemy]

    @staticmethod
    def best_path(point, targets):
        attack_points = []
        for target in targets:
            x, y = target
            for pos in [(x + dx, y + dy) for dx, dy in Geometry.cardinal]:
                if Combat.grid[pos] == '.':
                    attack_points.append(pos)
        # print('Attack Points:', attack_points)
        best_path = [None, float('inf')]
        for p in attack_points:
            path = AStar.search(point, p)
            # print(f'Path to {p}: {path}')
            if path and path[1] < best_path[1]:
                best_path = path
        return best_path[0]

    @staticmethod
    def attack(unit, target):
        Combat.grid[target].hp -= unit.atk
        if Combat.grid[target].hp <= 0:
            if Combat.grid[target] == 'G':
                Combat.goblins -= 1
            elif Combat.grid[target] == 'E':
                Combat.elves -= 1
            Combat.grid[target] = Unit(obj='.')

def simulate_battle(ELF_ATK):
    Combat.grid = Grid(default=Unit(obj='#'))
    Combat.elves = 0
    Combat.goblins = 0
    for y, x, item in Data.double_enum(data):
        unit = Unit(obj=item)
        if item == 'G' or item == 'E':
            unit.hp = 200
            unit.atk = 3
            if item == 'G':
                Combat.goblins += 1
            elif item == 'E':
                unit.atk = ELF_ATK
                Combat.elves += 1
        Combat.grid[x, y] = unit

    rounds = 0
    units = Combat.all_units()

    ORIG_ELVES = Combat.elves
    while Combat.goblins > 0 and Combat.elves > 0:
        units = Combat.all_units()
        for point, unit in units:
            if Combat.grid[point].obj == unit.obj:
                Combat.step(point, unit)
        if Combat.goblins == 0 or Combat.elves == 0:
            break

        if ELF_ATK > 3 and Combat.elves < ORIG_ELVES:
            return False

        rounds += 1
        status = ', '.join([str(u.hp) for _, u in Combat.all_units()])
        print(f'Round {rounds} (ATK: {ELF_ATK})')
    total_hp = 0
    for pos, unit in Combat.all_units():
        total_hp += unit.hp
    return total_hp * rounds

score = simulate_battle(3)
print_ans('15a', score)

score = False
atk = 4
while not score:
    score = simulate_battle(atk)
    if score:
        print_ans('15b', score)
    atk += 1