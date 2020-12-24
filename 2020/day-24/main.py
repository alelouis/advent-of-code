dat = [l for l in open('input')]
xyz = {'ne':(1,0,-1), 'e':(1,-1,0), 'se':(0,-1,1), 'sw':(-1,0,1), 'w': (-1,1,0), 'nw':(0,1,-1)}

def parse(l):
    seq = [p+c if p =='s' or p == 'n' else c for p, c in zip(l, l[1:]) if c != 's' and c!= 'n']
    if l[0] == 'e' or l[0] == 'w': seq.insert(0, l[0])
    return seq[:-1]

def add(p, d):
    return tuple(_p+_d for _p,_d in zip(p, d))

def move(p, ins):
    for ax in ins:
        t = add(p, xyz[ax]); p = t
    return p
    
ts, r_xyz, bt = list(map(parse, dat)), (0, 0, 0), set()
for ins in ts:
    t = move(r_xyz, ins)
    if t in bt: bt.remove(t)
    else: bt.add(t)

print(f'part-1 answer: {len(bt)}')

def count_bt(p, bt):
    return sum([add(p, xyz[ax]) in bt for ax in ['ne', 'e', 'se', 'sw', 'w', 'nw']])

def get_adj(p):
    return [add(p, xyz[ax]) for ax in ['ne', 'e', 'se', 'sw', 'w', 'nw']]

def get_check(fts):
    ct = fts.copy()
    for f_p in fts:
        adj_ts = get_adj(f_p)
        for a_p in adj_ts:
            ct.add(a_p)
    return ct

def get_tbflip(ct, bt):
    tbf = set()
    for checked_tile in ct:
        c = count_bt(checked_tile, bt)
        if checked_tile in bt:
            if c == 0 or c > 2: tbf.add(checked_tile)
        elif c == 2: tbf.add(checked_tile)
    return tbf

fts = bt 
for day in range(100):
    ts_checked = get_check(fts)
    ts_tbf = get_tbflip(ts_checked, bt)
    for tile in ts_tbf:
        if tile in bt: bt.remove(tile)
        else: bt.add(tile)
    fts = ts_tbf

print(f'part-2 answer: {len(bt)}')