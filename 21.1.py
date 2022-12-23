import re


def main():

    # filename = '21.1test.txt'
    filename = '21.1input.txt'

    monkeys_numbers = {}
    monkeys_operations = {}
    with open(filename) as f:
        for line in f:
            names = re.findall('[a-z]+', line)
            if len(names) == 1:
                monkeys_numbers[names[0]] = re.findall('\d+', line)[0]
            else:
                monkeys_operations[names[0]] = (names[1:], re.findall('[-\+\*/]', line)[0])
    # print(monkeys_numbers)
    # print(monkeys_operations)

    while 'root' not in monkeys_numbers:
        calculated = set()
        for name, operation in monkeys_operations.items():
            if (name1 := operation[0][0]) in monkeys_numbers and (name2 := operation[0][1]) in monkeys_numbers:
                monkeys_numbers[name] = str(int(eval(monkeys_numbers[name1] + operation[1] + monkeys_numbers[name2])))
                calculated.add(name)
        for name in calculated:
            monkeys_operations.pop(name)

    # print(monkeys_numbers)
    # print(monkeys_operations)
    print(monkeys_numbers['root'])


if __name__ == '__main__':
    main()
