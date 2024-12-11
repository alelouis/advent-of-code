# or just use functools.cache instead of memo dict
def count(stone, step, max_steps, memo):
    if step == max_steps:
        return 1
    else:
        if (stone, step) in memo:
            return memo[(stone, step)]
        if stone == 0:
            memo[(stone, step)] = count(1, step + 1, max_steps, memo)
        elif len(str_stone := str(stone)) % 2 == 0:
            left, right = int(str_stone[0:len(str_stone) // 2]), int(str_stone[len(str_stone) // 2:])
            memo[(stone, step)] = count(left, step + 1, max_steps, memo) + count(right, step + 1, max_steps, memo)
        else:
            memo[(stone, step)] = count(stone * 2024, step + 1, max_steps, memo)
        return memo[(stone, step)]


stones = list(map(int, open('input').read().strip().split(' ')))
print(sum(count(s, 0, 25, {}) for s in stones))
print(sum(count(s, 0, 75, {}) for s in stones))
