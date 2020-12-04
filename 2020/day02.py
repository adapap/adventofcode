import aoc

data = aoc.Data.fetch_by_line(day=2, year=2020)
a = b = 0
for line in data:
    count, letter, password = line.split()
    letter = letter[:-1]
    low, high = map(int, count.split('-'))
    if low <= password.count(letter) <= high:
        a += 1
    if (password[low - 1] == letter) ^ (password[high - 1] == letter):
        b += 1
aoc.print_ans('2a', a)
aoc.print_ans('2b', b)
