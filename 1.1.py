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

calories = max([sum(elf) for elf in calories_general])
print(calories)
