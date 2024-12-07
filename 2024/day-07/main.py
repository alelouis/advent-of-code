lines = [(int(l.split(':')[0]), list(map(int, l.split(':')[1].strip().split()))) for l in open('input').readlines()]


def solve(t, n, part):
    ops = [lambda x, y: x + y, lambda x, y: x * y, lambda x, y: int(str(x) + str(y))]
    return (t == n[0]) if len(n) == 1 else any([solve(*arg, part) for arg in [(t, [op(n[0], n[1])] + n[2:]) for op in ops[:part+1]]])


print(list(sum(l[0] for l in lines if solve(*l, part=p)) for p in [1, 2]))
