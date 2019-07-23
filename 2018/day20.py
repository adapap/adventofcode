"""Day 20: A Regular Map"""
from aoctools import Data, print_ans

from collections import defaultdict

data = Data.fetch(day=20, year=2018)
# data = '^ENWWW(NEEE|SSE(EE|N))$'
# data = '^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$'
# data = '^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$'
# data = '^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$'

dists = defaultdict(int)
cur = (0, 0)
prev = cur
points = [cur]

for char in data[1:-1]:
    if char == '(':
        points.append(cur)
    elif char == ')':
        points.pop()
    elif char == '|':
        cur = points[-1]
    else:
        x, y = cur
        dx, dy = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}.get(char)
        cur = (x + dx, y + dy)
        dists[cur] = min(dists[cur], dists[prev] + 1) if dists[cur] else dists[prev] + 1
    prev = cur
max_len = max(dists.values())
print_ans('20a', max_len)
rooms = sum(x >= 1000 for x in dists.values())
print_ans('20b', rooms)