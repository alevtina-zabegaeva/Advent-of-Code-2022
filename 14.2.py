def main():
    def draw_map(x_min=494, y_min=0, x_max=503, y_max=9):
        for y in range(y_min, y_max + 1):
            for x in range(x_min, x_max + 1):
                if (x, y) in stones:
                    print('#', end='')
                elif (x, y) in sands:
                    print('o', end='')
                else:
                    print('.', end='')
            print()


    # filename = '14.1test.txt'
    filename = '14.1input.txt'

    stones_coords = []
    with open(filename) as f:
        for line in f:
            line = line.strip().split(' -> ')
            stones_coords.append([tuple(map(int, elm.split(','))) for elm in line])

    stones = set()
    for stone_coords in stones_coords:
        for i in range(1, len(stone_coords)):
            diff0, diff1 = stone_coords[i][0] - stone_coords[i - 1][0], stone_coords[i][1] - stone_coords[i - 1][1]
            diff = (0, diff1 // abs(diff1)) if diff0 == 0 else (diff0 // abs(diff0), 0)
            for j in range(max(abs(diff0), abs(diff1)) + 1):
                stones.add((stone_coords[i - 1][0] + diff[0] * j, stone_coords[i - 1][1] + diff[1] * j))

    x_min, x_max = min(stones)[0], max(stones)[0]
    y_min, y_max = 0, max(stones, key=lambda item: item[1])[1] + 2

    sands = set()
    stop = False
    while not stop:
        cur_sand = (500, 0)
        while True:
            if cur_sand[1] == y_max - 1:
                sands.add(cur_sand)
                break
            if (cur_sand[0], cur_sand[1] + 1) in sands or (cur_sand[0], cur_sand[1] + 1) in stones:
                if (cur_sand[0] - 1, cur_sand[1] + 1) in sands or (cur_sand[0] - 1, cur_sand[1] + 1) in stones:
                    if (cur_sand[0] + 1, cur_sand[1] + 1) in sands or (cur_sand[0] + 1, cur_sand[1] + 1) in stones:
                        sands.add(cur_sand)
                        if cur_sand == (500, 0):
                            stop = True
                        break
                    else:
                        cur_sand = (cur_sand[0] + 1, cur_sand[1] + 1)
                else:
                    cur_sand = (cur_sand[0] - 1, cur_sand[1] + 1)
            else:
                cur_sand = (cur_sand[0], cur_sand[1] + 1)


    draw_map(x_min - 65, y_min, x_max + 65, y_max)
    print(len(sands))


if __name__ == '__main__':
    main()
