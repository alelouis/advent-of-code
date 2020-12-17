lines, dim, N = open('input').read().replace('\n',''), 4, 8
active = set([(i%N, i//N, 0, 0) for i, l in enumerate(lines) if l == '#'])
zo = [(x, y, z, w) for x in range(-1,2) for y in range(-1,2) for z in range(-1,2) for w in range(-1, 2)]
ns = zo.copy()
ns.remove(tuple([0]*dim))

def next_state(c):
    c_n = 0
    for n in ns:
        _n = (c[0] + n[0], c[1] + n[1], c[2] + n[2], c[3] + n[3])
        if _n in active: c_n += 1
    if c in active and not (c_n == 2 or c_n == 3): _active.remove(c)
    elif c_n == 3: _active.add(c)

for cycle in range(6):
    _active = active.copy()
    check_p = set([(p[0]+d[0], p[1]+d[1], p[2]+d[2], p[3]+d[3]) for p in active for d in zo])
    for c in check_p:
        next_state(c)
    active = _active.copy()

print(f'part-1/2 answer: {len(active)}')
