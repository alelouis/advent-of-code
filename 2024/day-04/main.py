def solve(part):
    z = 'XMAS' if part == 1 else 'MAS'
    p = [(pad := ['#'] * 3) + list(s.strip()) + pad for s in open('input').readlines()]
    p = (pad := 3 * [['#'] * len(p[0])]) + p + pad
    dir, sig, found = ((0, 1), (1, 0), (1, 1), (1, -1)) if part == 1 else ((1, 1), (1, -1)), (1, -1), 0
    for r in range(3, len(p) - 3):
        for c in range(3, len(p[0]) - 3):
            check = {(d, s): "".join([p[r + k * s * d[1]][c + k * s * d[0]] for k in range(*(0, 4) if part == 1 else (-1, 2))]) == z for s in sig for d in dir}
            found += sum(check[(d, s)] for d in dir for s in sig) if part == 1 else all(any(check[(d, s)] for s in sig) for d in dir)
    return found

print(solve(1), solve(2))