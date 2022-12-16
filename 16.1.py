import re


def main():
    def map_valves(cur_valve):
        map_v = {}
        for valve in valves:
            if valve != cur_valve and flow_rates[valve] != 0:
                map_v[valve] = shortest_dist(cur_valve, valve) + 1
        return map_v
    

    def shortest_dist(valve1, valve2):
        visited = set((valve1,))
        next_valves = valves[valve1]
        d = 0
        while d < len(valves):
            d += 1
            if valve2 in next_valves:
                return d
            visited |= set(next_valves)
            nextnext_valves = set()
            for valve in next_valves:
                nextnext_valves |= valves[valve]
            next_valves = nextnext_valves - visited


    T = 30

    # filename = '16.1test.txt'
    filename = '16.1input.txt'

    valves = {}
    flow_rates = {}
    opened_valves = set()
    with open(filename) as f:
        for line in f:
            name, *names = re.findall('[A-Z]{2}', line)
            flow_rate = int(re.findall('\d+', line)[0])
            valves[name] = set(names)
            flow_rates[name] = flow_rate
    print(f'Valves ({len(valves)}): {valves}')
    print('Flow rates', flow_rates)
    print()

    loc = 'AA'

    valves_dist = {loc: map_valves(loc)}
    for valve in valves:
        if flow_rates[valve] != 0:
            valves_dist[valve] = map_valves(valve)

    ways = [[[loc], 0, 0]]
    closed_ways = []
    while len(ways) > 0:
        next_ways = []
        for way in ways:
            exist_next = False
            for next_v in valves_dist[way[0][-1]]:
                if next_v not in way[0]:
                    if (next_t := way[1] + valves_dist[way[0][-1]][next_v]) < T:
                        next_released_pressure = way[2] + flow_rates[next_v] * (T - next_t)
                        next_ways.append([way[0] + [next_v], next_t, next_released_pressure])
                        exist_next = True
            if not exist_next:
                closed_ways.append(way)
        ways = next_ways

    # print(closed_ways)
    print(max(closed_ways, key=lambda item: item[2]))


if __name__ == '__main__':
    main()
