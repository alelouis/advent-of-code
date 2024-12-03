from re import finditer as f
from math import prod as pr

o = open("input").read()
print([sum(pr(map(int, m.groups())) for m in f(r'mul\((\d+),(\d+)\)', o) if p | (o.rfind("do()", 0, s := m.start()) >= o.rfind("don't()", 0, s))) for p in [-1, 0]])