import re

def main():

    # filename = '11.1test.txt'
    filename = '11.1input.txt'

    input = []
    with open(filename) as f:
        while (line := f.readline()):
            input.append({})
            # input[-1]['monkey'] = int(re.findall('\d+', line)[0])

            line = f.readline()
            input[-1]['items'] = list(map(int, re.findall('\d+', line)))

            line = f.readline()
            input[-1]['function'] = re.findall('old.+', line)[0]

            line = f.readline()
            input[-1]['test'] = int(re.findall('\d+', line)[0])

            line = f.readline()
            input[-1]['if_true'] = int(re.findall('\d+', line)[0])

            line = f.readline()
            input[-1]['if_false'] = int(re.findall('\d+', line)[0])

            line = f.readline()

    # print(input)
    monkey = [0] * len(input)
    for _ in range(20):
        for i, inp in enumerate(input):
            for old in inp['items']:
                old = eval(inp['function'])
                old = int(old / 3)
                if old % inp['test'] == 0:
                    input[inp['if_true']]['items'].append(old)
                else:
                    input[inp['if_false']]['items'].append(old)
                monkey[i] += 1
            inp['items'] = []
    monkey.sort(reverse=True)
    print(monkey[0] * monkey[1])

if __name__ == '__main__':
    main()
