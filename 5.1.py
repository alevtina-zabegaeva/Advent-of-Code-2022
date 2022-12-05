import re

def move(stacks, number, stack1, stack2):
    stack1 -= 1
    stack2 -= 1
    for _ in range(number):
        stacks[stack2].append(stacks[stack1].pop())

# filename = '5.1test.txt'
filename = '5.1input.txt'

table = []
procedures = []
with open(filename) as f:
    while True:
        line = f.readline()[:-1]
        if not line:
            break
        table.append(list(line[1::4]))
    table.pop()

    while True:
        line = f.readline().strip()
        if not line:
            break
        procedures.append(tuple(map(int, re.findall('\d+', line))))

table = table[::-1]
table = [row for row in zip(*table)]

stacks = []
for stack in table:
    stacks.append([s for s in stack if s != ' '])

for procedure in procedures:
    move(stacks, *procedure)

for stack in stacks:
    print(stack[-1], end='')
print()
