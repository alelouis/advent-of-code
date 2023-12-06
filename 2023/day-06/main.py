from math import sqrt, ceil, floor, prod

def above_roots(time, distance):
    return sum([sign * f((-time + sign * sqrt(time**2 - 4 * distance)) / 2) for f, sign in zip([ceil, floor], [1, -1])]) - 1

times, distances = [[int(t) for t in l.split(":")[1].strip().split(" ") if t.isdigit()] for l in open("input").readlines()]
print(prod(above_roots(*td) for td in zip(times, distances)))
print(above_roots(*(int("".join(map(str, k))) for k in (times, distances))))
