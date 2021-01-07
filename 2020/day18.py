import aoc
import re

puzzle = aoc.Puzzle(day=18, year=2020)
PART_1 = PART_2 = 0
data = puzzle.fetch_by_line()
# data = """2 * 3 + (4 * 5)
# 5 + (8 * 3 + 9 + 3 * 4 * 3)
# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2""".split('\n')
def lex(expr):
    tokens = []
    num = ''
    while expr != '':
        char = expr[0]
        if char.isdigit():
            num += char
        elif not char.isdigit() and num != '':
            tokens.append(int(num))
            num = ''
        if char in '()+*':
            tokens.append(char)
        expr = expr[1:]
    if num != '':
        tokens.append(int(num))
    return tokens

class Parser:
    def __init__(self, tokens, adv=False):
        self.pos = 0
        self.tokens = tokens
        self.adv = adv
    
    @property
    def cur_token(self):
        return self.tokens[self.pos]

    def term(self):
        if not self.adv:
            node = self.parens()
            while self.pos < len(self.tokens) and self.cur_token in '+*':
                op = self.cur_token
                self.pos += 1
                node = (op, node, self.parens())
            return node
        else:
            node = self.factor()
            while self.pos < len(self.tokens) and self.cur_token == '*':
                op = self.cur_token
                self.pos += 1
                node = (op, node, self.factor())
            return node
    
    def factor(self):
        node = self.parens()
        while self.pos < len(self.tokens) and self.cur_token == '+':
            op = self.cur_token
            self.pos += 1
            node = (op, node, self.parens())
        return node
    
    def parens(self):
        if self.cur_token == '(':
            self.pos += 1
            expr = self.term()
            assert self.cur_token == ')'
            self.pos += 1
            return expr
        return self.number()
    
    def number(self):
        n = self.cur_token
        self.pos += 1
        return n

def eval_tree(tree):
    if type(tree) == int:
        return tree
    if tree[0] == '*':
        return eval_tree(tree[1]) * eval_tree(tree[2])
    if tree[0] == '+':
        return eval_tree(tree[1]) + eval_tree(tree[2])

for line in data:
    tokens = lex(line)
    p = Parser(tokens)
    tree = p.term()
    val = eval_tree(tree)
    PART_1 += val
# puzzle.submit(part=1, answer=PART_1)
for line in data:
    tokens = lex(line)
    p = Parser(tokens, adv=True)
    tree = p.term()
    val = eval_tree(tree)
    PART_2 += val
puzzle.submit(part=2, answer=PART_2)
