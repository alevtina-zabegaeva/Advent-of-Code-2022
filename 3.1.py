def priority(letter):
    code = ord(letter)
    if code > 90:
        return code - 96
    else:
        return code - 65 + 27


# filename = '3.1test.txt'
filename = '3.1input.txt'

rucksacks = []
with open(filename) as f:
    for line in f:
        line = line.strip()
        size = len(line) // 2
        rucksacks.append((set(line[:size]), set(line[size:])))

one_items = [(rucksack[0] & rucksack[1]).pop() for rucksack in rucksacks]
priorities = [priority(one_item) for one_item in one_items]
print(sum(priorities))
