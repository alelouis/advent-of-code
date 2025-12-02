def is_periodic(s, part):
    divisors = [d for d in range(1, len(s)) if len(s) % d == 0 and (part == 2 or len(s) / d == 2)]
    for d in divisors:
        if all(len(set(s[i] for i in range(p, len(s), d))) == 1 for p in range(d)):
            return True
    return False


def solve(part):
    id_ranges, total = open("input").read().split(","), 0
    for id_range in id_ranges:
        id_min, id_max = [int(i) for i in id_range.split("-")]
        for i in range(id_min, id_max + 1):
            total += i if is_periodic(str(i), part) else 0
    return total


print(solve(1), solve(2))
