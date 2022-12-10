def main():
    # filename = '9.1test.txt'
    filename = '9.1input.txt'

    direction = {'R': (0, 1), 'U': (-1, 0), 'L': (0, -1), 'D': (1, 0)}
    motions = []
    with open(filename) as f:
        for line in f:
            line = line.rstrip().split()
            motions.append((*direction[line[0]], int(line[1])))

    current_head, current_tail = [0, 0], [0, 0]
    places = {tuple(current_tail)}

    for motion in motions:
        for _ in range(motion[2]):
            current_head = [current_head[i] + motion[i] for i in (0, 1)]
            dist_h = current_head[1] - current_tail[1]
            dist_v = current_head[0] - current_tail[0]
            if not (abs(dist_v) < 2 and abs(dist_h) < 2):
                if current_tail[1] != current_head[1]:
                    current_tail[1] += dist_h // abs(dist_h)
                if current_tail[0] != current_head[0]:
                    current_tail[0] += dist_v // abs(dist_v)
                places.add(tuple(current_tail))
    
    print(len(places))


if __name__ == '__main__':
    main()
