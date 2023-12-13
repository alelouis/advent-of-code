def transpose(p):
    return ["".join([p[r][c] for r in range(len(p))]) for c in range(len(p[0]))]


def find_reflection(p, r, part):
    return sum(((u + 1) * (part - 1 == sum(a != b for d in range(min(u, r - v - 1) + 1) for a, b in zip(p[u - d], p[v + d]))) for u, v in zip(range(r - 1), range(1, r))))


def solve(ps, part):
    return sum(find_reflection(transpose(p), len(p[0]), part) + 100 * find_reflection(p, len(p), part) for p in ps)


patterns = [l.split('\n') for l in open('input').read().split('\n\n')]
print(solve(patterns, 1))
print(solve(patterns, 2))
