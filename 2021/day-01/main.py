lines = [int(line) for line in open('input')]

def solve_1(lines):
    return sum([j > i for i, j in zip(lines, lines[1:])])

def solve_2(lines):
    return solve_1([sum(g) for g in zip(*[lines[i:] for i in range(3)])])

print(f'part-1 answer : {solve_1(lines)}')
print(f'part-2 answer : {solve_2(lines)}')