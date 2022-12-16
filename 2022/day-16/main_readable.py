from itertools import combinations


def parse(line):
    return (
        line[1],
        int(line[4].split("=")[1][:-1]),
        eval(str(list(map(lambda x: x.rstrip(","), line[9:])))),
    )


def get_valves(lines):
    valves = {
        parse(line)[0]: {"tunnels": parse(line)[2], "rate": parse(line)[1]}
        for line in lines
    }
    return valves


def filter_valves(valves):
    return set(k for k, v in valves.items() if v["rate"] > 0)


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


def max_brute(current, targets, minute, score, path, max_value):
    if minute > max_value or targets == set():
        return score
    else:
        return max(
            max_brute(
                target,
                targets - {target},
                minute + distances[f"{current}_{target}"] + 1,
                score
                + valves[target]["rate"]
                * (
                    max_value
                    - min(max_value, minute + distances[f"{current}_{target}"])
                ),
                path + [target],
                max_value,
            )
            for target in targets
        )


def partition_brute(valves, valves_filtered):
    m = 0
    for r in range(2, len(valves) // 2):
        for c in combinations(valves_filtered, r):
            m = max(
                m,
                max_brute("AA", valves_filtered - set(c), 1, 0, ["AA"], 26)
                + max_brute("AA", set(c), 1, 0, ["AA"], 26),
            )
    return m


valves = get_valves(list(map(lambda l: l.split(" "), open("test").read().splitlines())))
distances = {f"{k1}_{k2}": bfs(valves, k1, k2) for k2 in valves for k1 in valves}
print(f"part-1 answer: {max_brute('AA', filter_valves(valves), 1, 0, ['AA'], 30)}")
print(f"part-2 answer: {partition_brute(valves, filter_valves(valves))}")
