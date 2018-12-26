"""Day 21: Chronal Conversion"""
from aoctools import Data, print_ans

# 7510 < x < 127741 < 3179527

lowest = float('inf')
c = 0

def loop(part):
    c = 0
    seen = set()
    last_unique = 0

    while True:
        e = c | 65536
        c = 6718165
        while True:
            d = e & 255
            c += d
            c &= 16777215
            c *= 65899
            c &= 16777215
            if e < 256:
                if part == 1:
                    return c
                    break
                if part == 2:
                    if c not in seen:
                        seen.add(c)
                        last_unique = c
                        break
                    else:
                        return last_unique
            else:
                e = e // 256
print_ans('21a', loop(1))
print_ans('21b', loop(2))