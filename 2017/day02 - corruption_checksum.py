with open('input.txt') as f:
    data = [row.rstrip() for row in f.readlines()]
total = 0
for row in data:
    nums = [int(x) for x in row.split('\t')]
    total += max(nums) - min(nums)
print(f'Part A: {total}')

total = 0
for row in data:
    nums = [int(x) for x in row.split('\t')]
    pair = (False, False,)
    for start, first in enumerate(nums):
        for second in nums[start + 1:]:
            p = max(first, second), min(first, second)
            if p[0] % p[1] == 0:
                pair = p
        if pair != (False, False,):
            break
    total += pair[0] // pair[1]
print(f'Part B: {total}')