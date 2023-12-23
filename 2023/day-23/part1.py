import sys

sys.setrecursionlimit(10000)


def reverse_from_paths(paths, start, end):
    path = [end]
    current = end
    while current != start:
        path.append(paths[current][0])
        current = path[-1]
    path = path[::-1]
    return path


def get_neigh(node, dots):
    deltas = ((0, 1), (0, -1), (-1, 0), (1, 0))
    slopes = {"v": (1, 0), "<": (0, -1), ">": (0, 1), "^": (-1, 0)}
    candidates = set()
    if lines[node[0]][node[1]] == ".":
        for d in deltas:
            candidates.add((node[0] + d[0], node[1] + d[1]))
    else:
        d = slopes[lines[node[0]][node[1]]]
        candidates.add((node[0] + d[0], node[1] + d[1]))
    neigh = [c for c in candidates if c in dots]
    return neigh


def find_all_paths(get_neigh, start, end, path):
    path = path + [start]
    if start == end:
        return [len(path) - 1]
    paths = set()
    for node in reversed(get_neigh(start, dots)):
        if node not in path:
            newpaths = find_all_paths(get_neigh, node, end, path)
            for newpath in newpaths:
                paths.add(newpath)
    return paths


lines = [l.strip() for l in open("input").readlines()]
rows, cols = len(lines), len(lines[0])
dots = set((r, c) for r in range(len(lines)) for c in range(len(lines[0])) if (s := lines[r][c]) != "#")
paths = find_all_paths(get_neigh, (0, 1), (rows - 1, cols - 2), [])
print(max(p for p in paths))
