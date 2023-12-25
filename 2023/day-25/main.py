import networkx as nx
import random

lines, c, g = [l.strip().split(": ") for l in open("input").readlines()], 0, nx.Graph()

for left, right in lines:
    for r in right.split(" "):
        g.add_edge(left, r, capacity=1)

while c != 3:
    c, p = nx.minimum_cut(g, *random.sample(list(g.nodes()), k=2))

print(len(p[0]) * len(p[1]))
