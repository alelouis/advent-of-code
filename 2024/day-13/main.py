import re
from ortools.linear_solver import pywraplp


def solve(xa, xb, ya, yb, xprize, yprize, part):
    solver = pywraplp.Solver.CreateSolver("SCIP_MIXED_INTEGER_PROGRAMMING")
    a = solver.IntVar(0.0, solver.infinity(), "a")
    b = solver.IntVar(0.0, solver.infinity(), "b")
    solver.Add(a * xa + b * xb == xprize + (part == 2) * 10000000000000)
    solver.Add(a * ya + b * yb == yprize + (part == 2) * 10000000000000)
    solver.Minimize(b + 3 * a)
    status = solver.Solve()
    return int(solver.Objective().Value()) if status == pywraplp.Solver.OPTIMAL else 0


def parse(text):
    res = {}
    for match in re.findall(r'(\w+):\s*(?:X\+?(\d+),?\s*Y\+?(\d+)|X=(\d+),?\s*Y=(\d+))', text):
        x, y = (int(match[1]), int(match[2])) if (match[1] and match[2]) else (int(match[3]), int(match[4]))
        res[f"x{match[0].lower()}"], res[f"y{match[0].lower()}"] = x, y
    return res


machines = [parse(m) for m in open('test').read().split('\n\n')]
print(sum([solve(**machine, part=1) for machine in machines]))
print(sum([solve(**machine, part=2) for machine in machines]))
