ranges, ids = [x.split('\n') for x in open('input').read().split('\n\n')]
ranges, ids = [(map(int, r.split('-'))) for r in ranges], [*map(int, ids)]

def part1():
    return sum(any(l <= iid <= h for (l, h) in ranges) for iid in ids)

def part2():
    minimum = total = 0
    for s, e in sorted(ranges):
        if e >= minimum:
            total += e - max(minimum, s) + 1
            minimum = e + 1
    return total

print(part1(), part2())