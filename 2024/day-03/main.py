from re import finditer
from math import prod

ops, r = open("input").read(), r'mul\((\d+),(\d+)\)'
solve = lambda p: sum(prod(map(int, m.groups())) for m in finditer(r, ops) if p == 1 or (ops.rfind("do()", 0, s := m.start()) >= ops.rfind("don't()", 0, s)))
print(solve(1))
print(solve(2))