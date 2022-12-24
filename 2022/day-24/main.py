import copy, functools

def add(p, q): 
    return (p[0]+q[0], p[1]+q[1])

@functools.cache
def get_state_at(minute):
    next_positions = copy.deepcopy(pos)
    for position in pos:
        for s in pos[position]:
            (r, c), (dr, dc) = position, {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}[s]
            next_positions[position].remove(s)
            next_positions[(1+(r-1+dr*minute)%depth, 1+(c-1+dc*minute)%width)].extend(s)
    return next_positions

def possible(me, pos, start, end):
    deltas = (0, 1), (1, 0), (0, -1), (0, 0), (-1, 0), 
    moves = [add(me, d) for d in deltas]
    pos = [m for m in [add(me, d) for d in deltas] if ((m[0], m[1]) in pos and len(pos[(m[0], m[1])])==0)]
    if start in moves: pos.append(start)
    if end in moves: pos.append(end)
    return pos

def bfs(start, end, start_minute):
    queue, visited = [(start_minute, start)], set()
    while queue:
        minute, me = queue.pop(0)
        minute += 1
        for move in possible(me, get_state_at(minute), start, end):
            if (minute, move) not in visited:
                if move == end: return minute
                visited.add((minute, move))
                queue.append((minute, move))

mat = [list(r) for r in open('input').read().splitlines()]
pos = {(r, c): [mat[r][c]] if mat[r][c] in ['<', '>', '^', 'v'] else [] for c in range(len(mat[0])) for r in range(len(mat)) if mat[r][c] != '#'}
minr, maxr, minc, maxc = min(p[0] for p in pos)+1, max(p[0] for p in pos)-1, min(p[1] for p in pos), max(p[1] for p in pos)
width, depth = maxc-minc+1, maxr-minr+1
start, end = (0, 1), (36, 100)

one = bfs(start, end, 0)
print(f'part-1: {one}')
two = bfs(start, end, bfs(end, start, one))
print(f'part-2: {two}')