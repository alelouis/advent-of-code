line = open('input').readline().split('=')
x, y = line[1].split(',')[0].split('..'), line[2].split('..')
tgt = [[int(x[0]), int(x[1])], [int(y[0]), int(y[1])]]
tgts = set(tuple((x, y)) for y in range(tgt[1][0], tgt[1][1]+1) for x in range(tgt[0][0], tgt[0][1]+1))

trags, ite , xv_range, yv_range = [], 0, [0, 200], [-150, 150]
for xv in range(xv_range[0], xv_range[1]):
    for yv in range(yv_range[0], yv_range[1]):
        p, v, trag = [0, 0], [xv, yv], set()
        while p[1] > tgt[1][0]:
            p[0], p[1] = p[0] + v[0], p[1] + v[1]
            v[0] += 0 if v[0] == 0 else -1 if v[0] > 0 else -1
            v[1] -= 1
            trag.add(tuple((p[0], p[1])))
        if trag.intersection(tgts) != set(): trags.append(trag)

print(f'part-1 answer : {max([y for traj in trags for _, y in traj ])}')
print(f'part-2 answer : {len(trags)}')