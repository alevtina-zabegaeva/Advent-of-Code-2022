import re


def main():
    
    # x_min, y_min, x_max, y_max = 0, 0, 20, 20
    x_min, y_min, x_max, y_max = 0, 0, 4000000, 4000000

    # filename = '15.1test.txt'
    filename = '15.1input.txt'

    sensors = []
    beacons = []
    with open(filename) as f:
        for line in f:
            x1, y1, x2, y2 = list(map(int, re.findall('-?\d+', line)))
            sensors.append((x1, y1))
            beacons.append((x2, y2))

    for y in range(y_min, y_max + 1):
        coverage = []
        for i, sensor in enumerate(sensors):
            dist = abs(sensor[0] - beacons[i][0]) + abs(sensor[1] - beacons[i][1])
            # print(f'i = {i}, Distance = {dist}')
            if (diff := dist - abs(sensor[1] - y)) >= 0:
                if (x1 := max(sensor[0] - diff, x_min)) <= (x2 := min(sensor[0] + diff, x_max)):
                    coverage.append((x1, x2))
        coverage.sort()
        cur_max = x_min - 1
        for interval in coverage:
            if interval[0] > cur_max + 1:
                print(f'({cur_max + 1}, {y}) => tuning frequency = {(cur_max + 1) * 4000000 + y}')
                break
            cur_max = max(cur_max, interval[1])


if __name__ == '__main__':
    main()
