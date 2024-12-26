from collections import defaultdict


def mix(secret, number):
    return secret ^ number


def prune(secret):
    return secret % 16777216


def next_secret(secret):
    mul = secret * 64
    secret = prune(mix(secret, mul))
    secret = prune(secret)
    div = secret // 32
    secret = prune(mix(secret, div))
    mul = secret * 2048
    secret = prune(mix(secret, mul))
    return secret


data = [int(i) for i in open("input").readlines()]
part1 = 0
secrets, cycles, diffs = defaultdict(list), defaultdict(list), defaultdict(list)
for s in data:
    ns = s
    cycles[s].append(int(str(s)[-1]))
    for i in range(2000):
        ns = next_secret(ns)
        cycles[s].append(int(str(ns)[-1]))
        secrets[s].append(ns)
    part1 += ns
    diffs[s] = [b - a for a, b in zip(cycles[s], cycles[s][1:])]

sequences = set()
for s in data:
    sequences |= set(tuple(diffs[s][i : i + 4]) for i in range(len(diffs[s]) - 4))

max_banana = defaultdict(int)
for s in data:
    patterns = set()
    for i in range(len(cycles[s]) - 4):
        pattern = tuple(diffs[s][i : i + 4])
        if pattern not in patterns:
            patterns.add(pattern)
            max_banana[pattern] += cycles[s][i + 4]


print(part1)
print(max(max_banana.values()))
