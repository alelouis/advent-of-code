import itertools, re, collections as c


sch = [["."] + [d for d in l.strip()] + ["."] for l in open("input").readlines()]
sch.insert(0, ["."] * len(sch[0]))
sch.append(["."] * len(sch[0]))
sch_str, s, gears = "".join(list(itertools.chain(*sch))), 0, c.defaultdict(list)

for num in set(re.findall(r"\d+", sch_str)):
    pos = [p.start() for p in re.finditer(f"[^0-9]{num}[^0-9]", sch_str)]
    iss, jss = [p % len(sch[0]) + 1 for p in pos], [p // len(sch[0]) for p in pos]
    for i, j in zip(iss, jss):
        idx = [(m, n) for m in [j - 1, j + 1] for n in range(i - 1, i + len(num) + 1)]
        idx += [(j, i - 1), (j, i + len(num))]
        neigh = [sch[k][l] for k, l in idx]
        if "*" in neigh:
            gears[",".join(map(str, idx[neigh.index("*")]))].append(int(num))
        s += int(num) * (not all(n == "." for n in neigh))

print(s)
print(sum(v[0] * v[1] for _, v in gears.items() if len(v) == 2))
