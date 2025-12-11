def dfs(graph, node, target, part, dac, fft, path, cache):
    if (node, dac, fft) in cache:
        return cache[(node, dac, fft)]

    path = path + [node]
    dac, fft = 'dac' in path, 'fft' in path
    if node == target:
        return (dac and fft) if part == 2 else 1
    cache[(node, dac, fft)] = sum(dfs(graph, node, target, part, dac, fft, path, cache) for node in graph[node] if node not in path)
    return cache[(node, dac, fft)]

devices = {d.split(':')[0]:d.split(':')[1].split() for d in open('input').readlines()}
print(dfs(devices, 'you', 'out', 1, False, False, [], {}))
print(dfs(devices, 'svr', 'out', 2, False, False, [], {}))