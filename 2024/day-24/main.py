import networkx as nx

inits, gates = open("input").read().split("\n\n")
inits = {init.split(": ")[0]: bool(int(init.split(": ")[1])) for init in inits.splitlines()}

G = nx.DiGraph()

for i in inits:
    G.add_node(i)

for g in gates.splitlines():
    left, right = g.split(" -> ")
    arg1, op, arg2 = left.split(" ")
    G.add_node(arg1)
    G.add_node(arg2)
    G.add_node(right, op=op)
    G.add_edge(arg1, right)
    G.add_edge(arg2, right)

values = {n: v for n, v in inits.items()}
for n in nx.topological_sort(G):
    if n not in values:
        op = G.nodes[n]["op"]
        arg1, arg2 = [a[0] for a in G.in_edges(n)]
        match op:
            case "AND": out = values[arg1] & values[arg2]
            case "OR":  out = values[arg1] | values[arg2]
            case "XOR": out = values[arg1] ^ values[arg2]
            case _: raise Exception()
        values[n] = out


outs_nodes = sorted([z for z in values if z.startswith("z")])[::-1]
out_number_bool = "".join(['1' if values[o] else '0' for o in outs_nodes])
out_number_int = int(out_number_bool, 2)

print(out_number_int)

swaps = []
for n in G.nodes(data=True):
    prev = list(c[0] for c in G.in_edges(n[0]))
    next = list(c[1] for c in G.out_edges(n[0]))
    if n[0].startswith('z') and n[1]['op'] != 'XOR' and n[0] != 'z45':
        swaps.append(n[0])
    if 'op' in n[1] and n[1]['op'] == 'XOR':
        if all(c[0][0] not in ["x", "y", "z"] for c in prev + [n[0]]):
            swaps.append(n[0])
        if all(c[0][0] in 'xy' for c in prev) and not n[0].startswith('z') and all(c[1:] != '00' for c in prev):
            if "XOR" not in [r['op'] for r in [G.nodes[h] for h in next]]:
                swaps.append(n[0])
    if 'op' in n[1] and n[1]['op'] == 'AND':
        if all(c[0][0] in 'xy' for c in prev) and all(c[1:] != '00' for c in prev):
            if "OR" not in [r['op'] for r in [G.nodes[h] for h in next]]:
                swaps.append(n[0])

print(",".join(sorted(list(set(swaps)))))