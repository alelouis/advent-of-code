lines = [l.split('|') for l in open('input').readlines()]
lines, s = list(map(lambda l: [l[0].split(), l[1].split()], lines)), 0

for l in lines:
    d = {}
    for sig in l[0]: # finding 1, 4, 7 and 8
        ds, ld = set(sig), len(sig)
        if ld == 2: d['1'] = ds
        if ld == 3: d['7'] = ds
        if ld == 4: d['4'] = ds
        if ld == 7: d['8'] = ds

    for sig in l[0]: # finding 9 and 3
        ds, ld = set(sig), len(sig)
        if ld == 6 and d['4'].issubset(ds): d['9'] = ds
        if ld == 5 and d['1'].issubset(ds): d['3'] = ds

    for sig in l[0]: # finding 6 and 0
        ds, ld = set(sig), len(sig)
        if ld == 6 and not ds.issubset(d['9']):
            if d['1'].issubset(ds): d['0'] = ds
            else: d['6'] = ds

    for sig in l[0]: # finding 2 and 5
        ds, ld = set(sig), len(sig)
        if ld == 5 and not ds.issubset(d['3']):
            if ds.issubset(d['9']): d['5'] = ds
            else: d['2'] = ds

    s += int(''.join([r for di in l[1] for r in d if set(di) == d[r]]))

print(f'part-1 answer : {sum([len(d) in [2, 3, 4, 7] for l in lines for d in l[1]])}')
print(f'part-2 answer : {s}')