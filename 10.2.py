def main():
    def draw_pixel(c, x):
        return '#' if abs((c - 1) % 40 - x) < 2 else '.'


    # filename = '10.1test.txt'
    filename = '10.1input.txt'

    with open(filename) as f:
        program = [int(line.rstrip().split()[1]) if line[0] == 'a' else '' for line in f]
    
    cycle = 0
    x = 1
    picture = []

    for line in program:
        cycle += 1
        picture.append(draw_pixel(cycle, x))
        if line != '':
            cycle += 1
            picture.append(draw_pixel(cycle, x))
            x += line
    
    for i, p in enumerate(picture):
        print(p, end='')
        if (i + 1) % 40 == 0:
            print()

if __name__ == '__main__':
    main()
