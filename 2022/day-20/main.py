from copy import copy

def mix(numbers, indices):
    for i in range(len(numbers)):
        if indices.index(i)+numbers[i] == 0: 
            indices.insert(len(numbers)-1, indices.pop(indices.index(i)))
        else: 
            indices.insert((indices.index(i)+numbers[i])%(len(numbers)-1), indices.pop(indices.index(i)))
    return indices

numbers = list(map(int, open("input").read().splitlines()))
solve = lambda d, n : sum(d[g] for g in list((d.index(0) + j)%len(n) for j in (1000, 2000, 3000)))
initial, indices = [o * 811589153 for o in numbers], list(range(len(numbers)))
for i in range(10):
    indices = mix(copy(initial), copy(indices))
    decrypted = [initial[j] for j in indices]

print(f"part-1 answer: {solve([numbers[j] for j in mix(copy(numbers), list(range(len(numbers))))], numbers)}")
print(f"part-2 answer: {solve(decrypted, numbers)}")