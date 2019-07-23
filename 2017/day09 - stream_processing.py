with open('input.txt') as f:
    data = f.read()

i = 0
score = 0
total_score = 0
is_garbage = False
removed = 0
while i < len(data):
    char = data[i]
    if is_garbage:
        if char == '!':
            i += 1
        elif char == '>':
            is_garbage = False
        else:
            removed += 1
    else:
        if char == '{':
            score += 1
        elif char == '}' and score > 0:
            total_score += score
            score -= 1
        elif char == '!' and is_garbage:
            i += 1
        elif char == '<':
            is_garbage = True
    
    i += 1
print(f'Day 9a: {total_score}')
print(f'Day 9b: {removed}')