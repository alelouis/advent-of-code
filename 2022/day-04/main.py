data = [[list(map(int, d.split('-'))) for d in l.split(',')] for l in open("input").read().splitlines()]
part1 = part2 = 0

for line in data:
    sets = [set(range(l[0], l[1]+1)) for l in line]
    inter = len(set.intersection(*sets))
    part1 += any([inter == len(s) for s in sets])
    part2 += inter > 0

print(f'part-1 answer : {part1}')
print(f'part-2 answer : {part2}')