import aoc
from typing import Set

puzzle = aoc.Puzzle(day=8, year=2020)
PART_1 = PART_2 = None
data = puzzle.fetch_by_line()
# data = """nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6""".split('\n')
        
acc = 0
pc = 0
seen = set()
while pc < len(data):
    if pc in seen:
        PART_1 = acc
        break
    seen.add(pc)
    op, arg = data[pc].split(' ')
    if op == 'acc':
        acc += int(arg)
    elif op == 'nop':
        pass
    elif op == 'jmp':
        pc += int(arg)
        continue
    pc += 1
# puzzle.submit(part=1, answer=PART_1)

changed: Set[int] = set()
def run_program():
    pc = 0
    acc = 0
    seen = set()
    switched = False
    while pc < len(data):
        if pc in seen:
            break
        seen.add(pc)
        op, arg = data[pc].split(' ')
        if op == 'acc':
            acc += int(arg)
        elif op == 'nop':
            if pc not in changed and not switched:
                changed.add(pc)
                switched = True
                pc += int(arg)
        elif op == 'jmp':
            if pc not in changed and not switched:
                changed.add(pc)
                switched = True
            else:
                pc += int(arg)
                continue
        pc += 1
    else:
        global PART_2
        PART_2 = acc
while PART_2 is None:
    run_program()
print(PART_2)

# puzzle.submit(part=2, answer=PART_2)
