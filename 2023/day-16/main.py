import sys

sys.setrecursionlimit(5000)


def count_energy(moves):
    return sum(len(c) != 0 for r in moves for c in r)


def where(tile, heading):
    if heading in where_dict[tile]:
        return where_dict[tile][heading]
    else:
        return heading


def propagate(ray, layout, moves):
    pos, heading = ray
    new_pos = [pos[0] + headings[heading][0], pos[1] + headings[heading][1]]
    if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols:
        if heading in moves[new_pos[0]][new_pos[1]]:
            return
        else:
            moves[new_pos[0]][new_pos[1]].append(heading)
        if tuple(new_pos) in layout:
            for new_heading in where(layout[(new_pos[0], new_pos[1])], heading):
                propagate([new_pos, new_heading], layout, moves)
        else:
            propagate([new_pos, heading], layout, moves)


def find_max_energy():
    max_energy = 0
    for headstart in headings:
        for r in range(rows):
            ray = [[r, -1 if headstart == ">" else cols], headstart]
            propagate(ray, layout, (moves := [[[] for _ in range(cols)] for _ in range(rows)]))
            if (energy := count_energy(moves)) > max_energy:
                max_energy = energy
        for c in range(cols):
            ray = [[rows if headstart == "^" else -1, c], headstart]
            propagate(ray, layout, (moves := [[[] for _ in range(cols)] for _ in range(rows)]))
            if (energy := count_energy(moves)) > max_energy:
                max_energy = energy
    return max_energy


where_dict = {"|": {"<": "^v", ">": "^v"}, "-": {"^": "<>", "v": "<>"}, "/": {"^": ">", "v": "<", "<": "v", ">": "^"}, "\\": {"^": "<", "v": ">", "<": "^", ">": "v"}}
headings = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
lines = [list(l.strip()) for l in open("input").readlines()]
rows, cols = len(lines), len(lines[0])
layout = {(r, c): s for r in range(len(lines)) for c in range(len(lines[0])) if (s := lines[r][c]) != "."}
propagate([[0, -1], ">"], layout, (moves := [[[] for _ in range(cols)] for _ in range(rows)]))

print(count_energy(moves))
print(find_max_energy())
