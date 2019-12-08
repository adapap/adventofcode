from typing import List
class Op:
    ADD = 1
    MUL = 2
    INP = 3
    OUT = 4
    JNZ = 5
    JEZ = 6
    JLT = 7
    JEQ = 8
    STP = 99
class Intcode:
    def __init__(self, values: List[int]):
        self.values = values
    
    @classmethod
    def from_csv(cls, data):
        """Creates an Intcode process from CSV data (4,5,10,0,2)"""
        return cls(list(map(int, data.split(','))))
        
    def evaluate(self, inputs: List[int]):
        """Evaluates Intcode instructions while providing external input"""
        pos = 0
        values = self.values
        while True:
            ins = str(values[pos]).zfill(5)
            a, b, c, op = map(int, (*ins[:3], ins[-2:]))
            if op == Op.ADD:
                x, y, z = values[pos + 1:pos + 4]
                values[z] = (x if c else values[x]) + (y if b else values[y])
                pos += 4
            elif op == Op.MUL:
                x, y, z = values[pos + 1:pos + 4]
                values[z] = (x if c else values[x]) * (y if b else values[y])
                pos += 4
            elif op == Op.INP:
                n = next(inputs)
                x = values[pos + 1]
                values[x] = n
                pos += 2
            elif op == Op.OUT:
                x = values[pos + 1]
                out = x if c else values[x]
                if out:
                    return out
                pos += 2
            elif op == Op.JNZ:
                x, y = values[pos + 1:pos + 3]
                if (x if c else values[x]) != 0:
                    pos = y if b else values[y]
                else:
                    pos += 3
            elif op == Op.JEZ:
                x, y = values[pos + 1:pos + 3]
                if (x if c else values[x]) == 0:
                    pos = y if b else values[y]
                else:
                    pos += 3
            elif op == Op.JLT:
                x, y, z = values[pos + 1:pos + 4]
                if (x if c else values[x]) < (y if b else values[y]):
                    values[z] = 1
                else:
                    values[z] = 0
                pos += 4
            elif op == Op.JEQ:
                x, y, z = values[pos + 1:pos + 4]
                if (x if c else values[x]) == (y if b else values[y]):
                    values[z] = 1
                else:
                    values[z] = 0
                pos += 4
            elif op == Op.STP:
                break
            else:
                raise ValueError('No-op:', op)
        return 0