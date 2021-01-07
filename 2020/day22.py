import aoc
from collections import deque
from typing import Deque, Tuple

puzzle = aoc.Puzzle(day=22, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch()
decks = [list(map(int, x.split('\n')[1:])) for x in data.split('\n\n')]
def score(deck):
    return sum(x * (len(deck) - i) for i, x in enumerate(deck))
player1 = deque(decks[0])
player2 = deque(decks[1])
while len(player1) and len(player2):
    a, b = player1.popleft(), player2.popleft()
    if a > b:
        player1.extend([a, b])
    else:
        player2.extend([b, a])
winner = player1 or player2
PART_1 = score(winner)
# puzzle.submit(part=1, answer=PART_1)
player1 = deque(decks[0])
player2 = deque(decks[1])
repeated = False
def recursive_combat(p1: Deque[int], p2: Deque[int], depth=1) -> Tuple[int, Deque[int]]:
    seen = set()
    global repeated
    while len(p1) and len(p2):
        k = (tuple(p1), tuple(p2))
        if k in seen:
            repeated = True
            return 1, p1
        seen.add(k)
        a, b = p1.popleft(), p2.popleft()
        winner = None
        if len(p1) < a or len(p2) < b:
            # Winner has higher value card
            winner = 1 if a > b else 2
        else:
            # Recursive combat
            winner, _ = recursive_combat(deque(list(p1)[:a]), deque(list(p2)[:b]), depth + 1)
        if winner == 1:
            p1.extend([a, b])
        elif winner == 2:
            p2.extend([b, a])
    return (1, p1) if p1 else (2, p2)
_, winner = recursive_combat(player1, player2)
PART_2 = score(winner)
# puzzle.submit(part=2, answer=PART_2)
