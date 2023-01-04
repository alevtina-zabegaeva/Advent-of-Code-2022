def main():
    # filename = '25test.txt'
    filename = '25input.txt'


    input = []
    with open(filename) as f:
        input = [line.rstrip() for line in f]

    print(input)
    decimal_lst = []
    for inpt in input:
        decimal_lst.append(0)
        for i, digit in enumerate(inpt[::-1]):
            if digit == '=':
                d = -2
            elif digit == '-':
                d = -1
            else:
                d = int(digit)
            decimal_lst[-1] += d * 5**i
    print(decimal_lst)
    decimal_sum = sum(decimal_lst)
    print(decimal_sum)
    
    answer = []
    number = decimal_sum
    i = 0
    while 5**i < number:
        i += 1
    while i >= 0:
        div = int(number / 5**i)
        if abs(div) >= 3:
            sgn = div // abs(div)
            i += 1
            while answer[-1] == sgn * 2:
                number += sgn * (2 * 5**i)
                answer.pop()
                i += 1
            answer[-1] += sgn
            number -= sgn * 5**i
        else:
            number -= div * 5**i
            answer.append(div)
        i -= 1
    if answer[0] == 0:
        answer.pop(0)
    print(answer)
    for digit in answer:
        if digit == -2:
            print('=', end='')
        elif digit == -1:
            print('-', end='')
        else:
            print(digit, end='')
    print()


if __name__ == '__main__':
    main()
