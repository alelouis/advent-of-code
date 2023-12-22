from collections import deque


def fall_by_one(brick):
    return [(brick[i][0], brick[i][1], brick[i][2] - 1) for i in [0, 1]]


def where(b):
    return set((x, y, z) for z in range(b[0][2], b[1][2] + 1) for y in range(b[0][1], b[1][1] + 1) for x in range(b[0][0], b[1][0] + 1))


def drop_bricks(bricks):
    nb, where_map = [], {}
    for b in sorted(bricks, key=lambda b: b[0][2]):
        while (f := fall_by_one(b))[0][2] > 0:
            next_b = f
            if any((o in where_map for o in where(next_b))):
                break
            else:
                b = next_b
        nb.append(b)
        for o in where(b):
            where_map[o] = str(b)
    return where_map, nb


def get_relations(occ, nb):
    rel = dict({str(k): {"up": set(), "down": set()} for k in nb})
    for b in nb:
        for pos in where(fall_by_one(b)) - where(b):
            if pos in occ:
                rel[occ[pos]]["up"].add(str(b))
                rel[str(b)]["down"].add(occ[pos])
    return rel


def its_raining_bricks(brick):
    f, q = {str(brick)}, deque([brick])
    while q:
        b = str(q.popleft())
        for up in rel[b]["up"]:
            if all(b in f for b in rel[up]["down"]):
                f.add(up)
                q.append(up)
    return len(f) - 1


def solve(l):
    return sum(l(its_raining_bricks(f)) for f in nb)


bricks = [[tuple(list(map(int, c.split(",")))) for c in l.strip().split("~")] for l in open("input").readlines()]
occ, nb = drop_bricks(bricks)
rel = get_relations(occ, nb)
print(solve(lambda x: x == 0))
print(solve(lambda x: x))
