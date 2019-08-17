"""Day 17: No Such Thing as Too Much"""
from aoctools import *

data = Data.fetch_by_line(day=17, year=2015)
sizes = list(map(int, data))
def fit_containers(liters, containers, constraint):
    if liters < 0 or constraint < 0:
        return 0
    if liters == 0:
        return 1
    if containers:
        keep = fit_containers(liters - containers[0], containers[1:], constraint - 1)
        take = fit_containers(liters, containers[1:], constraint)
        return keep + take
    return 0

quantity = 150
# sizes = [20, 15, 10, 5, 5]
result = fit_containers(quantity, sizes, constraint=len(sizes))
print_ans('17a', result)
min_containers = 0
minimized = 0
while True:
    minimized = fit_containers(quantity, sizes, constraint=min_containers)
    if minimized:
        break
    min_containers += 1
print_ans('17b', minimized)