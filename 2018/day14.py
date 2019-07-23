"""Day 14: Chocolate Charts"""
from aoctools import Data, print_ans

recipes = [3, 7]
elf0, elf1 = 0, 1

data = Data.fetch(day=14, year=2018)
# data = '59414'
num_recipes = int(data)
token = [int(x) for x in data]
found = False

moving_sum = 10
n = 0
ans = None
while not found or not ans:
    if n and not n % 1E5:
        print(n)
    recipes.extend(divmod(moving_sum, 10) if moving_sum >= 10 else [moving_sum])
    elf0 = (elf0 + recipes[elf0] + 1) % len(recipes)
    elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
    moving_sum = recipes[elf0] + recipes[elf1]
    # Part 1
    if n == num_recipes + 10 and not ans:
        ans = ''.join(str(x) for x in recipes[num_recipes:num_recipes + 10])
    # Part 2
    token_a = recipes[-len(token):] == token
    token_b = recipes[-len(token)-1:-1] == token
    if (token_a or token_b) and not found:
        found = len(recipes) - len(token)
        if token_b:
            found -= 1
    n += 1
print_ans('14a', ans)
print_ans('14b', found)