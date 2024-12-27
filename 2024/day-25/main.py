patterns = open("input").read().split("\n\n")
locks = []
keys = []

for p in patterns:
    lines = p.splitlines()
    tmp = [-1] * len(lines[0])
    for c in range(len(lines[0])):
        for l in lines:
            tmp[c] += l[c] == "#"
    if all(l == "#" for l in lines[0]):
        locks.append(tmp)
    else:
        keys.append(tmp)

fit = sum(not any([(a + b) >= 6 for a, b in zip(lock, key)]) for lock in locks for key in keys)
print(fit)
