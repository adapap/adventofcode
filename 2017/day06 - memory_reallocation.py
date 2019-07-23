import re
with open('input.txt') as f:
    data = [int(x) for x in re.split(r'\s+', f.read().strip())]

"""Original solution."""
# seen = {}
# def distribute(blocks):
#     max_cell = max(blocks)
#     i = blocks.index(max_cell)
#     blocks[i] = 0
#     while max_cell > 0:
#         i = (i + 1) % len(blocks)
#         blocks[i] += 1
#         max_cell -= 1
#     return blocks

# blocks = data
# step = 0
# while tuple(blocks) not in seen:
#     seen[tuple(blocks)] = step
#     blocks = distribute(blocks)
#     step += 1
# print(f'Day 6a: {step}')
# print(f'Day 6b: {step - seen[tuple(blocks)]}')

# """Using Floyd cycle finding algorithm."""
seen = {}
def next_state(state):
    lst = list(state)
    if state in seen:
        return seen[state]
    n = max(lst)
    i = lst.index(n)
    lst[i] = 0
    while n > 0:
        i = (i + 1) % len(lst)
        lst[i] += 1
        n -= 1
    seen[state] = tuple(lst)
    return seen[state]

def floyd(f, x):
    """Finds the first occurrence of a cyclic repetition."""
    a = f(x)
    b = f(f(x))
    while a != b:
        a = f(a)
        b = f(f(b))
    
    mu = 0
    a = x
    while a != b:
        a = f(a)
        b = f(b)
        mu += 1
    
    lam = 1
    b = f(a)
    while a != b:
        b = f(b)
        lam += 1
    
    print(f'Day 6a: {mu + lam}')
    print(f'Day 6b: {lam}')

floyd(next_state, tuple(data))