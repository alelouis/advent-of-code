from functools import lru_cache


@lru_cache
def ways(springs, groups):
    if len(groups) == 0:
        return len(springs) == 0 or all(s in ["?", "."] for s in springs)
    elif len(springs) == 0:
        return 0
    elif springs[0] == "?":
        return sum(ways(f"{c}{springs[1:]}", groups) for c in [".", "#"])
    elif springs[0] == ".":
        return ways(springs[1:], groups)
    elif springs[0] == "#":
        if not all(s in ["?", "#"] for s in springs[: groups[0]]):
            return 0
        elif len(springs) > groups[0]:
            if springs[groups[0]] == "#":
                return 0
            if springs[groups[0]] in ["?", "."]:
                return ways(springs[1 + groups[0] :], groups[1:])
        elif len(springs) < groups[0]:
            return 0
        elif len(springs) == groups[0]:
            return ways(springs[groups[0] :], groups[1:])


lines = [((list(l.split(" ")[0])), list(map(int, l.split(" ")[1].strip().split(",")))) for l in open("input").readlines()]
part_1 = part_2 = 0

for springs, contiguous in lines:
    part_1 += ways("".join(springs), tuple(contiguous))
    part_2 += ways("?".join(["".join(springs)] * 5), tuple(contiguous * 5))

print(part_1)
print(part_2)
