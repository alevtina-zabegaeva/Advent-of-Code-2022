def main():
    def check_signal(c, x):
        return c*x if c % 40 == 20 else 0


    # filename = '10.1test.txt'
    filename = '10.1input.txt'

    with open(filename) as f:
        program = [int(line.rstrip().split()[1]) if line[0] == 'a' else '' for line in f]
    
    cycle = 0
    x = 1
    sum_signal_strength = 0

    for line in program:
        cycle += 1
        sum_signal_strength += check_signal(cycle, x)
        if line != '':
            cycle += 1
            sum_signal_strength += check_signal(cycle, x)
            x += line
    print(sum_signal_strength)

if __name__ == '__main__':
    main()
