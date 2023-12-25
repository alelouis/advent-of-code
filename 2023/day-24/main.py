import sympy


def crossing_point(line_0, line_1):
    pos_0, vel_0 = line_0  # ax + c
    pos_1, vel_1 = line_1  # bx + d
    a = vel_0[1] / vel_0[0]
    c = pos_0[1] - a * pos_0[0]
    b = vel_1[1] / vel_1[0]
    d = pos_1[1] - b * pos_1[0]
    if a - b == 0:
        return float("inf"), float("inf")
    else:
        x = (d - c) / (a - b)
        y = a * x + c
        return x, y


def delta(p0, p1):
    return p0[0] - p1[0], p0[1] - p1[1]


def scalar(v0, v1):
    return v0[0] * v1[0] + v0[1] * v1[1]


def find_crossing():
    test_area, crossed = [200000000000000, 400000000000000], 0
    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            line_0 = pos[i], vel[i]
            line_1 = pos[j], vel[j]
            x, y = crossing_point(line_0, line_1)
            if test_area[0] <= x <= test_area[1] and test_area[0] <= y <= test_area[1]:
                s0 = scalar(delta(line_0[0], (x, y)), line_0[1])
                s1 = scalar(delta(line_1[0], (x, y)), line_1[1])
                crossed += all(s < 0 for s in (s0, s1))
    return crossed


def oops():
    xi, yi, zi = sympy.var("xi"), sympy.var("yi"), sympy.var("zi")
    vxi, vyi, vzi = sympy.var("vxi"), sympy.var("vyi"), sympy.var("vzi")
    t1, t2, t3 = sympy.var("t1"), sympy.var("t2"), sympy.var("t3")
    equations = []
    for t, p, v in zip([t1, t2, t3], pos[0:3], vel[0:3]):
        equations.append(sympy.Eq(xi + t * vxi, p[0] + v[0] * t))
        equations.append(sympy.Eq(yi + t * vyi, p[1] + v[1] * t))
        equations.append(sympy.Eq(zi + t * vzi, p[2] + v[2] * t))
    return sum(sympy.solve(equations)[0][k] for k in (xi, yi, zi))


lines = [l.strip().split(" @ ") for l in open("input").readlines()]
pos, vel = [], []
for l in lines:
    p, v = (list(map(int, l[i].split(", "))) for i in [0, 1])
    pos.append(p)
    vel.append(v)

print(find_crossing())
print(oops())
