from copy import deepcopy as dc

lines = [l.rstrip().split('-') for l in open('example')]
counts, ways = {}, {}

for a, b in lines: 
    ways[a] = {b} if a not in ways else ways[a].union({b})
    ways[b] = {a} if b not in ways else ways[b].union({a})
    counts[a] = counts[b] = 0

for way in ways.keys(): ways[way].discard('start')

def find_path(ways, cave, counts, part):
    if cave.islower():
        counts[cave] += 1
        if any([counts[c] >= part for c in counts]):
            for way in ways.keys():
                for c in counts: 
                    if counts[c] > 0: ways[way].discard(c)
    if cave == 'end': return 1
    elif ways[cave] == set(): return 0
    else: return sum([find_path(dc(ways), p, dc(counts), part) for p in ways[cave]])

print(f"part-1 answer : {find_path(dc(ways), 'start', dc(counts), 1)}")
print(f"part-2 answer : {find_path(dc(ways), 'start', dc(counts), 2)}")