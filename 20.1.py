from copy import deepcopy

def main():

    # filename = '20.1test.txt'
    filename = '20.1input.txt'

    with open(filename) as f:
        input = [int(line) for line in f.readlines()]
    length = len(input)

    map_numbers = [[n, True] for n in input]
    counter = 0
    while counter < length:
        for i, number in enumerate(map_numbers):
            if number[1]:
                number[1] = False
                counter += 1
                if number[0] != 0:
                    new_index = (i + number[0]) % (length - 1)
                    map_numbers.pop(i)
                    map_numbers.insert(new_index, number)
                break

    numbers = [n[0] for n in map_numbers]
    print(numbers)
    i0 = numbers.index(0)
    print(i0)
    answer = numbers[(i0 + 1000) % length] + numbers[(i0 + 2000) % length] + numbers[(i0 + 3000) % length]
    print(numbers[(i0 + 1000) % (length)], numbers[(i0 + 2000) % (length)], numbers[(i0 + 3000) % (length)])
    print(answer)


if __name__ == '__main__':
    main()
