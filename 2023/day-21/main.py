import numpy as np


def build_map(rows, cols, lines, rep):
    offsets, rocks, marked = [(rows * i, cols * j) for i in range(-rep, rep + 1) for j in
                              range(-rep, rep + 1)], set(), set()
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == "#":
                rocks.add((r, c))
            if lines[r][c] == "S":
                start = (r, c)
    rocks = set((r[0] + offset_r, r[1] + offset_c) for offset_r, offset_c in offsets for r in rocks)
    return rocks, start


def count_for(max_iter):
    positions, iteration, history = [start], 0, dict()
    for iteration in range(max_iter):
        print(iteration)
        marked = set()
        for p in positions:
            marked |= get_next_pos(p)
        positions = marked
        history[iteration] = marked
    return history, len(marked)


def get_next_pos(pos):
    return set(
        c for c in [(pos[0] + d[0], pos[1] + d[1]) for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]] if c not in rocks)


lines = [l.strip() for l in open("input").readlines()]
rows, cols = len(lines), len(lines[0])
rocks, start = build_map(rows, cols, lines, 2)
print(count_for(64)[1])


xx = [65 + i * 131 for i in range(3)]
yy = [count_for(x)[1] for x in xx]
print(xx)
print(yy)
poly = np.polyfit(xx, yy, deg=2)
f = lambda x: poly[2] + x * poly[1] + x**2 * poly[0]
print(int(f(26501365)))

""" second method, less obscure """
history, _ = count_for(330)


def get_sum_value(m, idx):
    return int(m[idx[0] * 131:(idx[0] + 1) * 131, idx[1] * 131:(idx[1] + 1) * 131].sum())


def get_map_at_it(ite):
    m = np.zeros((131 * 5, 131 * 5))
    for mark in history[ite]:
        m[mark[0] + 262, mark[1] + 262] = 1
    return m


m = get_map_at_it(65 + 131 * 2 - 1)
smalls = [get_sum_value(m, idx) for idx in ((0, 1), (0, 3), (4, 1), (4, 3))]
bigs = [get_sum_value(m, idx) for idx in ((1, 1), (1, 3), (3, 1), (3, 3))]
pointy = [get_sum_value(m, idx) for idx in ((0, 2), (2, 0), (2, 4), (4, 2))]
center = get_sum_value(m, (2, 2))
border = get_sum_value(m, (3, 2))


def get_map_at_it(ite):
    m = np.zeros((131 * 5, 131 * 5))
    for mark in history[ite]:
        m[mark[0] + 262, mark[1] + 262] = 1
    return m


goal = 26501365 // 131
print(goal * sum(smalls) + (goal - 1) * sum(bigs) + sum(pointy) + goal ** 2 * border + (goal - 1) ** 2 * center)
