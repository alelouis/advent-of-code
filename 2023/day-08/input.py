import math, sys
sys.setrecursionlimit(50000)

def walk_from(end, n, ns, s=0):
    return s if end(n) else walk_from(end, ns[n][0] if insts[s % (len(insts) - 1)] == 'L' else ns[n][1], ns, s + 1)

insts, _, *maps = open('input').readlines()
nodes = {(a := m.split(' = '))[0]: (a[1].strip()[1:-1].split(', ')) for m in maps}

print(walk_from(lambda x: x == 'ZZZ', 'AAA', nodes, 0))
print(math.lcm(*[walk_from(lambda x: x[-1] == 'Z', n, nodes, 0) for n in [n for n in nodes if n[-1] == 'A']]))
