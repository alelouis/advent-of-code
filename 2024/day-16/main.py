import heapq


def find_elements(element):
    return set((r, c) for r in range(rows) for c in range(cols) if map[r][c] in element)


def dij(start, end):
    queue = [(0, start, '>', [start])]
    visited = {}
    best_paths = set()
    best_score = float('inf')
    while queue:
        score, pos, d, path = heapq.heappop(queue)
        if pos == end:
            if score == best_score:
                best_paths |= set(path)
            elif score < best_score:
                best_score, best_paths = score, set()
        visited[pos, d] = score
        for np, nd in [((pos[0]+vec[d][0], pos[1]+vec[d][1]), d)] + [(pos, nd) for nd in cycle[d]]:
            if np in free:
                new_score = score + (1000 if d != nd else 1)
                if visited.get((np, nd), float('inf')) > new_score:
                    heapq.heappush(queue, (new_score, np, nd, path + [np]))
    return best_score, best_paths


vec = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
cycle = {'v': ['>', '<'], '^': ['>', '<'], '>': ['^', 'v'], '<': ['^', 'v']}
map = [[c for c in l.strip()] for l in open('input').readlines()]
rows, cols = len(map), len(map[0])
free, (start,), (end,) = find_elements('.SE'), find_elements('S'), find_elements('E')
score, best_paths = dij(start, end)
print(score, len(best_paths))