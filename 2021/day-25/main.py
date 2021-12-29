from copy import deepcopy

m = [list(l.strip()) for l in open('input')]
shape, n = (len(m[0]), len(m)), 1

def step(m, moved = False):
    new_m = deepcopy(m)
    for y in range(shape[1]):
        for x in range(shape[0]):
            if m[y][x] == '>' and m[y][(x+1)%shape[0]] == '.':
                    moved = True
                    new_m[y][x] = '.'
                    new_m[y][(x+1)%shape[0]] = '>'
    m = deepcopy(new_m)
    for y in range(shape[1]):
        for x in range(shape[0]):
            if m[y][x] == 'v' and m[(y+1)%shape[1]][x] == '.':
                    moved = True
                    new_m[y][x] = '.'
                    new_m[(y+1)%shape[1]][x] = 'v'
    return moved, new_m

moved, m = step(m)
while moved:
    n += 1
    moved, m = step(m)
print(f"part-1 answer: {n}")