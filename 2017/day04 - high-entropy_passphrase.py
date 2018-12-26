with open('input.txt') as f:
    data = f.readlines()
    valid = 0
    valid2 = 0
    for line in data:
        words = line.strip().split(' ')
        words2 = [''.join(sorted(word)) for word in words]
        if len(set(words)) == len(words):
            valid += 1
        if len(set(words2)) == len(words2):
            valid2 += 1
    print(f'Day 4a: {valid}')
    print(f'Day 4b: {valid2}')