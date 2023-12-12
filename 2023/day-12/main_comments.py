# Using memoization for recursive calls caching.
# The dict memo maps (springs, groups) input arguments to return calls.


def ways(memo, springs, groups):
    # If already computed this set of arguments, return stored value
    if (springs, groups) in memo:
        return memo[(springs, groups)]
    if len(groups) == 0:
        # If no group left, check that the springs are empty or that the remaining characters are not #
        memo[(springs, groups)] = len(springs) == 0 or all(s in ["?", "."] for s in springs)
        return memo[(springs, groups)]
    # If there are remaining groups but no character, can't be a solution
    elif len(springs) == 0:
        memo[(springs, groups)] = 0
        return memo[(springs, groups)]
    # If there are still groups and springs
    elif springs[0] == "?":
        # If on a ?, count ways of doing branches from . and #
        memo[(springs, groups)] = sum(ways(memo, f"{c}{springs[1:]}", groups) for c in [".", "#"])
        return memo[(springs, groups)]
    elif springs[0] == ".":
        # If on a ., just skip it and process remaining string
        memo[(springs, groups)] = ways(memo, springs[1:], groups)
        return memo[(springs, groups)]
    elif springs[0] == "#":
        if not all(s in ["?", "#"] for s in springs[: groups[0]]):
            # If springs in current group length are not # or ?, can't be a solution
            memo[(springs, groups)] = 0
            return memo[(springs, groups)]
        elif len(springs) > groups[0]:
            # If all # or ? AND a character after the current group
            if springs[groups[0]] == "#":
                # The group would be larger and groups[0], can't be a solution
                memo[(springs, groups)] = 0
                return memo[(springs, groups)]
            if springs[groups[0]] in ["?", "."]:
                # If next character is a potential . validate group and process remaining .
                memo[(springs, groups)] = ways(memo, springs[1 + groups[0] :], groups[1:])
                return memo[(springs, groups)]
        elif len(springs) < groups[0]:
            # If the length of the string is inferior to the length group, can't be a solution
            memo[(springs, groups)] = 0
            return memo[(springs, groups)]
        elif len(springs) == groups[0]:
            # If equal, validate group
            memo[(springs, groups)] = ways(memo, springs[groups[0] :], groups[1:])
            return memo[(springs, groups)]


lines = [((list(l.split(" ")[0])), list(map(int, l.split(" ")[1].strip().split(",")))) for l in open("input").readlines()]
part_1 = part_2 = 0
memo = dict()
for springs, contiguous in lines:
    part_1 += ways(dict(), "".join(springs), tuple(contiguous))
    part_2 += ways(dict(), "?".join(["".join(springs)] * 5), tuple(contiguous * 5))

print(part_1)
print(part_2)
