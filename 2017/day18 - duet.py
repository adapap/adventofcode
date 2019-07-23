from collections import defaultdict, deque

with open('input.txt') as f:
    instructions = [x.strip().split(' ') for x in f.readlines()]

class Registers:
    def __init__(self, instructions, coprocess=False, **reg):
        self.registers = defaultdict(int)
        self.last_snd = None
        self.first_snd = None
        self.step = 0
        self.instructions = instructions
        self.coprocess = coprocess
        self.waiting = False
        self.other = None
        self.sent = 0
        self.queue = deque()
        for r in reg:
            self.registers[r] = reg[r]
        self.label = '1' if self.registers.get('p', 0) == 1 else '0'

    def loop(self):
        if self.waiting:
            return
        while 0 <= self.step < len(instructions):
            cmd, x = instructions[self.step][:2]
            if len(instructions[self.step]) == 3:
                y = instructions[self.step][2]
            if cmd == 'snd':
                self.snd(x)
            elif cmd == 'set':
                self.set(x, y)
            elif cmd == 'add':
                self.add(x, y)
            elif cmd == 'mul':
                self.mul(x, y)
            elif cmd == 'mod':
                self.mod(x, y)
            elif cmd == 'rcv':
                self.rcv(x)
                if not self.coprocess:
                    if self.first_snd:
                        break
                else:
                    if self.waiting:
                        break
            elif cmd == 'jgz':
                inc = self.jgz(x, y)
                self.step += inc
            self.step += 1

    def reg(self, x):
        try:
            return int(x)
        except ValueError:
            return self.registers[x]

    def snd(self, x):
        self.last_snd = self.reg(x)
        if self.coprocess:
            self.other.queue.append(self.reg(x))
            self.other.waiting = False
            self.sent += 1

    def set(self, x, y):
        self.registers[x] = self.reg(y)

    def add(self, x, y):
        self.registers[x] += self.reg(y)

    def mul(self, x, y):
        self.registers[x] *= self.reg(y)

    def mod(self, x, y):
        self.registers[x] %= self.reg(y)

    def jgz(self, x, y):
        if self.reg(x) > 0:
            return self.reg(y) - 1
        return 0

    def rcv(self, x):
        if not self.coprocess:
            if self.reg(x) != 0 and not self.first_snd:
                self.first_snd = self.last_snd
                # print(self.first_snd)
        else:
            if self.queue:
                self.registers[x] = self.queue.popleft()
            else:
                self.waiting = True

    def __repr__(self):
        return f'<Prog {self.label}>'


duet = Registers(instructions)
duet.loop()
print(f'Day 18a: {duet.first_snd}')

duet_a = Registers(instructions, True, p=0)
duet_b = Registers(instructions, True, p=1)
duet_a.other = duet_b
duet_b.other = duet_a
while not (duet_a.waiting and duet_b.waiting):
    duet_a.loop()
    duet_b.loop()
print(f'Day 18b: {duet_b.sent}')