def priority(letter):
    code = ord(letter)
    if code > 90:
        return code - 96
    else:
        return code - 65 + 27


# filename = '3.1test.txt'
filename = '3.1input.txt'

with open(filename) as f:
    rucksacks = [set(line.strip()) for line in f]

common_items = []
for i in range(0, len(rucksacks) - 2, 3):
    common_items.append((rucksacks[i].intersection(rucksacks[i + 1], rucksacks[i + 2])).pop())

priorities = [priority(common_item) for common_item in common_items]
print(sum(priorities))
