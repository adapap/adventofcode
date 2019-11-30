"""Day 20: Infinite Elves and Infinite Houses"""
from aoctools import *
from math import sqrt
from functools import reduce

data = int(Data.fetch(day=20, year=2015))
# data = 70
def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))
def find_house(goal):
    h = 0
    while True:
        h += 1
        # if h % 10000 == 0:
        #     print(h)
        presents = sum(factors(h)) * 10
        if presents >= goal:
            return h
house = find_house(data)
print_ans('20a', house)

houses = [0] * (data // 10)
for i in range(1, data // 10):
    for j in range(i, data // 10, i):
        if j > 50 * i:
            break
        houses[j] += i * 11
house = next(i for i, x in enumerate(houses) if x >= data)
print_ans('20b', house)