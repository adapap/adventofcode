from collections import defaultdict

steps = 345

spinlock = [0]
cur_pos = 0
for i in range(1, 2018):
    cur_pos = (cur_pos + steps) % len(spinlock)
    spinlock.insert(cur_pos + 1, i)
    cur_pos += 1
print(f'Day 17a: {spinlock[spinlock.index(2017) + 1]}')

cur_pos = 0
val = 0
for spin in range(1, 50 * 1000000):
    cur_pos = (cur_pos + steps) % spin
    if cur_pos == 0:
        val = spin
    cur_pos += 1

print(f'Day 17b: {val}')