"""Day 12: JSAbacusFramework.io"""
from aoctools import *
import json
import re

data = Data.fetch(day=12, year=2015)
print_ans('12a', sum(map(int, re.findall(r'\-?[0-9]+', data))))
def find_sum(item):
    if type(item) == dict:
        if 'red' in item.values():
            return 0
        return sum(map(find_sum, item.values()))
    elif type(item) == list:
        return sum(map(find_sum, item))
    elif type(item) == int:
        return item
    return 0
obj = json.loads(data)
print_ans('12b', find_sum(obj))