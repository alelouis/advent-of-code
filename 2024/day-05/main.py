from collections import defaultdict


def check_valid(u):
    for i in range(len(u)):
        for j in (k for k in range(len(u)) if k != i):
            if u[j] not in (before if i > j else after)[u[i]]:
                return False, (i, j)
    return True, (-1, -1)


rules, updates = open('input').read().split('\n\n')
rules, updates = [r.split('|') for r in rules.split('\n')], [u.split(',') for u in updates.split('\n')]

before, after = defaultdict(set), defaultdict(set)
for a, b in rules:
    before[b].add(a)
    after[a].add(b)

answer_valid = answer_invalid = 0
for update in updates:
    valid, (i, j) = check_valid(update)
    if valid:
        answer_valid += int(update[int(len(update) / 2)])
    else:
        while not valid:
            update[i], update[j] = update[j], update[i]
            valid, (i, j) = check_valid(update)
        answer_invalid += int(update[int(len(update) / 2)])

print(answer_valid)
print(answer_invalid)
