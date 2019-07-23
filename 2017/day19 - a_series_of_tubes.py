from collections import defaultdict
from string import ascii_uppercase as let

with open('input.txt') as f:
    data = [x.strip('\n') for x in f.readlines()]

class Step:
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)
    moves = ['NORTH', 'EAST', 'SOUTH', 'WEST']

class Grid:
    def __init__(self, data):
        self.state = defaultdict(lambda: ' ')
        self.pos = None
        self.dir = 'SOUTH'
        self.steps = 0
        self.letters = []
        for y, row in enumerate(data):
            for x, char in enumerate(row):
                if y == 0 and char != ' ' and self.pos is None:
                    self.pos = (x, y)
                self.state[(x, y)] = char

    def step(self, move):
        return tuple(a + b for a, b in zip(self.pos, move))

    def move(self):
        cur_state = self.state[self.pos]
        new_pos = self.step(getattr(Step, self.dir))
        new_state = self.state[new_pos]
        if cur_state == '|':
            if new_state != ' ':
                self.pos = new_pos
                self.steps += 1
        elif cur_state == '-':
            if new_state != ' ':
                self.pos = new_pos
                self.steps += 1
        elif cur_state == '+':
            left = Step.moves[Step.moves.index(self.dir) - 1]
            left_pos = self.step(getattr(Step, left))
            right = Step.moves[(Step.moves.index(self.dir) + 1) % 4]
            right_pos = self.step(getattr(Step, right))
            if self.state[left_pos] != ' ':
                self.pos = left_pos
                self.dir = left
                self.steps += 1
            elif self.state[right_pos] != ' ':
                self.pos = right_pos
                self.dir = right
                self.steps += 1
            else:
                self.pos = None
        elif cur_state.isalpha():
            if (self.dir == 'NORTH' or self.dir == 'SOUTH') and new_state != ' ':
                self.pos = new_pos
                self.letters.append(cur_state)
                self.steps += 1
            elif (self.dir == 'EAST' or self.dir == 'WEST') and new_state != ' ':
                self.pos = new_pos
                self.letters.append(cur_state)
                self.steps += 1
            else:
                self.letters.append(cur_state)
                self.steps += 1
                self.pos = None
        else:
            self.pos = None

    def __repr__(self):
        return ''.join(self.letters)

grid = Grid(data)
while grid.pos is not None:
    # print(grid.pos, grid.state[grid.pos], grid.dir)
    grid.move()
print(f'Day 19a: {grid}')
print(f'Day 19b: {grid.steps}')