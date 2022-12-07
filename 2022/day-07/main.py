from collections import defaultdict

f, dirs, cts = open("input"), [], defaultdict(list)

for line in f.read().splitlines():
    cwd = "/".join(dirs)
    match line.split():
        case ["$", "cd", ".."]: dirs.pop()
        case ["$", "cd", d]: dirs.append(d)
        case ["$", "ls"]: pass
        case [a, b]: cts[cwd].append([a, f"{cwd}/{b}"] if a == "dir" else [a, b])

def local_sum(cts, folder, memo):
    s = sum(local_sum(cts, c[1], memo) if c[0] == "dir" else int(c[0]) for c in cts[folder])
    memo[folder] = s
    return s

memo = {}
local_sum(cts, "/", memo)

print(f"part-1 answer: {sum(v for k, v in memo.items() if v <= 1e5)}")
print(f"part-2 answer: {min([v for k, v in memo.items() if (7e7 - memo['/'] + v) >= 3e7])}")