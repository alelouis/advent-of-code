from collections import deque, defaultdict

def find_elements(element):
    return set(r + 1j*c for r in range(rows) for c in range(cols) if map[r][c] in element)

def get_path(m, visited):
    path = []
    while m:
        path.append(m)
        m = visited[m][0]
    return path[::-1]

def l1(a, b):
    return abs(a.real-b.real) + abs(b.imag-a.imag)

def bfs(start):
    visited, queue = {}, deque()
    visited[start] = (None, 0)
    queue.append(start)
    while queue:
        m = queue.popleft()
        for neighbour in [(m + d) for d in (1, -1, 1j, -1j) if (m + d) in free]:
            if neighbour not in visited:
                visited[neighbour] = (m, visited[m][1] + 1)
                queue.append(neighbour)
    return visited

def please_cheat(ps):
    cheats = defaultdict(set)
    for i, ni in enumerate(optimal_path):
        for nj in optimal_path[i+1:]:
            if (d := l1(ni, nj)) <= ps and v[nj][1] + d < v[ni][1]:
                cheats[int(v[ni][1] - v[nj][1] - d)].add((ni, nj))
    return sum(len(c) for gain, c in cheats.items() if gain >= 100)


map = [[c for c in l.strip()] for l in open('input').readlines()]
rows, cols = len(map), len(map[0])
walls, free, (start,), (end,) = [find_elements(e) for e in '#.SE']
free.add(start); free.add(end)

v = bfs(end)
optimal_path = get_path(start, v)[::-1]

print(please_cheat(2))
print(please_cheat(20))