"""Day 8: Memory Maneuver"""
from aoctools import Data, IntTuple, print_ans

data = Data.fetch(day=8, year=2018)
# data = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'

class Node:
    def __init__(self, child_nodes, entries, depth):
        self.child_nodes = child_nodes
        self.entries = entries
        self.depth = depth
        self.children = []
        self.metadata = []
    @property
    def datasum(self):
        return sum(self.metadata)
    
    def __repr__(self):
        return f'{self.depth}: {self.metadata}'

nums = list(IntTuple(*data.split()))
nodes = []

def make_tree(data, depth=0, parent=None):
    a, b = data[:2]
    # Base Case: No children -> Add node, return remaining data
    if a == 0:
        node = Node(a, b, depth)
        node.metadata = data[2:2 + b]
        nodes.append(node)
        return (data[2 + b:], node)
    else:
        # While there are children, loop through each and recurse process
        new_data = data[2:]
        has_children = a
        children = []
        while has_children:
            new_data, child = make_tree(new_data, depth + 1)
            has_children -= 1
            children.append(child)
        # Add remaining data once back in outer layer
        node = Node(a, b, depth)
        node.metadata = new_data[:b]
        nodes.append(node)
        for child in children:
            node.children.append(child)
        return (new_data[b:], node)

make_tree(nums)
total = sum(node.datasum for node in nodes)
print_ans('8a', total)

root = nodes[-1]
def find_value(node):
    if node.children == []:
        return sum(node.metadata)
    else:
        total = 0
        for i in node.metadata:
            if 1 <= i <= len(node.children):
                total += find_value(node.children[i - 1])
        return total

root_value = find_value(root)
print_ans('8b', root_value)