from itertools import pairwise

def check(r):
    return (r == sorted(r) or r == sorted(r, reverse=True)) and all(map(lambda x: 1 <= abs(x[1] - x[0]) <= 3, pairwise(r)))

reports = [list(map(int, p.rstrip().split())) for p in open('input').readlines()]
print(sum([check(r) for r in reports]))
print(sum([any(check(r[:i] + r[i+1:]) for i in range(len(r))) for r in reports]))