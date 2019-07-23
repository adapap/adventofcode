with open('input.txt') as f:
    data = [int(l.strip()) for l in f.readlines()]

class CPU:
    def __init__(self, instructions):
        self.pos = 0
        self.instructions = instructions
        self.len = len(instructions)

    def cycle(self):
        count = 0
        while self.pos in self.instructions:
            step = self.instructions[self.pos]
            self.instructions[self.pos] += 1
            self.pos += step
            count += 1
        print(f'Day 5a: {count}')

    def cycle2(self):
        count = 0
        while self.pos >= 0 and self.pos < self.len:
            step = self.instructions[self.pos]
            if self.instructions[self.pos] >= 3:
                self.instructions[self.pos] -= 1
            else:
                self.instructions[self.pos] += 1
            self.pos += step
            count += 1
        print(f'Day 5b: {count}')

cpu = CPU(data)
cpu.cycle()

cpu = CPU(data)
cpu.cycle2()