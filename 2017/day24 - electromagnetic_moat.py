from collections import defaultdict

with open('input.txt') as f:
    data = f.readlines()

ports = defaultdict(set)
for p in data:
    a, b = list(map(int, p.strip().split('/')))
    ports[a].add(b,)
    ports[b].add(a,)

def dfs(ports, bridge=None):
    bridge = bridge or [(0, 0)]
    val = bridge[-1][1]
    for port in ports[val]:
        if not ((port, val) in bridge or (val, port) in bridge):
            new = bridge + [(val, port)]
            yield new
            yield from dfs(ports, new)

results = []
for v in dfs(ports):
    results.append((len(v), sum(a + b for a, b in v)))

strongest = sorted(results, key=lambda x: x[1])[-1][1]
longest_strongest = sorted(results, reverse=True)[0][1]
print(f'Day 24a: {strongest}')
print(f'Day 24b: {longest_strongest}')