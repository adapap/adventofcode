registers = None
def addr(a, b):
    return registers[a] + registers[b]
def addi(a, b):
    return registers[a] + b

def mulr(a, b):
    return registers[a] * registers[b]
def muli(a, b):
    return registers[a] * b

def banr(a, b):
    return registers[a] & registers[b]
def bani(a, b):
    return registers[a] & b

def borr(a, b):
    return registers[a] | registers[b]
def bori(a, b):
    return registers[a] | b

def setr(a, b):
    return registers[a]
def seti(a, b):
    return a

def gtir(a, b):
    return 1 if a > registers[b] else 0
def gtri(a, b):
    return 1 if registers[a] > b else 0
def gtrr(a, b):
    return 1 if registers[a] > registers[b] else 0

def eqir(a, b):
    return 1 if a == registers[b] else 0
def eqri(a, b):
    return 1 if registers[a] == b else 0
def eqrr(a, b):
    return 1 if registers[a] == registers[b] else 0