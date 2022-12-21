import networkx as nx
from sympy import sympify, solve

def graph_solve(part):
    g = nx.DiGraph()
    e, out = [], {}
    for node in nodes:
        l, r = node.split(": ")
        if r.isnumeric():
            if part == 2 and l == 'humn': r = "x"
            out.update({l: r})
        else:
            pl, pr, op = r[0:4], r[7:], r[5]
            if part == 2 and l == 'root': op = "=="
            out.update({l: {"op": op, "l": pl, "r": pr}})
            e.extend([(pr, l), (pl, l)])
    g.add_edges_from(e)
    for node in list(nx.topological_sort(g)):
        if isinstance(out[node], dict):
            op, l, r = out[node]["op"], out[node]["l"], out[node]["r"]
            out[node] = f"({out[l]}{op}{out[r]})" 
    return out

nodes = open("input").read().splitlines()
print(int(eval(graph_solve(part=1)['root'])))
out = graph_solve(part=2)
print(solve(sympify(out["root"].split("==")[0][1:]) - sympify(out["root"].split("==")[1][:-1]))[0])