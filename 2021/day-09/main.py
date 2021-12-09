lines = [list(map(int, list(l.rstrip()))) for l in open('input')]
s = (len(lines), len(lines[0]))
m = [[9 for _ in range(s[1]+2)] for _ in range(s[0]+2)]
chks = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for i in range(s[0]):
    for j in range(s[1]):
        m[1+i][1+j] = lines[i][j]

def find_lows(m):
    lows = [[i, j] for i in range(1, s[0]+1) for j in range(1, s[1]+1) if all([m[i][j] < m[i+x][j+y] for x, y in chks])]
    risk = sum([1 + m[i][j] for i,j in lows])
    return lows, risk

def spread(m, i, j):
    next = [[i+d[0], j+d[1]] for d in chks if m[i+d[0]][j+d[1]] != 9]
    for p in (next + [[i, j]]): m[p[0]][p[1]] = 9
    return 1 if next == [] else 1+sum([spread(m, n[0], n[1]) for n in next]) 

lows, risk = find_lows(m)
bassins = sorted([spread(m, p[0], p[1]) for p in lows])

print(f'part-1 answer : {risk}')
print(f'part-2 answer : {bassins[-1]*bassins[-2]*bassins[-3]}')