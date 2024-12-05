from collections import defaultdict
from functools import cmp_to_key

rules, updates = open('input').read().split('\n\n')
rules, updates = [r.split('|') for r in rules.split('\n')], [u.split(',') for u in updates.split('\n')]

before, after = defaultdict(set), defaultdict(set)
for a, b in rules:
    before[b].add(a)
    after[a].add(b)

compare = lambda a, b: 1 if a in after[b] else -1 if a in before[b] else 0
part1 = sum(int(u[int(len(u) / 2)]) for u in updates if u == sorted(u, key=cmp_to_key(compare)))
part2 = sum(int(s[int(len(update) / 2)]) for update in updates if update != (s := sorted(update, key=cmp_to_key(compare))))

print(part1, part2)
