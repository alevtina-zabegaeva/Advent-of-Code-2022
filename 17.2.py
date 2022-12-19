from itertools import cycle


def main():
    def highest_rock(chamber):
        return max(max(chamber, key=lambda item: max(item)))

    
    def loc_rock(loc, rock):
        return tuple((r[0] + loc[0], r[1] + loc[1]) for r in rock)

    
    def turn(rock, x=0, y=0):
        return tuple((r[0] + x, r[1] + y) for r in rock)
    

    def check(rock, chamber):
        for r in rock:
            if r[0] < 0 or r[0] >= len(chamber) or r[1] in chamber[r[0]]:
                return False
        return True


    def draw(chamber, rock):
        y_max = max(highest_rock(chamber), max(rock, key=lambda item: item[1])[1])
        for y in range(y_max, -1, -1):
            for x in range(len(chamber)):
                if y in chamber[x]:
                    print('#', end='')
                elif (x, y) in rock:
                    print('@', end='')
                else:
                    print('.', end='')
            print()
        print()


    def start_period(diff_heights, max_len):
        for start in range(1, max_len // 4):
            for p in range(10, max_len // 4):
                if diff_heights[start:start + p] == diff_heights[start + p:start + 2 * p] == diff_heights[start + 2 * p:start + 3 * p]:
                    return start, p


    # filename = '17.1test.txt'
    filename = '17.1input.txt'

    with open(filename) as f:
        winds = iter(cycle(f.readline()))

    rocks = iter(cycle((((0, 0), (1, 0), (2, 0), (3, 0)),
                        ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
                        ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
                        ((0, 0), (0, 1), (0, 2), (0, 3)),
                        ((0, 0), (1, 0), (0, 1), (1, 1)))))
    '''
    ####

    .#.
    ###
    .#.

    ..#
    ..#
    ###

    #
    #
    #
    #

    ##
    ##
    '''

    chamber = [{0}, {0}, {0}, {0}, {0}, {0}, {0}]
    i = 0
    j = 0
    max_len = 15000
    N = 1000000000000
    heights = [0]
    diff_heights = [0]
    while i < max_len:
        rock = next(rocks)
        loc = (2, highest_rock(chamber) + 4)
        cur = loc_rock(loc, rock)
        while True:
            wind = next(winds)
            j += 1
            if wind == '<':
                cur_next = turn(cur, x=-1)
            else:
                cur_next = turn(cur, x=1)
            if check(cur_next, chamber):
                cur = cur_next
            cur_next = turn(cur, y=-1)
            if check(cur_next, chamber):
                cur = cur_next
            else:
                for r in cur:
                    chamber[r[0]].add(r[1])
                i += 1
                break
        heights.append(highest_rock(chamber))
        diff_heights.append(heights[-1] - heights[-2])
       
    # draw(chamber, cur)
    start, period = start_period(diff_heights, max_len)
    print(start, period)
    periodic = N - start
    print(periodic // period * sum(diff_heights[start:start + period]) + heights[periodic % period + start])


if __name__ == '__main__':
    main()
