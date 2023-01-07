import itertools


def main():
    def neighbours(x, y, z):
        return ((x - 1, y, z), (x + 1, y, z),
                (x, y - 1, z), (x, y + 1, z),
                (x, y, z - 1), (x, y, z + 1))


    # filename = '18.1test.txt'
    filename = '18.1input.txt'

    with open(filename) as f:
        droplets = [tuple(map(int, line.rstrip().split(','))) for line in f]

    min_coord = [min(droplets, key=lambda item: item[i])[i] for i in range(3)]
    max_coord = [max(droplets, key=lambda item: item[i])[i] for i in range(3)]
    
    outer_drops = set((x, y, z) for x in (min_coord[0] - 1, max_coord[0] + 1)
                                for y in range(min_coord[1] - 1, max_coord[1] + 2)
                                for z in range(min_coord[2] - 1, max_coord[2] + 2))
    outer_drops |= set((x, y, z) for y in (min_coord[1] - 1, max_coord[1] + 1)
                                 for z in range(min_coord[2] - 1, max_coord[2] + 2)
                                 for x in range(min_coord[0] - 1, max_coord[0] + 2))
    outer_drops |= set((x, y, z) for z in (min_coord[2] - 1, max_coord[2] + 1)
                                 for x in range(min_coord[0] - 1, max_coord[0] + 2)
                                 for y in range(min_coord[1] - 1, max_coord[1] + 2))

    outer_border = outer_drops
    while len(outer_border) > 0:
        next_border = set()
        for drop in outer_border:
            for neighbour in neighbours(*drop):
                if (neighbour not in droplets and neighbour not in outer_drops and
                    min_coord[0] <= neighbour[0] <= max_coord[0] and
                    min_coord[1] <= neighbour[1] <= max_coord[1] and
                    min_coord[2] <= neighbour[2] <= max_coord[2]):
                    next_border.add(neighbour)
        outer_border = next_border
        outer_drops |= outer_border

    delta = [max_coord[i] - min_coord[i] + 3 for i in range(3)]

    sides = 6 * len(outer_drops) - 2 * (delta[0] * delta[1] + delta[1] * delta[2] + delta[2] * delta[0])
    for drop in outer_drops:
        for neighbour in neighbours(*drop):
            if neighbour in outer_drops:
                sides -= 1
    print(sides)


if __name__ == '__main__':
    main()
