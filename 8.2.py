import numpy as np

def main():
    def scenic_index(arr, ii, jj):
        sides = [np.flip(arr[ii,:jj]),
                 arr[ii, jj + 1:],
                 np.flip(arr[:ii,jj]),
                 arr[ii + 1:,jj]]
        views = 1
        for side in sides:
            counter = 0
            for elem in side:
                counter += 1
                if elem >= arr[ii, jj]:
                    break
            views *= counter

        return views
        

    # filename = '8.1test.txt'
    filename = '8.1input.txt'

    with open(filename) as f:
        trees = [list(map(int, list(line.rstrip()))) for line in f]
    trees = np.array(trees)

    scenic = []
    for i in range(trees.shape[0]):
        for j in range(trees.shape[1]):
            scenic.append(scenic_index(trees, i, j))
    print(max(scenic))


if __name__ == '__main__':
    main()
