import re

# filename = '4.1test.txt'
filename = '4.1input.txt'

with open(filename) as f:
    assignments = tuple(tuple(map(int, re.split('[-,]', line.strip()))) for line in f)

counter = 0
for assignment in assignments:
    if assignment[1] < assignment[2] or assignment[3] < assignment[0]:
        counter += 1

print(len(assignments) - counter)
