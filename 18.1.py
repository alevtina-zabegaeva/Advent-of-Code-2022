def main():
    def neighbours(x, y, z):
        return ((x - 1, y, z), (x + 1, y, z),
                (x, y - 1, z), (x, y + 1, z),
                (x, y, z - 1), (x, y, z + 1))


    # filename = '18.1test.txt'
    filename = '18.1input.txt'

    with open(filename) as f:
        droplets = [tuple(map(int, line.rstrip().split(','))) for line in f]
    # print(f'Droplets: {droplets}')

    sides = 6 * len(droplets)
    for drop in droplets:
        for neighbour in neighbours(*drop):
            if neighbour in droplets:
                sides -= 1
    print(sides)

if __name__ == '__main__':
    main()
