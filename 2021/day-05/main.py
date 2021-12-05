lines = [l.rstrip().split(' -> ') for l in open('input') if l != '\n']
lines = list(map(lambda x: [x[0].split(','), x[1].split(',')], lines))
vents = [[0 for _ in range(1000)] for _ in range(1000)]

for l in lines:
    x1, x2, y1, y2 = int(l[0][0]), int(l[1][0]), int(l[0][1]), int(l[1][1])
    x = list(range(x1, x2 + (-1 if x1 > x2 else 1), -1 if x1 > x2 else 1))
    y = list(range(y1, y2 + (-1 if y1 > y2 else 1), -1 if y1 > y2 else 1))
    if x1 == x2:
        for i in range(len(y)): vents[x1][y[i]] += 1
    elif y1 == y2:
        for i in range(len(x)): vents[x[i]][y1] += 1
    else:                                              # part 2
        for i in range(len(x)): vents[x[i]][y[i]] += 1 # part 2

print(f'part-1/2 answer : {sum([x > 1 for l in vents for x in l])}')