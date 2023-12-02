import re


def find(e, part):
    mapp, idx, num = (
        ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
        [],
        [],
    )
    search_for = [str(i + 1) for i in range(9)] + (mapp if part == 2 else [])
    for k in search_for:
        occ = [i.start() for i in re.finditer(k, e)]
        idx.extend(occ)
        num.extend([mapp.index(k) + 1 if k in mapp else int(k)] * len(occ))
    return 10 * num[idx.index(min(idx))] + num[idx.index(max(idx))]


print(sum([find(e, part=1) for e in open("input").readlines()]))
print(sum([find(e, part=2) for e in open("input").readlines()]))
