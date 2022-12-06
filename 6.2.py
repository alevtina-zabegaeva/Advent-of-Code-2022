def main():
    N = 14

    filename = '6.1input.txt'
    with open(filename) as f:
        signal = f.readline()

    # signal = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    # signal = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    # signal = "nppdvjthqldpwncqszvftbrmjlhg"
    # signal = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    # signal = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

    for i in range(N, len(signal)):
        if len(set(signal[i - N:i])) == N:
            break
    print(i)

if __name__ == '__main__':
    main()
