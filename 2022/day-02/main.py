rds = [r.split(' ') for r in open('input').read().splitlines()]

s = {'X': 1, 'Y': 2, 'Z': 3}
l, d, w = [['B', 'X'], ['C', 'Y'], ['A', 'Z']], [['A', 'X'], ['B', 'Y'], ['C', 'Z']], [['C', 'X'], ['A', 'Y'], ['B', 'Z']]

part1 = sum([(p + s[r[1]]) if r in i else 0 for p, i in zip((0, 3, 6), (l, d, w)) for r in rds])
find = lambda i, r: [p[1] for p in i if p[0]==r[0]][0]
part2 = sum([(p + s[find(i, r)]) if r[1] == t else 0 for p, i, t in zip((0, 3, 6), (l, d, w), ('X', 'Y', 'Z')) for r in rds])

print(f'part-1 answer : {part1}')
print(f'part-2 answer : {part2}')