from collections import deque


def get_path(m, visited):
    path = []
    while m:
        path.append(m)
        m = visited[m]
    return path[::-1]


def bfs(node, target):
    visited, queue = {}, deque()
    visited[node] = None
    queue.append(node)
    while queue:
        m = queue.popleft()
        if m == target:
            return get_path(m, visited)
        for neighbour in [(m + d) for d in (1, -1, 1j, -1j) if (m + d) in free]:
            if neighbour not in visited:
                visited[neighbour] = m
                queue.append(neighbour)


bytes = [int(l.split(',')[0]) + 1j * int(l.split(',')[1]) for l in open('input').readlines()]
free = set(r + 1j * c for r in range(70 + 1) for c in range(70 + 1)) - set(bytes[:1024])
print(len(bfs(0, 70 + 70 * 1j)))

for n_bytes in range(len(bytes), 0, -1):
    free = set(r + 1j * c for r in range(70 + 1) for c in range(70 + 1)) - set(bytes[:n_bytes])
    if bfs(0, 70 + 70 * 1j) is not None:
        print(f"{bytes[n_bytes].real:.0f},{bytes[n_bytes].imag:.0f}")
        break
