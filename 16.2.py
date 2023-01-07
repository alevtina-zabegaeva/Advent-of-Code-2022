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


    T = 26

    # filename = '16.1test.txt'
    filename = '16.1input.txt'

    valves = {}
    flow_rates = {}
    with open(filename) as f:
        for line in f:
            name, *names = re.findall('[A-Z]{2}', line)
            flow_rate = int(re.findall('\d+', line)[0])
            valves[name] = set(names)
            flow_rates[name] = flow_rate

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
            for next_v in valves_dist[way[0][-1]]:
                if next_v not in way[0]:
                    if (next_t := way[1] + valves_dist[way[0][-1]][next_v]) < T:
                        next_released_pressure = way[2] + flow_rates[next_v] * (T - next_t)
                        next_ways.append([way[0] + [next_v], next_t, next_released_pressure])
            closed_ways.append(way)
        ways = next_ways
    
    closed_ways_lst = []
    closed_ways_len = []
    for closed_way in closed_ways:
        closed_way_set = set(closed_way[0][1:])
        if closed_way_set in closed_ways_lst:
            ind = closed_ways_lst.index(closed_way_set)
            closed_ways_len[ind] = max(closed_ways_len[ind], closed_way[2])
        else:
            closed_ways_lst.append(closed_way_set)
            closed_ways_len.append(closed_way[2])
    
    max2 = 0
    for i in range(l := len(closed_ways_lst)):
        for j in range(i + 1, l):
            if closed_ways_lst[i].isdisjoint(closed_ways_lst[j]):
                if max2 < (s := closed_ways_len[i] + closed_ways_len[j]):
                    max2 = s
                    max_w1, max_w2 = closed_ways_lst[i], closed_ways_lst[j]

    print(max2, max_w1, max_w2)


if __name__ == '__main__':
    main()
