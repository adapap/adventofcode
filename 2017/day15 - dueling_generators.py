class Generator:
    def __init__(self, *, start_value, factor):
        self.start_value = start_value
        self.value = start_value
        self.factor = factor
        self.div = 2 ** 31 - 1

    def values(self, m=1):
        while True:
            self.value = (self.value * self.factor) % (self.div)
            if self.value % m == 0:
                yield self.value & 0xffff

gen_a = Generator(start_value=883, factor=16807)
gen_b = Generator(start_value=879, factor=48271)

valid = 0
if gen_a.value == gen_b.value:
    valid += 1
a = gen_a.values()
b = gen_b.values()
for x in range(int(40E6)):
    if next(a) == next(b):
        valid += 1
print(f'Day 15a: {valid}')

gen_a.value = gen_a.start_value
gen_b.value = gen_b.start_value
valid = 0
if gen_a.value == gen_b.value:
    valid += 1
a = gen_a.values(4)
b = gen_b.values(8)
for x in range(int(5E6)):
    if next(a) == next(b):
        valid += 1
print(f'Day 15b: {valid}')