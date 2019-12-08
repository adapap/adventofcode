"""Day 7: Amplification Circuit"""
from aoctools import *
from intcode import Intcode

from itertools import permutations

data = Data.fetch(day=7, year=2019)
data = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
prog = Intcode.from_csv(data)
max_thrust = -float('inf')
for input_data in permutations(range(5), 5):
    print(input_data)
    result = prog.evaluate(iter(input_data))
    if result > max_thrust:
        max_thrust = result
        print(max_thrust)