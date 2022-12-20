from copy import copy

def mix(num, idx):
    for i in range(len(num)):
        if idx.index(i)+num[i] == 0: idx.insert(len(num)-1, idx.pop(idx.index(i)))
        else: idx.insert((idx.index(i)+num[i])%(len(num)-1), idx.pop(idx.index(i)))
    return idx

num = list(map(int, open("input").read().splitlines()))
solve = lambda d, n : sum(d[g] for g in list((d.index(0) + j)%len(n) for j in (1000, 2000, 3000)))
init, idx = [o * 811589153 for o in num], list(range(len(num)))
for i in range(10):
    idx = mix(copy(init), copy(idx))
    decrypted = [init[j] for j in idx]

print(f"part-1 answer: {solve([num[j] for j in mix(copy(num), list(range(len(num))))], num)}")
print(f"part-2 answer: {solve(decrypted, num)}")