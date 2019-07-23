with open('input.txt') as f:
    data = f.read()

def find_total(part):
    diff = 1 if part == 'A' else int(len(data) / 2)
    total = 0
    for index, num in enumerate(data):
        if num == data[index - diff]:
            total += int(num)
    print(f'Part {part}: {total}')

find_total('A')
find_total('B')