def main():
    # filename = '9.2test.txt'
    filename = '9.1input.txt'

    direction = {'R': (0, 1), 'U': (-1, 0), 'L': (0, -1), 'D': (1, 0)}
    motions = []
    with open(filename) as f:
        for line in f:
            line = line.rstrip().split()
            motions.append((*direction[line[0]], int(line[1])))

    l = 10
    current = [[0, 0] for _ in range(l)]
    places = {tuple(current[-1])}

    for motion in motions:
        for _ in range(motion[2]):
            current[0] = [current[0][i] + motion[i] for i in (0, 1)]
            for j in range(1, l):
                dist_h = current[j - 1][1] - current[j][1]
                dist_v = current[j - 1][0] - current[j][0]
                if not (abs(dist_v) < 2 and abs(dist_h) < 2):
                    if current[j][1] != current[j - 1][1]:
                        current[j][1] += dist_h // abs(dist_h)
                    if current[j][0] != current[j - 1][0]:
                        current[j][0] += dist_v // abs(dist_v)
            places.add(tuple(current[-1]))
        
    print(len(places))


if __name__ == '__main__':
    main()
