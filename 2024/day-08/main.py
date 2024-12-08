lines = [list(s.strip()) for s in open('input').readlines()]
rows, cols, frequencies = len(lines), len(lines[0]), set(open('input').read()) - {'\n', '.'}
nodes = {freq: set(r + 1j*c for r in range(rows) for c in range(cols) if lines[r][c] == freq) for freq in frequencies}

def find_antinodes(n_max, dirs):
    antinodes = {f: set() for f in frequencies}
    for freq in frequencies:
        for node1 in nodes[freq]:
            for node2 in nodes[freq] - {node1}:
                for dir in dirs:
                    n = 1
                    while 0 <= (node := node1 + dir * n * (node2 - node1)).real < rows and 0 <= node.imag < cols and n <= n_max:
                        antinodes[freq].add(node)
                        n += 1
    return antinodes

print(len(list(set().union(*[v for v in find_antinodes(1, [-1]).values()]))))
print(len(list(set().union(*[v for v in find_antinodes(100, [-1, 1]).values()]))))