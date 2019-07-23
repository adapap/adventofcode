import string

with open('input.txt') as f:
    data = f.read().split(',')

class Programs:
    def __init__(self, num):
        self.data = list(string.ascii_lowercase[:num])

    def spin(self, n):
        n %= len(self.data)
        self.data = self.data[-n:] + self.data[:-n]

    def exchange(self, a, b):
        self.data[a], self.data[b] = self.data[b], self.data[a]

    def partner(self, a, b):
        x, y = self.data.index(a), self.data.index(b)
        self.exchange(x, y)

    def __repr__(self):
        return ''.join(self.data)

# data = 's1,x3/4,pe/b'

# dance = Programs(num=5)
dance = Programs(num=16)
original = dance.data

def step(dance):
    for move in data:
        if move.startswith('s'):
            dance.spin(int(move[1:]))
        elif move.startswith('x'):
            a, b = [int(x) for x in move[1:].split('/')]
            dance.exchange(a, b)
        elif move.startswith('p'):
            a, b = move[1:].split('/')
            dance.partner(a, b)

step(dance)

print(f'Day 16a: {dance}')

seen = []
dance = Programs(num=16)

repeat = 1E9
i = 0
while i < repeat:
    if str(dance) not in seen:
        seen.append(str(dance))
        step(dance)
    else:
        print(f'Day 16b: {seen[int(repeat % i)]}')
        break
    i += 1