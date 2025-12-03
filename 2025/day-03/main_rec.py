def rsolve(b, nb, f=0):
    return str(m := max((lr := [b[i] for i in range(len(b) - nb + f + 1)]))) + rsolve(b[lr.index(m) + 1:], nb, f + 1) if f < nb else ''

print(list(sum(int(rsolve(b, nb, 0)) for b in [b.strip() for b in open('input').readlines()]) for nb in [2, 12]))
