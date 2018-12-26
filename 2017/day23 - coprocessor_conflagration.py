# Instructions
"""
set b 99
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23
"""

b = 99
c = b

def not_prime():
    h = 0
    for x in range(b, c + 1, 17):
        for i in range(2, x):
            if x % i == 0:
                h += 1
                break
    return h
# Part A
mul = (b - 2) ** 2
print(f'Day 23a: {mul}')

# Part B
b = (b * 100) + 100000
c = b + 17000

print(f'Day 23b: {not_prime()}')