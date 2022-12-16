import re


def main():
    
    # Y = 10
    Y = 2000000
    # filename = '15.1test.txt'
    filename = '15.1input.txt'

    sensors = []
    beacons = []
    with open(filename) as f:
        for line in f:
            x1, y1, x2, y2 = list(map(int, re.findall('-?\d+', line)))
            sensors.append((x1, y1))
            beacons.append((x2, y2))

    coverage = set()
    for i, sensor in enumerate(sensors):
        dist = abs(sensor[0] - beacons[i][0]) + abs(sensor[1] - beacons[i][1])
        # print(f'i = {i}, Distance = {dist}')
        if (diff := dist - abs(sensor[1] - Y)) >= 0:
            coverage |= set(range(sensor[0] - diff, sensor[0] + diff + 1))
    for beacon in set(beacons):
        if beacon[1] == Y:
            coverage.discard(beacon[0])
 
    print(len(coverage))


if __name__ == '__main__':
    main()
