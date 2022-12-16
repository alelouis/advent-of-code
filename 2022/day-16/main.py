from itertools import combinations

def bfs(graph, start, end):
    queue, visited = [[start]], []
    while queue:
        path = queue.pop(0)
        if path[-1] == end:
            return len(path) - 1
        for adjacent in graph[path[-1]]["tunnels"]:
            if adjacent not in visited:
                visited.append(adjacent)
                queue.append(list(path) + [adjacent])

def parse(line): return (line[1], int(line[4].split("=")[1][:-1]), eval(str(list(map(lambda x: x.rstrip(","), line[9:])))))
def get_valves(lines): return {parse(line)[0]: {"tunnels": parse(line)[2], "rate": parse(line)[1]}for line in lines}
def filter_valves(valves): return set(k for k, v in valves.items() if v["rate"] > 0)
def dfs(c, t, m, s, mv): return s if (m > mv or t == set()) else max(dfs(tg, t - {tg}, m + d[f"{c}_{tg}"] + 1, s + valves[tg]["rate"] * (mv - min(mv, m + d[f"{c}_{tg}"])), mv,)for tg in t)
def part(v, vf): return max(dfs("AA", vf - set(c), 1, 0, 26) + dfs("AA", set(c), 1, 0, 26) for r in range(2, len(v) // 2) for c in combinations(vf, r))

valves = get_valves(list(map(lambda l: l.split(" "), open("input").read().splitlines())))
d = {f"{k1}_{k2}": bfs(valves, k1, k2) for k2 in valves for k1 in valves}
print(f"part-1 answer: {dfs('AA', filter_valves(valves), 1, 0, 30)}")
print(f"part-2 answer: {part(valves, filter_valves(valves))}")

#(╯°□°）╯︵ ┻━┻