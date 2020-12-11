import copy

def rules(s, p):
    ns, b = copy.deepcopy(s), False
    for y in range(1, len(s[0])-1):
        for x in range(1, len(s)-1):
            a = sum([s[x+k[0]][y+k[1]]=='#' for k in d]) if p == 1 else seat_in_sight(s, x, y)
            if s[x][y] == 'L' and a == 0: ns[x][y], b = '#', True
            if s[x][y] == '#' and a >= (4 if p == 1 else 5): ns[x][y], b = 'L', True
    return b, ns

def seat_in_sight(s, i, j):
    c = 0
    for k in d:
        x, y = i, j
        while 0 < x < len(s)-1 and 0 < y < len(s[0])-1:
            x, y = x + k[0], y + k[1]
            if s[x][y] == '#': c += 1; break
            elif s[x][y] == 'L': break 
    return c

d = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]; d.remove((0, 0))

s1 = [list('.'+l.rstrip('\n')+'.') for l in open('input')]
s1.insert(0, '.'*len(s1[0])); s1.insert(len(s1), '.'*len(s1[0]));
s2 = copy.deepcopy(s1)

b = True
while b: b, s1 = rules(s1, 1)
answer_1 = sum(j=='#' for i in s1 for j in i)
print(f'part-1 answer: {answer_1}')

b = True
while b: b, s2 = rules(s2, 2)
answer_2 = sum(j=='#' for i in s2 for j in i)
print(f'part-2 answer: {answer_2}')