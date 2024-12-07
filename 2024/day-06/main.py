def walk(terrain, obstacles):
    (cd, p), v = start, set()
    while p in terrain:
        v.add((cd, p))
        if (next_pos := (p[0] + d[cd][0], p[1] + d[cd][1])) in obstacles:
            cd = c[cd]
        else:
            p = next_pos
            if (cd, p) in v: return 'loop'
    return v

lines = [list(s.strip()) for s in open('test').readlines()]
rows, cols = len(lines), len(lines[0])
ter, obs = (set((r, c) for r in range(rows) for c in range(cols) if lines[r][c] in t) for t in ['.^v><', '#'])
start = [(d, (r, c)) for r in range(rows) for c in range(cols) if (d := lines[r][c]) in '^v><'][0]
d, c = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}, {'^': '>', '>': 'v', 'v': '<', '<': '^'}

v = walk(ter, obs)
print(len(set(p for _, p in v)))
print(sum(walk(ter - {o}, obs | {o}) == 'loop' for o in (set(p for _, p in v) - set(start))))


