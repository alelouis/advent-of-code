from heapq import *
import time


def manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def solve_this_fucking_day(end, part):
    (r, s) = (1, 3) if part == 1 else (4, 10)
    q, v = [(0, 0, (0, 0), "?")], set()
    while q:
        _, h, p, d = heappop(q)
        if (p, d) not in v:
            v.add((p, d))
            if p == end:
                return h
            for nd in op[d]:
                np, nh = p, h
                for i in range(1, s + 1):
                    np = (np[0] + ds[nd][0], np[1] + ds[nd][1])
                    if 0 <= np[0] < rows and 0 <= np[1] < cols:
                        nh += lines[np[0]][np[1]]
                        if i >= r and (np, nd) not in v:
                            heappush(q, (nh - manhattan(np, (70, 70)), nh, np, nd))


op = {"v": "<>", "^": "<>", "<": "v^", ">": "v^", "?": "v^<>"}
ds = {"v": (1, 0), "<": (0, -1), ">": (0, 1), "^": (-1, 0)}
lines = [list(map(int, list(l.strip()))) for l in open("input").readlines()]
rows, cols = len(lines), len(lines[0])
print(solve_this_fucking_day((rows - 1, cols - 1), 1))
print(solve_this_fucking_day((rows - 1, cols - 1), 2))
