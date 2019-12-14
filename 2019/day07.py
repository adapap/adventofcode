"""Day 7: Amplification Circuit"""
from aoctools import *
from intcode import Intcode

from itertools import cycle, permutations

data = Data.fetch(day=7, year=2019)
# data = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
# data = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'
# data = '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'
max_thrust = -float('inf')
for input_data in permutations(range(5), 5):
    out = 0
    for x in input_data:
        prog = Intcode.from_csv(data)
        prog.add_inputs(x, out)
        prog.evaluate()
        out = prog.get_output()
    max_thrust = max(out, max_thrust)
print_ans('7a', max_thrust)
max_thrust = -float('inf')
for input_data in permutations(range(5, 10), 5):
    amps = [Intcode.from_csv(data) for _ in range(5)]
    out = 0
    first_cycle = True
    for i in cycle(range(5)):
        if first_cycle:
            amps[i].add_inputs(input_data[i])
        amps[i].add_inputs(out)
        amps[i].evaluate()
        try:
            out = amps[i].get_output()
        except IndexError:
            break
        if i == 4:
            first_cycle = False
            max_thrust = max(out, max_thrust)
print_ans('7b', max_thrust)
# 3808978 < x < 61696857