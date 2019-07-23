"""Day 13: Minecart Madness"""
from aoctools import Data, Grid, print_ans

data = Data.fetch_by_line(day=13, year=2018, no_strip=True)
# data = r"""/->-\        
# |   |  /----\
# | /-+--+-\  |
# | | |  | v  |
# \-+-/  \-+--/
#   \------/   """.split('\n')
# data = """|
# v
# |
# |
# |
# ^
# |""".split('\n')
# data = r"""/>-<\  
# |   |  
# | /<+-\
# | | | v
# \>+</ |
#   |   ^
#   \<->/""".split('\n')

grid = Grid()
class Cart:
    moves = {
        0: (0, -1),
        1: (-1, 0),
        2: (0, 1),
        3: (1, 0)
    }
    def __init__(self, x, y, face):
        self.x = x
        self.y = y
        self.face = face
        self.last_turn = 2
        self.track = False

    @property
    def grid_pos(self):
        return grid[self.x, self.y]

    def tick(self):
        dx, dy = Cart.moves.get(self.face)
        self.x += dx
        self.y += dy
        for c in carts:
            if c != self and c.x == self.x and c.y == self.y:
                return f'{self.x},{self.y}'
        if self.grid_pos == '\\':
            self.face = {
            0: 1,
            1: 0,
            2: 3,
            3: 2
            }.get(self.face)
        elif self.grid_pos == '/':
            self.face = {
            0: 3,
            1: 2,
            2: 1,
            3: 0
            }.get(self.face)
        elif self.grid_pos == '+':
            new_turn = (self.last_turn + 1) % 3
            self.last_turn = new_turn
            if new_turn == 0:
                self.face = (self.face + 1) % 4
            # Ignore going straight
            elif new_turn == 2:
                self.face = (self.face - 1) % 4
    def __repr__(self):
        char = {0: '^', 1: '<', 2: 'v', 3: '>'}.get(self.face)
        return f'({self.x}, {self.y}: {char})'
carts = []

for y, x, item in Data.double_enum(data):
    if item == '>':
        carts.append(Cart(x, y, 3))
        grid[x, y] = '-'
    elif item == 'v':
        carts.append(Cart(x, y, 2))
        grid[x, y] = '|'
    elif item == '<':
        carts.append(Cart(x, y, 1))
        grid[x, y] = '-'
    elif item == '^':
        carts.append(Cart(x, y, 0))
        grid[x, y] = '|'
    else:
        grid[x, y] = item


first_collision = None
its = 0
while len(carts) > 1:
    for cart in sorted(carts, key=lambda c: (c.x, c.y)):
        collided = cart.tick()
        if collided:
            carts = [c for c in carts if c.x != cart.x or c.y != cart.y]
            if first_collision is None:
                first_collision = collided
print_ans('13a', first_collision)
print_ans('13b', f'{carts[0].x},{carts[0].y}')