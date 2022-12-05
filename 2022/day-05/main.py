import re
from copy import deepcopy as dc

def solve(part, stacks, instructions):
    for instruction in instructions:
        moves, fro, to = list(map(int, re.findall(r'\d+', instruction)))
        stacks[to-1] += [stacks[fro-1].pop() for _ in range(moves)][::part]
    return ''.join([stacks[i].pop() for i in stacks])

part, rows, cols = 1, 8, 9
lines = open('input').readlines()
crates = [[l[2*i+1] for i in range(2*cols-1)] for l in lines[:rows]]
stacks = {k//2: [crates[j][k] for j in range(rows) if crates[j][k].isalpha()][::-1] for k in range(0, cols*2, 2)}

print(solve(1, dc(stacks), dc(lines[rows+2:])))
print(solve(-1, dc(stacks), dc(lines[rows+2:])))