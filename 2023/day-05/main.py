def parse(input_name):
    almanac = almanac_ranges = dict()
    for idx, section in enumerate(open(input_name).read().split("\n\n")):
        lines = section.splitlines()
        if idx == 0:
            seeds = list(map(int, lines[0].split(": ")[1].split(" ")))
        else:
            header = lines[0].split(" ")[0]
            almanac[header] = [list(map(int, l.split(" "))) for l in lines[1:]]
            almanac_ranges[header] = [[s, s + l - 1, d - s] for d, s, l in almanac[header]]
    return seeds, almanac_ranges


def convert(number, source, destination, almanac):
    for start, end, delta in almanac[f"{source}-to-{destination}"]:
        if start <= number <= end:
            return number + delta
    return number


def convert_interval(interval, conversion, almanac):
    return [
        convert(interval[0], *conversion.split("-to-"), almanac),
        1 + convert(interval[1] - 1, *conversion.split("-to-"), almanac),
    ]


def intersect(starts, ends):
    inter = [max(starts), min(ends)]
    return [] if inter[1] < inter[0] else inter


def merge(min_v, max_v, intervals):
    bounds = [min_v, max_v]
    for i in intervals:
        bounds.extend([i[0], min(i[1] + 1, max_v)])
    return [[p, q] for p, q in zip(sorted(set(bounds)), sorted(set(bounds))[1:])]


def solve(part):
    seeds, almanac, minimums = *parse("input"), []
    for start, lenght in zip(seeds[::2], seeds[1::2]):
        intervals = [[start, start + (1 if part == 1 else lenght)]]
        for c in almanac:
            bounds = []
            for i in intervals:
                bounds += merge(*i, [k for a, b, _ in almanac[c] if len(k := intersect([a, i[0]], [b, i[1] - 1]))])
            intervals = [convert_interval(inter, c, almanac) for inter in bounds]
        minimums.append(min([min(p) for p in intervals]))
    return min(minimums)


print(solve(1))
print(solve(2))
