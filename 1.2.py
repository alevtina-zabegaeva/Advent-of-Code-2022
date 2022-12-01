import numpy as np

filename = '1.1input.txt'

calories_general = []
calories = []
with open(filename) as f:
    for line in f:
        if line != "\n":
            calories.append(int(line.strip()))
        else:
            calories_general.append(calories)
            calories = []

n = 3
calories = np.fromiter((sum(elf) for elf in calories_general), int, count = len(calories_general))
partitioned_array = np.partition(calories, len(calories) - n)
print(sum(partitioned_array[-3:]))
