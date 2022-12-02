filename = '2.1input.txt'

with open(filename) as f:
    games = [line.strip().split() for line in f]

score_dict = {'X': 0, 'Y': 3, 'Z': 6,
              'A': 1, 'B': 2, 'C': 3}
lose_draw_win_dict = {'X': 2, 'Y': 0, 'Z': 1}

score = [score_dict[game[1]] + (score_dict[game[0]] + lose_draw_win_dict[game[1]] - 1) % 3 + 1 for game in games]
print(sum(score))
