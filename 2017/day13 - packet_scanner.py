with open('input.txt') as f:
    data = f.readlines()

class Scanner:
    def __init__(self, depth, _range):
        self.depth = depth
        self._range = _range

    @property
    def severity(self):
        return self.depth * self._range
    
    def get_state(self, time=0):
        height = self._range
        period = 2 * (height - 1)
        steps = (self.depth + time) % period
        return 2 * (height - 1) if steps > height - 1 else steps

scanners = []
for line in data:
    nums = [int(x) for x in line.strip().split(': ')]
    scanners.append(Scanner(*nums))

severity = 0
for scanner in scanners:
    if scanner.get_state() == 0:
        severity += scanner.severity
print(f'Day 13a: {severity}')

time = 0
while any(scanner.get_state(time) == 0 for scanner in scanners):
    time += 1
print(f'Day 14a: {time}')