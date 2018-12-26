with open('input.txt') as f:
    data = f.readlines()

disks = {}
root = None

class Disk:
    def __init__(self, weight=0, children=[], parent=None):
        self.weight = weight
        self.children = children
        self.parent = parent

    def __repr__(self):
        return f'{self.children}>'

for line in data:
    values = line.strip().split(' ')
    disk_name, weight = values[:2]
    if root is None:
        root = disk_name
    weight = int(weight[1:-1])
    if disk_name in disks:
        disks[disk_name].weight = weight
    else:
        disks[disk_name] = Disk(weight=weight)
    if len(values) > 3:
        children = ''.join(values[3:]).split(',')
        for child in children:
            if child in disks:
                disks[child].parent = disk_name
            else:
                disks[child] = Disk(parent=disk_name)
        disks[disk_name].children = children

while disks[root].parent != None:
    root = disks[root].parent
print(f'Day 7a: {root}')

def find_weight(node):
    total = [find_weight(disks[child]) for child in node.children]
    if len(set(total)) > 1:
        diff = abs(max(total) - min(total))
        print(f'Day 7b: {diff}')
    return node.weight + sum(total)
find_weight(disks[root])