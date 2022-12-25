import re
import copy


def main():
    def neighbours(x, y):
        return ((x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y - 1))

    
    def neighbours3(x, y, step):
        elements = [((x - 1, y - 1), (x - 1, y), (x - 1, y + 1)), # N
                    ((x + 1, y + 1), (x + 1, y), (x + 1, y - 1)), # S
                    ((x + 1, y - 1), (x, y - 1), (x - 1, y - 1)), # W
                    ((x - 1, y + 1), (x, y + 1), (x + 1, y + 1))  # E
                    ]
        return [elements[s % 4] for s in range(step, step + 4)]
    
    def draw():
        x_min = min(elves)[0]   
        x_max = max(elves)[0]
        y_min = min(elves, key=lambda item: item[1])[1]   
        y_max = max(elves, key=lambda item: item[1])[1]
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                if (x, y) in elves:
                    print('#', end='')
                else:
                    print('.', end='')
            print()


    # filename = '23.1test.txt'
    # filename = '23.1test2.txt'
    filename = '23.1input.txt'

    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    elves = []
    with open(filename) as f:
        for i, line in enumerate(f):
            for m in re.finditer('#', line):
                elves.append((i, m.start(0)))
    quantity = len(elves)
    draw()
    print()

    step = 0
    while True:
        elves_next = []
        for elf in elves:
            if all(neighbour not in elves for neighbour in neighbours(*elf)):
                elves_next.append(elf)
            else:
                for i, elements in enumerate(neighbours3(*elf, step)):
                    if all(neighbour not in elves for neighbour in elements):
                        elves_next.append(tuple(map(sum, zip(elf, dir[(step + i) % 4]))))
                        break
                else:
                    elves_next.append(elf)
        elves_nextstop = elves_next.copy()
        for i, elf in enumerate(elves_next[:-1]):
            for j in range(i + 1, quantity):
                if elf == elves_next[j]:
                    elves_nextstop[i] = elves[i]
                    elves_nextstop[j] = elves[j]
                    break
        step += 1
        if elves == elves_nextstop:
            break
        elves = elves_nextstop.copy()
    # draw()
    print(step)


if __name__ == '__main__':
    main()
