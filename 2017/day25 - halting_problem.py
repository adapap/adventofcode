from collections import defaultdict

class Turing:
    def __init__(self):
        self.cursor = 0
        self.tape = defaultdict(int)
        self.func = self.A

    @property
    def state(self):
        return self.tape[self.cursor]

    @property
    def checksum(self):
        return sum(self.tape.values())
    

    def A(self):
        if self.state == 0:
            self.tape[self.cursor] ^= 1
            self.cursor += 1
        else:
            self.tape[self.cursor] ^= 1
            self.cursor -= 1
        self.func = self.B

    def B(self):
        if self.state == 0:
            self.cursor += 1
            self.func = self.C
        else:
            self.cursor -= 1

    def C(self):
        if self.state == 0:
            self.tape[self.cursor] ^= 1
            self.cursor += 1
            self.func = self.D
        else:
            self.tape[self.cursor] ^= 1
            self.cursor -= 1
            self.func = self.A

    def D(self):
        if self.state == 0:
            self.tape[self.cursor] ^= 1
            self.cursor -= 1
            self.func = self.E
        else:
            self.cursor -= 1
            self.func = self.F

    def E(self):
        if self.state == 0:
            self.tape[self.cursor] ^= 1
            self.cursor -= 1
            self.func = self.A
        else:
            self.tape[self.cursor] ^= 1
            self.cursor -= 1
            self.func = self.D

    def F(self):
        if self.state == 0:
            self.tape[self.cursor] ^= 1
            self.cursor += 1
            self.func = self.A
        else:
            self.cursor -= 1
            self.func = self.E

checksum = 12586542
machine = Turing()
for _ in range(checksum):
    machine.func()
print(f'Day 25a: {machine.checksum}')