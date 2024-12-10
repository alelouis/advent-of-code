from collections import deque


def bfs(g, start, part):
    q, v, th = deque([start]), [], 0
    while q:
        n = q.popleft()
        th += g[n] == 9 and (part == 1) * n not in v
        v.append(n)
        for ne in [p for p in [n + 1j, n + 1, n - 1j, n - 1] if (p in g) and (g[p] - g[n] == 1)]:
            if ne not in v:
                q.append(ne)
    return th


lines = [[int(c) for c in list(s.strip())] for s in open('input').readlines()]
pos = {r + 1j * c: lines[r][c] for r in range(len(lines)) for c in range(len(lines[0]))}
print([sum(bfs(pos, start, part) for start in [p for p, v in pos.items() if v == 0]) for part in [1, 2]])
