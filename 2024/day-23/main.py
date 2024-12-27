import networkx as nx

data = open("input").readlines()

G = nx.Graph()
for link in data:
    c1, c2 = link.strip().split("-")
    G.add_nodes_from([c1, c2])
    G.add_edge(c1, c2)

cliques = list(nx.enumerate_all_cliques(G))
print(len([c for c in cliques if len(c) == 3 and any([p[0] == "t" for p in c])]))
print(",".join(sorted(cliques[-1])))
