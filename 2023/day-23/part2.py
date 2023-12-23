import networkx as nx
import numpy as np
from networkx.classes.function import path_weight


def build_graph():
    adj_np = np.zeros((len(dots), len(dots)), dtype=int)
    for node in dots:
        deltas = ((0, 1), (0, -1), (-1, 0), (1, 0))
        candidates = set((node[0] + d[0], node[1] + d[1]) for d in deltas)
        for n in [c for c in candidates if c in dots]:
            adj_np[node_to_idx[node]][node_to_idx[n]] = 1
            adj_np[node_to_idx[n]][node_to_idx[node]] = 1
    return nx.from_numpy_array(adj_np, create_using=nx.MultiGraph)


lines = [l.strip() for l in open("example").readlines()]
rows, cols = len(lines), len(lines[0])
dots = set((r, c) for r in range(len(lines)) for c in range(len(lines[0])) if (s := lines[r][c]) != "#")
node_to_idx = {n: i for i, n in enumerate(dots)}
G = build_graph()

removed = True
while removed:
    removed = False
    for n in G.nodes():
        if len(list(G.neighbors(n))) == 2:
            a, b = list(G.neighbors(n))
            G.add_edge(a, b, weight=sum(G[c][n][0]["weight"] for c in (a, b)))
            G.remove_node(n)
            removed = True
            break

all_path = nx.all_simple_paths(G, node_to_idx[(0, 1)], node_to_idx[(rows - 1, cols - 2)])
print(max(path_weight(G, p, "weight") for p in all_path))
