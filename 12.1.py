import numpy as np

def main():
    def neighbours(ii, jj):
        neighbours_set = set()
        if ii - 1 >= 0:
            neighbours_set.add((ii - 1, jj))
        if jj - 1 >= 0:
            neighbours_set.add((ii, jj - 1))
        if ii + 1 < len_i:
            neighbours_set.add((ii + 1, jj))
        if jj + 1 < len_j:
            neighbours_set.add((ii, jj + 1))
        return neighbours_set


    def get_possible(heightmap, ii, jj):
        possible_set = set()
        cur_value = heightmap[ii, jj]
        for n_i, n_j in neighbours(ii, jj):
            if heightmap[n_i, n_j] - cur_value <= 1:
                possible_set.add((n_i, n_j))
        return possible_set
        

    # filename = '12.1test.txt'
    filename = '12.1input.txt'

    heightmap = []
    with open(filename) as f:
        for i, line in enumerate(f):
            if (j := line.find('S')) != -1:
                S_loc = (i, j)
                line = line[:j] + 'a' + line[j + 1:]
            if (j := line.find('E')) != -1:
                E_loc = (i, j)
                line = line[:j] + 'z' + line[j + 1:]
            heightmap.append(list(map(lambda x: ord(x) - ord('a'), list(line.rstrip()))))
    heightmap = np.array(heightmap)
    # print(heightmap)
    # print(S_loc, E_loc)

    current_loc = {S_loc}
    len_i, len_j = np.shape(heightmap)
    stepsmap = np.full_like(heightmap, len_i * len_j)
    step = 0
    stepsmap[S_loc] = step
    print(stepsmap)

    # for _ in range(30):
    while E_loc not in current_loc and step < len_i * len_j and len(current_loc) > 0:
        step += 1
        next_loc = set()
        for cur_l in current_loc:
            possible = get_possible(heightmap, *cur_l)
            for pos in possible:
                if stepsmap[pos] > step:
                    stepsmap[pos] = step
                    next_loc.add(pos)
        current_loc = next_loc
    print(stepsmap)
    print(stepsmap[E_loc])

if __name__ == '__main__':
    main()
