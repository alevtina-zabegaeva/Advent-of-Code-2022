def main():
    def compare(l1, l2):
        islist1, islist2 = isinstance(l1, list), isinstance(l2, list)
        if islist1 and islist2:
            for j in range(max(len_l1 := len(l1), len_l2 := len(l2))):
                if j >= len_l1:
                    return True
                if j >= len_l2:
                    return False
                c = compare(l1[j], l2[j])
                if c is False or c is True:
                    return c
        elif not islist1 and not islist2:
            if l1 < l2:
                return True
            if l1 > l2:
                return False
        elif islist1 and not islist2:
            c = compare(l1, [l2])
            if c is False or c is True:
                return c
        else:
            c = compare([l1], l2)
            if c is False or c is True:
                return c


    # filename = '13.1test.txt'
    filename = '13.1input.txt'

    with open(filename) as f:
        lists = [eval(line) for line in f if line.strip()]

    packet = [[[2]], [[6]]]
    counter = [1, 2]
    for lst in lists:
        if compare(lst, packet[0]):
            counter[0] += 1
            counter[1] += 1
        elif compare(lst, packet[1]):
            counter[1] += 1

    print(counter)
    print(counter[0] * counter[1])


if __name__ == '__main__':
    main()
