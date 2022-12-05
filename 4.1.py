import re

# filename = '4.1test.txt'
filename = '4.1input.txt'

with open(filename) as f:
    assignments = tuple(tuple(map(int, re.split('[-,]', line.strip()))) for line in f)

counter = 0
for assignment in assignments:
    if (assignment[0] <= assignment[2] and assignment[1] >= assignment[3] or
        assignment[0] >= assignment[2] and assignment[1] <= assignment[3]):
        counter += 1

print(counter)
