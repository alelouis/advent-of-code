import networkx as nx  # booooooooooooooooo

dist = lambda b1, b2 : sum((a - b) ** 2 for a, b in zip(b1, b2))
box = [tuple(map(int, l.strip().split(','))) for l in open('input').readlines()]
distance_matrix = {(box[i], box[j]): dist(box[i], box[j]) for i in range(len(box)) for j in range(i + 1, len(box))}
sorted_box = sorted(distance_matrix.items(), key=lambda item: item[1])
edges = [d[0] for d in sorted_box]

def part1():
    cc = [len(c) for c in sorted(nx.connected_components(nx.from_edgelist(edges[:1000])), key=len, reverse=True)]
    return cc[0] * cc[1] * cc[2]

def part2():
    low, high, n_pairs = len(box), len(box) ** 2, 0
    while low <= high:
        mid = (low + high) // 2
        cc = len(sorted(nx.connected_components(nx.from_edgelist(edges[:mid + 1])), key=len, reverse=True)[0])
        if cc == len(box):
            n_pairs = mid
            high = mid - 1
        elif cc < len(box): low = mid + 1
        else: high = mid - 1
    return sorted_box[n_pairs][0][0][0] * sorted_box[n_pairs][0][1][0]

print(part1(), part2())
