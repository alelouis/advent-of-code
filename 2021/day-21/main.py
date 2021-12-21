import itertools

def game(part, turn, bound, pos, score, p, hist, dices):
    if (p, str(pos), str(score)) in hist: return hist[(p, str(pos), str(score))]
    wins = [0, 0]
    for dice in dices(turn):
        _pos = pos.copy()
        _score = score.copy()
        _pos[p] = (_pos[p] + dice - 1)%10 + 1
        _score[p] += _pos[p]
        if _score[p] >= bound: 
            if part == 1: print(f'part-1 answer : {(turn+1)*3 * score[0 if p else 1]}')
            wins[p] += 1
        else:
            next_turns = game(part, turn+1, bound, _pos, _score, 0 if p else 1, hist, dices)
            wins[0], wins[1] = wins[0] + next_turns[0], wins[1] + next_turns[1]
    hist[(p, str(pos), str(score))] = wins
    return wins

game(1, 0, 1000, [5, 10], [0, 0], 0, {}, lambda t: [6 + 9*t])
dirac_dice = list(map(sum, itertools.product(range(1,4), repeat=3)))
print(f'part-2 answer : {max(game(2, 0, 21, [5, 10], [0, 0], 0, {}, lambda t : dirac_dice))}')