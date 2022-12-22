import re
import math
import copy


def main():
    T = 24

    # filename = '19.1test.txt'
    filename = '19.1input.txt'

    blueprients = []
    with open(filename) as f:
        for line in f:
            numbers = list(map(int, re.findall('\d+', line)[1:]))
            blueprients.append(((numbers[0], 0, 0, 0), (numbers[1], 0, 0, 0), (numbers[2], numbers[3], 0, 0), (numbers[4], 0, numbers[5], 0)))

    max_geodes = []
    for costs in blueprients:
        print('Blueprint', len(max_geodes) + 1)
        tree = [[[0], # robots
                0, # time
                [0, 0, 0, 0], # resourses
                [1, 0, 0, 0] # robots
                ]]
        max_geodes.append(0)
        finished_tree = []
        max_robots = (max(costs[0][0], costs[1][0], costs[2][0], costs[3][0]),
                         costs[2][1],
                         costs[3][2])        
        while len(tree) > 0:
            next_tree = []
            for way in tree:
                for r in range(4):
                    if r in (0, 1, 2) and way[3][r] == max_robots[r]:
                        continue
                    if any([cost > 0 and way[3][i] == 0 for i, cost in enumerate(costs[r])]):
                        continue
                    delta_t = 1 + max([math.ceil((cost - way[2][i]) / way[3][i]) if cost > way[2][i] else 0 for i, cost in enumerate(costs[r])])
                    if (time := way[1] + delta_t) >= T:
                        continue
                    way0 = way[0] + [r]
                    robots = way[3].copy()
                    robots[r] += 1
                    resourses = [way[2][i] + delta_t * rob - costs[r][i] for i, rob in enumerate(way[3])]
                    # TODO wenn zu lange um max_geode zu bekommen -> nicht append
                    if (resourses[3] + (T-time)/2 * (2 * robots[3] + (T-time) - 1)) > max_geodes[-1]:
                        next_tree.append([way0, time, resourses, robots])
                if way[3][3] != 0:
                    delta_t = T - way[1]
                    way0 = way[0].copy()
                    robots = way[3].copy()
                    resourses = [way[2][i] + delta_t * rob for i, rob in enumerate(way[3])]
                    if resourses[3] > max_geodes[-1]:
                        finished_tree = [way0, T, resourses, robots]
                        max_geodes[-1] = resourses[3]
            tree = copy.deepcopy(next_tree)
            print(f'Current: {len(tree)}, max: {max_geodes[-1]}, {finished_tree}')
        print()
    print(max_geodes)
    print(sum([geodes * (i + 1) for i, geodes in enumerate(max_geodes)]))




if __name__ == '__main__':
    main()
