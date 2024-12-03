from re import finditer
from math import prod

ops, r = open("input").read(), r'mul\((\d+),(\d+)\)'
solve = lambda p: sum(prod(map(int, m.groups())) for m in finditer(r, ops) if p == 1 or ((ss := ops[:m.start()]).rfind("do()") >= ss.rfind("don't()")))
print(solve(1))
print(solve(2))