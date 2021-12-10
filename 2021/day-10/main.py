lines = [l.rstrip() for l in open('input')]
s, e = '({[<', ')}]>'
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores_2 = {')': 1, ']': 2, '}': 3, '>': 4}

def step(st, h, l):
    if h == len(l): return ''.join([e[s.find(c)] for c in st[::-1]])
    elif l[h] in s: return step(st+l[h], h+1, l)
    elif st != '' and l[h] == e[s.find(st[-1])]: return step(st[:-1], h+1, l)
    else: return scores[l[h]]

def get_score(seq, sc = 0):
    for s in seq: sc = 5 * sc + scores_2[s]
    return sc

out = [step('', 0, l) for l in lines]
scores = sorted([get_score(s) for s in [l for l in out if isinstance(l, str)]])
print(f'part-1 answer : {sum([l for l in out if isinstance(l, int)])}')
print(f'part-2 answer : {scores[int(len(scores)/2)]}')