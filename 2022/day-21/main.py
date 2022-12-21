import networkx as nx
from sympy import sympify, solve

def graph_solve(part):
    g, e, out = nx.DiGraph(), [], {}
    for node in nodes:
        l, r = node.split(": ")
        if r.isnumeric(): out.update({l: "x" if part == 2 and l == 'humn' else r})
        else:
            out.update({l: {"op": "==" if part == 2 and l == 'root' else r[5], "l": r[0:4], "r": r[7:]}})
            e.extend([(r[7:], l), (r[0:4], l)])
    g.add_edges_from(e)
    for node in list(nx.topological_sort(g)):
        if isinstance(out[node], dict): out[node] = f"({out[out[node]['l']]}{out[node]['op']}{out[out[node]['r']]})" 
    return out

nodes = open("input").read().splitlines()
print(int(eval(graph_solve(part=1)['root'])))
print(solve(sympify(graph_solve(part=2)["root"].split("==")[0][1:]) - sympify(graph_solve(part=2)["root"].split("==")[1][:-1]))[0])