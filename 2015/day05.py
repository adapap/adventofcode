"""Day 5: Doesn't He Have Intern-Elves For This?"""
from aoctools import *
from string import ascii_lowercase as alphabet

data = Data.fetch_by_line(day=5, year=2015)
def is_nice(s):
    min_3_vowels = sum(s.count(x) for x in 'aeiou') >= 3
    double_letter = any(x + x in s for x in alphabet)
    exclude_strings = not any(x in s for x in ['ab', 'cd', 'pq', 'xy'])
    return min_3_vowels and double_letter and exclude_strings
def is_nice2(s):
    pair = any(s.count(s[i:i+2]) >= 2 for i in range(len(s) - 1))
    repeat = any(s[i] == s[i + 2] for i in range(len(s) - 2))
    return pair and repeat
total = sum(is_nice(x) for x in data)
total2 = sum(is_nice2(x) for x in data)
print_ans('5a', total)
print_ans('5b', total2)