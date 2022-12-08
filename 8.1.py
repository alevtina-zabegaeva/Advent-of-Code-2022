import numpy as np

def main():
    def visible(arr, ii, jj):
        return (all(arr[ii,:jj] < arr[ii, jj]) or
                all(arr[ii,jj + 1:] < arr[ii, jj]) or
                all(arr[:ii,jj] < arr[ii, jj]) or
                all(arr[ii + 1:,jj] < arr[ii, jj]))
        

    # filename = '8.1test.txt'
    filename = '8.1input.txt'

    with open(filename) as f:
        trees = [list(map(int, list(line.rstrip()))) for line in f]
    trees = np.array(trees)

    counter = 0
    for i in range(trees.shape[0]):
        for j in range(trees.shape[1]):
            if visible(trees, i, j):
                counter += 1
    print(counter)


if __name__ == '__main__':
    main()
