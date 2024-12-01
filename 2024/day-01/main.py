pairs = [sorted([int(p.rstrip().split('   ')[i]) for p in open('input').readlines()]) for i in [0, 1]]

print(sum(abs(p0 - p1) for p0, p1 in zip(*pairs)))
print(sum(p0 * pairs[1].count(p0) for p0 in pairs[0]))