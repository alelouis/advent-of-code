f = open('input')
init = f.readline().rstrip(); f.readline()
poly = dict(l.rstrip().split(' -> ') for l in f)

def polymerization(steps):
    polyc = {k:0 for k in poly.keys()}
    elemc = {u:0 for u in set(''.join([k for k in polyc.keys()]))}
    for i in range(len(init)): elemc[init[i]] += 1
    for i in range(len(init)-1): polyc[init[i:i+2]] += 1
    for _ in range(steps):
        _polyc = polyc.copy()
        for k, v in polyc.items():
            elem = poly[k]
            elemc[elem] += v
            if v > 0:
                _polyc[k[0]+elem] += v
                _polyc[elem+k[1]] += v
                _polyc[k] -= v
        polyc = _polyc
    arr = [v for v in elemc.values()]
    return max(arr)-min(arr)

print(f'part-1 answer : {polymerization(10)}')
print(f'part-2 answer : {polymerization(40)}')