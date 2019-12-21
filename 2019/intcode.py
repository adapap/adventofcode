from collections import defaultdict, deque
from typing import List
class Op:
    ADD = 1 # Add two values
    MUL = 2 # Multiply two values
    INP = 3 # Store input value
    OUT = 4 # Output value
    JNZ = 5 # Jump if not equal to zero
    JEZ = 6 # Jump if equal to zero
    JLT = 7 # Jump if less than zero
    JEQ = 8 # Jump if equal
    ARB = 9 # Adjust relative base
    STP = 99 # Halt program

class Parameter:
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2

class Intcode:
    def __init__(self, values: List[int], pos: int=0):
        self.values = defaultdict(int)
        self.values.update({i: values[i] for i in range(len(values))})
        self.pos = pos
        self.inputs = deque()
        self.outputs = deque()
        self.relative_base = 0
        self.halted = False
    
    @classmethod
    def from_csv(cls, data):
        """Creates an Intcode process from CSV data (4,5,10,0,2)"""
        return cls(list(map(int, data.split(','))))
    
    @classmethod
    def from_data(cls, data, pos=0):
        """Creates an Intcode process from an integer iterable"""
        return cls(data, pos)
    
    def add_inputs(self, *inputs):
        """Adds inputs to the input stream"""
        self.inputs.extend(inputs)
    
    def get_output(self, n=1, all_output=False):
        """Gets next n outputs"""
        if not self.outputs:
            return []
        if all_output:
            return list(self.outputs)
        if n == 1:
            return self.outputs.popleft()
        return [self.outputs.popleft() for _ in range(n)]
    
    def get_parameter(self, n, p, write=False):
        """Gets a parameter based on its mode."""
        if p == Parameter.POSITION:
            if write:
                return n
            return self.values[n]
        elif p == Parameter.IMMEDIATE:
            return n
        elif p == Parameter.RELATIVE:
            if write:
                return n + self.relative_base
            return self.values[n + self.relative_base]
        else:
            raise ValueError('Invalid parameter mode:', p)
    
    def get_values(self, n=1):
        """Returns the next n parameters, from 1-3"""
        a = self.values[self.pos + 1]
        b = self.values[self.pos + 2]
        c = self.values[self.pos + 3]
        if n == 1:
            return a
        elif n == 2:
            return a, b
        elif n == 3:
            return a, b, c
        
    def evaluate(self):
        """Evaluates Intcode instructions handling input and output streams"""
        while True:
            ins = str(self.values[self.pos]).zfill(5)
            mode3, mode2, mode1, op = map(int, (*ins[:3], ins[-2:]))
            if op == Op.ADD:
                p1, p2, p3 = self.get_values(3)
                self.values[self.get_parameter(p3, mode3, write=True)] = self.get_parameter(p1, mode1) + self.get_parameter(p2, mode2)
                self.pos += 4
            elif op == Op.MUL:
                p1, p2, p3 = self.get_values(3)
                self.values[self.get_parameter(p3, mode3, write=True)] = self.get_parameter(p1, mode1) * self.get_parameter(p2, mode2)
                self.pos += 4
            elif op == Op.INP:
                if not self.inputs:
                    break
                n = self.inputs.popleft()
                p1 = self.get_values(1)
                self.values[self.get_parameter(p1, mode1, write=True)] = n
                self.pos += 2
            elif op == Op.OUT:
                p1 = self.get_values(1)
                self.outputs.append(self.get_parameter(p1, mode1))
                self.pos += 2
            elif op == Op.JNZ:
                p1, p2 = self.get_values(2)
                if self.get_parameter(p1, mode1) != 0:
                    self.pos = self.get_parameter(p2, mode2)
                else:
                    self.pos += 3
            elif op == Op.JEZ:
                p1, p2 = self.get_values(2)
                if self.get_parameter(p1, mode1) == 0:
                    self.pos = self.get_parameter(p2, mode2)
                else:
                    self.pos += 3
            elif op == Op.JLT:
                p1, p2, p3 = self.get_values(3)
                if self.get_parameter(p1, mode1) < self.get_parameter(p2, mode2):
                    self.values[self.get_parameter(p3, mode3, write=True)] = 1
                else:
                    self.values[self.get_parameter(p3, mode3, write=True)] = 0
                self.pos += 4
            elif op == Op.JEQ:
                p1, p2, p3 = self.get_values(3)
                if self.get_parameter(p1, mode1) == self.get_parameter(p2, mode2):
                    self.values[self.get_parameter(p3, mode3, write=True)] = 1
                else:
                    self.values[self.get_parameter(p3, mode3, write=True)] = 0
                self.pos += 4
            elif op == Op.ARB:
                p1 = self.get_values(1)
                self.relative_base += self.get_parameter(p1, mode1)
                self.pos += 2
            elif op == Op.STP:
                self.pos += 1
                self.halted = True
                break
            else:
                raise ValueError('Invalid opcode:', op)