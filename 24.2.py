import re


def main():
    def neighbours(x, y):
        if (x, y) == (0, 1):
            return {(0, 1), (1, 1)}
        if (x, y) == (x_max, y_max - 1):
            return {(x_max, y_max - 1), (x_max - 1, y_max - 1)}
        all_n = {           (x - 1, y),
                 (x, y - 1),  (x, y), (x, y + 1),
                            (x + 1, y)}
        if x == 1 and y != 1:
            all_n.discard((x - 1, y))
        elif x == x_max - 1 and y != y_max - 1:
            all_n.discard((x + 1, y))
        if y == 1:
            all_n.discard((x, y - 1))
        elif y == y_max - 1:
            all_n.discard((x, y + 1))  
        return all_n

    
    def draw():
        print('#.' + '#' * (y_max - 1))
        for x in range(1, x_max):
            print('#', end='')
            for y in range(1, y_max):
                if (x, y) in blizzards_loc:
                    print('b', end='')
                else:
                    print('.', end='')
            print('#')
        print('#' * (y_max - 1) + '.#')
        print()


    def go(step, start, goal, blizzards_loc):
        cur = {start}
        while True:
            step += 1
            blizzards_loc_next = []
            for i, blizzard in enumerate(blizzards_loc):
                next_loc = tuple(map(sum, zip(blizzard, blizzards_dir[i])))
                if next_loc[0] == 0:
                    next_loc = (x_max - 1, next_loc[1])
                elif next_loc[0] == x_max:
                    next_loc = (1, next_loc[1])
                elif next_loc[1] == 0:
                    next_loc = (next_loc[0], y_max - 1)
                elif next_loc[1] == y_max:
                    next_loc = (next_loc[0], 1)
                blizzards_loc_next.append(next_loc)
            blizzards_loc = blizzards_loc_next.copy()
            cur_next = set()
            for loc in cur:
                for neighbour in neighbours(*loc):
                    if neighbour not in blizzards_loc:
                        if neighbour == goal:
                            print()
                            print(step)
                            return step, blizzards_loc
                        cur_next.add(neighbour)
            if len(cur_next) == 0:
                return -1, blizzards_loc
            cur = cur_next.copy()


    # filename = '24.1test2.txt'
    filename = '24.1input.txt'

    dir = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

    blizzards_loc = []
    blizzards_dir = []
    with open(filename) as f:
        for i, line in enumerate(f):
            for m in re.finditer('[<^v>]', line):
                blizzards_loc.append((i, m.start(0)))
                blizzards_dir.append(dir[m[0]])
        x_max = i
        y_max = len(line) - 1

    begin = (0, 1)
    end = (x_max, y_max - 1)
    draw()
    print(x_max, y_max)
    # print(blizzards_loc)
    # print(blizzards_dir)
    
    st, blizzards_loc = go(0, begin, end, blizzards_loc)
    st, blizzards_loc = go(st, end, begin, blizzards_loc)
    st, blizzards_loc = go(st, begin, end, blizzards_loc)


if __name__ == '__main__':
    main()
