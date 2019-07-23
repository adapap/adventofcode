"""Day 4: The Ideal Stocking Stuffer"""
from aoctools import *
from hashlib import md5

data = Data.fetch(day=4, year=2015)
secret = data
number = 0
encoded = ''
while not encoded.startswith('0' * 5):
    number += 1
    to_hash = (secret + str(number)).encode('utf-8')
    encoded = md5(to_hash).hexdigest()
number2 = number
while not encoded.startswith('0' * 6):
    number2 += 1
    to_hash = (secret + str(number2)).encode('utf-8')
    encoded = md5(to_hash).hexdigest()
print_ans('4a', number)
print_ans('4b', number2)