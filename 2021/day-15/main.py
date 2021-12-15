def scale(l, s):
    ll = len(l)
    _l = [[l[i%ll][j%ll]+(i//ll+j//ll) for i in range(ll*s)] for j in range(ll*s)]
    for i in range(ll*s):
        for j in range(ll*s):
            if _l[i][j] >= 10: _l[i][j] = _l[i][j] - 9    
    return _l

def get_short(l):
    ll = len(l)
    tv = [[1e4 for _ in range(ll)] for _ in range(ll)]
    v, tv[0][0] = [[0 for _ in range(ll)] for _ in range(ll)], 0
    l, tv, i, j, v, m, mp = prop(l, tv, 0, 0, v, [0], [[0, 0]])
    while [i, j] != [ll-1, ll-1]: l, tv, i, j, v, m, mp = prop(l, tv, i, j, v, m, mp)
    return tv[-1][-1]

def prop(l, tv, i, j, v, m, mp):
    v[i][j], c = 1, []
    chks = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for d in chks:
        if 0 <= i+d[0] < len(tv) and 0 <= j+d[1] < len(tv):
            c.append([i+d[0], j+d[1]])
    for ci, cj in c:
        _tv = tv[i][j] + l[ci][cj]
        if _tv < tv[ci][cj]:
            tv[ci][cj] = _tv
            m.append(_tv)
            mp.append([ci, cj])
    if [i,j] in mp:
        pop = mp.index([i,j])
        mp.pop(pop)
        m.pop(pop)
    return l, tv, *mp[m.index(min(m))], v, m, mp

l = [list(map(int, list(l.rstrip()))) for l in open('input')]
print(f'part-1 answer : {get_short(l)}')
print(f'part-2 answer : {get_short(scale(l, 5))}')