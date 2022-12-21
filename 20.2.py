from copy import deepcopy

def main():

    # filename = '20.1test.txt'
    filename = '20.1input.txt'

    decryption_key = 811589153
    with open(filename) as f:
        input = tuple(int(line) * decryption_key for line in f.readlines())
    print(input)
    length = len(input)
    print(length)

    N = 10

    current = [i for i in range(length)]

    for _ in range(N):
        for n in range(length):
            if input[n] != 0:
                cur_index = current.index(n)
                new_index = (cur_index + input[n]) % (length - 1)
                current.pop(cur_index)
                current.insert(new_index, n)
    print(current)

    i0 = current.index(input.index(0))
    answer = (input[current[(i0 + 1000) % length]] +
              input[current[(i0 + 2000) % length]] +
              input[current[(i0 + 3000) % length]])
    print(answer)


if __name__ == '__main__':
    main()
