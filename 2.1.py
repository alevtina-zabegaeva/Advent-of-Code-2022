filename = '2.1input.txt'

with open(filename) as f:
    games = [line.strip().split() for line in f]

score_dict = {'X': 1, 'Y': 2, 'Z': 3,
              'A': 1, 'B': 2, 'C': 3}
score = [score_dict[game[1]] + (score_dict[game[1]] - score_dict[game[0]] + 1) % 3 * 3 for game in games]
print(sum(score))

score = [ord(game[1]) - ord('X') + 1 + (ord(game[1]) - ord('X') - ord(game[0]) + ord('A') + 1) % 3 * 3 for game in games]
print(sum(score))
