import math
import re


def main():

    # filename = '22.1test.txt'
    filename = '22.1input.txt'

    dir_dict = ((0, 1), (1, 0), (0, -1), (-1, 0))
    rotation_dict = {'R': 1, 'L': -1}

    walls = set()
    row_borders = []
    with open(filename) as f:
        i = 0
        while (line := f.readline().rstrip()) != '':
            for m in re.finditer('#', line):
                walls.add((i, m.start(0)))
            row_borders.append((re.search('[.#]', line).start(), len(line) - 1))
            i += 1
        way = [int(elm) if elm.isdigit() else elm for elm in re.findall('\d+|[LR]', f.readline())]
    
    row_max_len = max(row_borders, key=lambda item: item[1])[1] + 1
    column_borders = ['']*row_max_len
    column_len = len(row_borders)
    edge = math.gcd(row_max_len, column_len)
    for column in range(row_max_len):
        row, row1, row2 = 0, 0, column_len - 1
        while row < column_len:
            if row_borders[row][0] <= column <= row_borders[row][1]:
                row1 = row
                break
            row += 1
        while row < column_len - 1:
            row += 1
            if column < row_borders[row][0] or column > row_borders[row][1]:
                row2 = row - 1
                break    
        column_borders[column] = (row1, row2)

    cur_loc = [0, row_borders[0][0]]
    cur_dir = 0
    for w in way:
        if isinstance(w, int):
            for _ in range(w):
                next_loc = list(map(sum, zip(cur_loc, dir_dict[cur_dir])))
                next_dir = cur_dir
                if next_loc[1] == row_max_len:
                    next_dir = 2
                    next_loc[0] = edge * 3 - cur_loc[0] - 1
                    next_loc[1] = edge * 2 - 1
                elif next_loc[0] == column_len:
                    next_loc[0] = 0
                    next_loc[1] = edge * 2 + cur_loc[1]
                elif next_loc[0] == -1:
                    if cur_loc[1] >= 2 * edge:
                        next_loc[0] = edge * 4 - 1
                        next_loc[1] = cur_loc[1] - edge * 2
                    else:
                        next_dir = 0
                        next_loc[0] = edge * 2 + cur_loc[1]
                        next_loc[1] = 0
                elif next_loc[1] == -1:
                    if cur_loc[0] >= 3 * edge:
                        next_dir = 1
                        next_loc[0] = 0
                        next_loc[1] = cur_loc[0] - edge * 2
                    else:
                        next_dir = 0
                        next_loc[0] = edge * 3 - cur_loc[0] - 1
                        next_loc[1] = edge
                elif next_loc[0] == 3 * edge and next_loc[1] >= edge and cur_dir == 1:
                    next_dir = 2
                    next_loc[0] = edge * 2 + cur_loc[1]
                    next_loc[1] = edge - 1
                elif next_loc[0] == edge and next_loc[1] >= 2 * edge and cur_dir == 1:
                    next_dir = 2
                    next_loc[0] = cur_loc[1] - edge
                    next_loc[1] = edge * 2 - 1
                elif next_loc[1] == edge * 2:
                    if cur_loc[0] >= 2 * edge:
                        next_dir = 2
                        next_loc[0] = edge * 3 - cur_loc[0] - 1
                        next_loc[1] = edge * 3 - 1
                    elif cur_loc[0] >= edge and cur_dir == 0:
                        next_dir = 3
                        next_loc[0] = edge - 1
                        next_loc[1] = edge + cur_loc[0]
                elif next_loc[1] == edge and next_loc[0] >= edge * 3 and cur_dir == 0:
                    next_dir = 3
                    next_loc[0] = edge * 3 - 1
                    next_loc[1] = cur_loc[0] - edge * 2
                elif next_loc[1] == edge - 1:
                    if cur_loc[0] < edge:
                        next_dir = 0
                        next_loc[0] = edge * 3 - cur_loc[0] - 1
                        next_loc[1] = 0
                    elif cur_loc[0] < 2 * edge and cur_dir == 2:
                        next_dir = 1
                        next_loc[0] = edge * 2
                        next_loc[1] = cur_loc[0] - edge
                elif next_loc[0] == edge * 2 - 1 and next_loc[1] < edge and cur_dir == 3:
                    next_dir = 0
                    next_loc[0] = edge + cur_loc[1]
                    next_loc[1] = edge
                if tuple(next_loc) in walls:
                    break
                cur_loc = next_loc
                cur_dir = next_dir
        else:
            cur_dir = (cur_dir + rotation_dict[w]) % 4

    print(cur_loc, cur_dir)
    print(1000 * (cur_loc[0] + 1) + 4 * (cur_loc[1] + 1) + cur_dir)


if __name__ == '__main__':
    main()
