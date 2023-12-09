from itertools import cycle


def diff(line, stack, part):
    return stack if (d := [j - i for i, j in zip(line, line[1:])])[-1] == 0 else diff(d, stack + [d[-(2 - part)]], part)


def solve(lines, part):
    return sum(sum([s * e for s, e in zip(cycle([1, 2 * (part % 2) - 1]), diff(l, [l[-(2 - part)]], part))]) for l in lines)


lines = [list(map(int, m.split())) for m in open("input").readlines()]

print(solve(lines, 1))
print(solve(lines, 2))
