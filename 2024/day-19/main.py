from functools import cache

patterns, designs = open('input').read().split('\n\n')


@cache
def fill(d): return 1 if d == '' else 0 if len(v := [p for p in patterns.split(', ') if d.startswith(p)]) == 0 else sum([fill(d[len(p):]) for p in v])


print(sum(fill(d) > 0 for d in designs.splitlines()))
print(sum(fill(d) for d in designs.splitlines()))