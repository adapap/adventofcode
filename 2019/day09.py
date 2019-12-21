"""Day 9: Sensor Boost"""
from aoctools import *
from intcode import Intcode

data = Data.fetch(day=9, year=2019)
# Return output as copy of self
# data = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
# Output 16-digit number
# data = '1102,34915192,34915192,7,4,7,99,0'
# Output large number
# data = '104,1125899906842624,99'
prog = Intcode.from_csv(data)
prog.add_inputs(1)
prog.evaluate()
answer = prog.get_output()
print_ans('9a', answer)
prog = Intcode.from_csv(data)
prog.add_inputs(2)
prog.evaluate()
answer = prog.get_output()
print_ans('9b', answer)