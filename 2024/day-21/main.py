import heapq
from functools import cache

numeric_map = [[c for c in l.strip()] for l in open("numeric").readlines()]
directional_map = [[c for c in l.strip()] for l in open("directional").readlines()]

numeric_pos = set((r, c) for r in range(len(numeric_map)) for c in range(len(numeric_map[0])) if numeric_map[r][c] in "0123456789A")
directional_pos = set((r, c) for r in range(len(directional_map)) for c in range(len(directional_map[0])) if directional_map[r][c] in "<v>^A")


def flatten(S):
    if not S:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])


def find(element, map):
    return [(r, c) for r in range(len(map)) for c in range(len(map[0])) if map[r][c] == element][0]


def convert_path_to_string(path):
    string = ""
    for node, next_node in zip(path, path[1:]):
        delta = (next_node[0] - node[0], next_node[1] - node[1])
        string += moves[delta]
    return string


def dij(start, end, map_pos):
    queue = [(0, start, [start])]
    visited = {}
    best_paths = set()
    while queue:
        score, pos, path = heapq.heappop(queue)
        if pos == end:
            best_paths.add(convert_path_to_string(path))
        visited[pos] = score
        for np in [(pos[0] + d[0], pos[1] + d[1]) for d in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (pos[0] + d[0], pos[1] + d[1]) in map_pos]:
            new_score = score + 1
            if visited.get(np, float("inf")) > new_score:
                heapq.heappush(queue, (new_score, np, path + [np]))
    return best_paths


def type_keypad(before, index, code, map_type):
    map = numeric_map if map_type == "numeric" else directional_map
    if index == len(code):
        return before
    else:
        current_char = "A" if index == 0 else code[index - 1]
        target_char = code[index]
        paths = dij(find(current_char, map), find(target_char, map), numeric_pos)
        return [type_keypad(before + p + "A", index + 1, code, map_type) for p in paths]


@cache
def shorter(sequence, idx_robot, n_robots):
    total_len = 0
    if idx_robot == n_robots:
        return len(sequence)
    else:
        for i, (s, st) in enumerate(zip("A" + sequence, ("A" + sequence)[1:])):
            paths = dij(find(s, directional_map), find(st, directional_map), directional_pos)
            total_len += min([shorter(p + "A", idx_robot + 1, n_robots) for p in paths])
    return total_len


def min_length(codes, n_robots):
    ans = 0
    for code in codes:
        kps = flatten(type_keypad("", 0, code, "numeric"))
        s = min(shorter(k, 0, n_robots) for k in kps)
        ans += s * int(code[:-1])
    return ans


moves = {(1, 0): "v", (-1, 0): "^", (0, -1): "<", (0, 1): ">"}
codes = [l.strip() for l in open("input").readlines()]
print(min_length(codes, 2))
print(min_length(codes, 25))
