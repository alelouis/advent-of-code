from functools import reduce
from itertools import combinations
from ortools.linear_solver import pywraplp


def multi_xor(strs):
    y = reduce(lambda x, y: x ^ y, [int(x, 2) for x in strs])
    return format(y, f'0{len(strs[0])}b')


def light2bin(light):
    return light[1:-1].replace('.', '0').replace('#', '1')


def button2bin(buttons, size):
    return [''.join(['1' if str(i) in set(button[1:-1].split(',')) else '0' for i in range(size)]) for button
                     in buttons]


def find_combination(buttons, light_bin):
    for r in range(1, len(buttons)):
        for c in combinations(buttons, r):
            if multi_xor(c) == light_bin:
                return r


machines = [l.strip().split() for l in open('input').readlines()]
solver = pywraplp.Solver.CreateSolver("SAT")

part_1 = part_2 = 0
for machine in machines:
    light, *buttons, joltages = machine
    light, buttons, joltages = light2bin(light), button2bin(buttons, len(light) - 2), list(map(int, (joltages[1:-1].split(','))))
    bvar = {i: solver.IntVar(0, solver.infinity(), f"(b{i})") for i in range(len(buttons))}
    for p in range(len(joltages)):
        solver.Add(sum(bvar[i] for i in range(len(buttons)) if int(buttons[i][p])) == joltages[p])
    solver.Minimize(sum(b for b in bvar.values()))
    solver.Solve()
    part_1 += find_combination(buttons, light)
    part_2 += solver.Objective().Value()

print(part_1, int(part_2))
