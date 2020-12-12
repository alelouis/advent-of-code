from math import cos, sin, radians

instructions = [[l[0], int(l[1:])] for l in open('input')]
n, e, a = 0, 0, 0
for cmd, k in instructions:
    n += (cmd == 'N')*k - (cmd == 'S')*k - (cmd == 'F')*k*sin(radians(a))
    e += (cmd == 'E')*k - (cmd == 'W')*k + (cmd == 'F')*k*cos(radians(a))
    a += (cmd == 'R')*k - (cmd == 'L')*k
print(f'part-1 answer: {int(abs(n) + abs(e))}')

wn, we, n, e = 1, 10, 0, 0
for cmd, k in instructions:
    wn += (cmd == 'N')*k - (cmd == 'S')*k
    we += (cmd == 'E')*k - (cmd == 'W')*k
    n, e = n+(cmd == 'F')*k*wn, e+(cmd == 'F')*k*we
    if cmd == 'L' or cmd == 'R':
        k = k if cmd == 'R' else -k
        _wn = round(wn*cos(radians(k)) - we*sin(radians(k)))
        _we = round(wn*sin(radians(k)) + we*cos(radians(k)))
        wn, we = _wn, _we
print(f'part-2 answer: {int(abs(n) + abs(e))}')