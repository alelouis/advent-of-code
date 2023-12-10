from collections import deque


def bfs(start):
    queue, visited, values = deque([start]), [], {start: 0}
    while queue:
        visited.append(queue.popleft())
        row, col = eval(visited[-1])
        neighbors = [f"({nr}, {nc})" for dir in choices[mapp[row][col]] if 0 <= (nr := row + moves[dir][0]) < len(mapp) and 0 <= (nc := col + moves[dir][1]) < len(mapp[0])]
        for neigh in neighbors:
            if neigh not in visited:
                queue.append(neigh)
                values[neigh] = values[visited[-1]] + 1
    return values


def count_inside(lines, values):
    inside_points = 0
    for r in range(len(lines)):
        switch = 1
        for c in range(len(lines[0])):
            if f"({r}, {c})" in values:
                switch *= -1 if lines[r][c] in ["|", "F", "7"] else 1
            else:
                inside_points += 1 if switch == -1 else 0
    return inside_points


mapp = [list(l.strip()) for l in open("input").readlines()]
choices = {"|": ["N", "S"], "7": ["W", "S"], "F": ["E", "S"], "L": ["N", "E"], "J": ["N", "W"], "-": ["E", "W"]}
moves = {"S": (1, 0), "N": (-1, 0), "E": (0, 1), "W": (0, -1)}

start = (72, 119)
mapp[start[0]][start[1]] = "J"

values = bfs(str(start))
print(max(v for v in values.values()))
print(count_inside(mapp, values))
