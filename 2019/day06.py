"""Day 6: Universal Orbit Map"""
from aoctools import *
from collections import defaultdict

data = Data.fetch_by_line(day=6, year=2019)
# data = """COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L""".split('\n')
# data = """COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L
# K)YOU
# I)SAN""".split('\n')
graph = defaultdict(list)
for line in data:
    node, edge = line.split(')')
    graph[edge].append(node)
edges = {}
def traverse(node):
    if node in edges:
        return edges[node]
    n = 0
    for parent in graph[node]:
        n += 1 + traverse(parent)
    edges[node] = n
    return edges[node]
orbits = 0
for v in list(graph.keys()):
    orbits += traverse(v)
print_ans('6a', orbits)
def search(node, path):
    if node in path:
        return float('inf')
    path += (node,)
    if node == 'SAN':
        return len(path) - 3
    low = float('inf')
    neighbors = graph[node] + [x for x in graph if node in graph[x]]
    for edge in neighbors:
        length = search(edge, path)
        if length < low:
            low = length
    return low
dist = search('YOU', tuple())
print_ans('6b', dist)