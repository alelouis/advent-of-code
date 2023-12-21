import numpy as np


def build_map(rows, cols, lines, rep):
    offsets, rocks, marked = [(rows * i, cols * j) for i in range(-rep, rep + 1) for j in range(-rep, rep + 1)], set(), set()
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == "#":
                rocks.add((r, c))
            if lines[r][c] == "S":
                start = (r, c)
    rocks = set((r[0] + offset_r, r[1] + offset_c) for offset_r, offset_c in offsets for r in rocks)
    return rocks, start


def count_for(max_iter):
    positions, iteration = [start], 0
    for iteration in range(max_iter):
        marked = set()
        for p in positions:
            marked |= get_next_pos(p)
        positions = marked
    return len(marked)


def get_next_pos(pos):
    return set(c for c in [(pos[0] + d[0], pos[1] + d[1]) for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]] if c not in rocks)


lines = [l.strip() for l in open("input").readlines()]
rows, cols = len(lines), len(lines[0])
rocks, start = build_map(rows, cols, lines, 2)
print(count_for(64))

xx = [65 + i * 131 for i in range(3)]
yy = [count_for(x) for x in xx]
poly = np.polyfit(xx, yy, deg=2)
f = lambda x: poly[2] + x * poly[1] + x**2 * poly[0]
print(int(f(26501365)))
