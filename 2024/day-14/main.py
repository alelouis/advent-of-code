import numpy as np


def count(p, rmin, rmax, cmin, cmax):
    return sum(cmin <= c < cmax and rmin <= r < rmax for c, r in p)


def part1():
    pos = [[(p[0] + 100 * v[0]) % cols, (p[1] + 100 * v[1]) % rows] for i, (p, v) in
           enumerate(zip(positions, velocities))]
    a = count(pos, 0, rows // 2, 0, cols // 2)
    b = count(pos, rows // 2 + 1, rows, 0, cols // 2)
    c = count(pos, 0, rows // 2, cols // 2 + 1, cols)
    d = count(pos, rows // 2 + 1, rows, cols // 2 + 1, cols)
    return a * b * c * d


def part2():
    store = np.zeros((10000, len(positions), 2))
    for it in range(np.size(store, 0)):
        for i, (p, v) in enumerate(zip(positions, velocities)):
            store[it, i] = [(p[0] + it * v[0]) % cols, (p[1] + it * v[1]) % rows]
    return np.argmin(np.var(store, axis=1)[:, 1] * np.var(store, axis=1)[:, 0])


rows, cols = 103, 101
positions, velocities = [
    [[list(map(int, d.split('=')[1].split(','))) for d in l.strip().split(' ')][i] for l in open("input").readlines()]
    for i in [0, 1]]

print(part1())
print(part2())
