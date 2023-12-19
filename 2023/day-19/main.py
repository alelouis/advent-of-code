from math import prod
from collections.abc import Iterable


def invert(cond):
    return cond.replace('<', '>=') if '<' in cond else cond.replace('>', '<=')


def get_value(cond):
    return [int(cond.split(c + '=')[1]) if '=' in cond else int(cond.split(c)[1]) for c in ['>', '<'] if c in cond][0]


def flatten(xs):
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x


def clean_paths(paths):
    for p in paths:
        while 'end' in p:
            p.pop(p.index('end'))
    return paths


def get_workflows(instructions):
    workflows = {}
    for inst in instructions:
        name, workflow = inst.split('{')
        workflow = workflow[:-1].split(',')
        workflows[name] = [tuple(cond.split(':')) for cond in workflow[0:-1]] + [('end', workflow[-1])]
    return workflows


def process_workflow(name, part):
    for condition, ret in workflows[name]:
        if condition == 'end':
            return ret
        else:
            if eval(f"{part[condition[0]]}{condition[1:]}"):
                return ret


def process_part(part):
    ret, name = None, 'in'
    while name not in "AR":
        name = process_workflow(name, part)
    return name


def branching(name, conditions):
    if name in 'AR':
        return conditions + [name]
    else:
        return [branching(n, c) for n, c in zip([w[1] for w in workflows[name]], [
            conditions + [f'{invert(c)}' for c in [w[0] for w in workflows[name]][0:idx]] + [condition] for
            idx, (condition, ret) in enumerate(workflows[name])])]


def compute_combinations(A_path):
    combinations = 0
    for p in A_path:
        ranges = {c: [1, 4000] for c in 'xmas'}
        for cond in p[:-1]:
            for idx, (v, s) in enumerate(zip(ranges[cond[0]], [1, -1])):
                comp = f'{v}{cond[1:]}'
                if not eval(comp):
                    ranges[cond[0]][idx] = int(get_value(comp)) + s * (0 if "=" in comp else 1)
        combinations += prod(v[1] - v[0] + 1 for v in ranges.values())
    return combinations


def part1():
    return sum(sum(part.values()) for part in parts if process_part(part) == 'A')


def part2():
    flat_path = list(flatten(branching('in', [])))
    ar_indices = [-1] + [i for i in range(len(flat_path)) if flat_path[i] in 'AR']
    A_path = clean_paths(
        [p for p in [flat_path[i + 1:j + 1] for i, j in zip(ar_indices, ar_indices[1:])] if p[-1] == "A"])
    return compute_combinations(A_path)


instructions, parts = [l.split('\n') for l in open('input').read().split('\n\n')]
workflows = get_workflows(instructions)
parts = [eval(f"dict({p[1:-1]})") for p in parts]

print(part1())
print(part2())
