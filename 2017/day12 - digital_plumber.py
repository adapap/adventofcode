from collections import defaultdict

with open('input.txt') as f:
    data = f.readlines()

class Pipeline:
    def __init__(self):
        self.network = defaultdict(list)
        self.seen = None

    def add_link(self, a, b):
        net = self.network
        if b not in net[a]:
            net[a].append(b)
        if a not in net[b]:
            net[b].append(a)

    def find_links(self, pipe):
        if self.seen is None:
            self.seen = [pipe]
        for link in self.network[pipe]:
            if link not in self.seen:
                self.seen.append(link)
                self.find_links(link)
        return self.seen

    def num_links(self, pipe):
        self.seen = None
        return len(self.find_links(pipe))

    @property
    def groups(self):
        pipes = [p for p in self.network.keys()]
        groups = 0
        while pipes:
            links = self.find_links(pipes[0])
            pipes = [p for p in pipes if p not in links]
            groups += 1
        return groups

pipeline = Pipeline()
for line in data:
    vals = line.strip().split(' ')
    pipe = vals[0]
    links = ''.join(vals[2:]).split(',')
    for link in links:
        pipeline.add_link(pipe, link)

part_a = pipeline.num_links('0')
print(f'Day 12a: {part_a}')
print(f'Day 12b: {pipeline.groups}')