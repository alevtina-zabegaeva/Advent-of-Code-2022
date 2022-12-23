import re
import copy


def main():

    # filename = '21.1test.txt'
    filename = '21.1input.txt'

    monkeys_numbers_input = {}
    monkeys_operations_input = {}
    with open(filename) as f:
        for line in f:
            names = re.findall('[a-z]+', line)
            if len(names) == 1:
                monkeys_numbers_input[names[0]] = re.findall('\d+', line)[0]
            else:
                monkeys_operations_input[names[0]] = (names[1:], re.findall('[-\+\*/]', line)[0])

    monkeys_operations_input['root'] = (monkeys_operations_input['root'][0], '-')

    X, Y = [0, 1e13], []
    for x in X:
        monkeys_numbers = copy.deepcopy(monkeys_numbers_input)
        monkeys_operations = copy.deepcopy(monkeys_operations_input)
        monkeys_numbers['humn'] = str(x)

        while 'root' not in monkeys_numbers:
            calculated = set()
            for name, operation in monkeys_operations.items():
                if (name1 := operation[0][0]) in monkeys_numbers and (name2 := operation[0][1]) in monkeys_numbers:
                    monkeys_numbers[name] = str(eval(monkeys_numbers[name1] + operation[1] + monkeys_numbers[name2]))
                    calculated.add(name)
            for name in calculated:
                monkeys_operations.pop(name)

        Y.append(float(monkeys_numbers['root']))
    x = (X[0] * Y[1] - X[1] * Y[0]) / (Y[1] - Y[0])
    print(x)


if __name__ == '__main__':
    main()
