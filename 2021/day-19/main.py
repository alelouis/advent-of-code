def parse(lines):
    scans, scan, scan_id = {}, [], 0
    for l in lines[1:]:
        if not l.startswith('---'): scan.append(list(map(int, l.split(','))))
        else:
            scans.update({len(scans.keys())+1:scan})
            scan = []
    scans.update({scan_id:scan})
    return scans

def get_orient(scan):
    bea = []
    for b in scan:
        planes, _bea = [[b[0], b[1], b[2]], [b[0], b[2], -b[1]], [b[1], b[2], b[0]]], []
        for axis in planes:
            a, b, c = axis
            _bea.append([a, b, c]); _bea.append([-a, b, -c])
            _bea.append([-b, a, c]); _bea.append([-b, -a, -c])
            _bea.append([-a, -b, c]); _bea.append([a, -b, -c])
            _bea.append([b, -a, c]); _bea.append([b, a, -c])
        bea.append(_bea)
    return [[bea[j][i] for j in range(len(bea))] for i in range(24)]

def step(scan_p, cmp_mat, scans, scans_0, i_cmps, i_refs):
    for i_cmp in i_cmps:
        for i_ref in i_refs:
            if not cmp_mat[i_cmp][i_ref]:
                scan_r = scans_0[i_ref]
                orients = get_orient(scans[i_cmp])
                matched, i_orient, offset = 0, -1, 0
                for n, scan_o in enumerate(orients):
                    d = [sum([abs(x-y) for x, y in zip(bea_r, bea)]) for bea in scan_o for bea_r in scan_r]
                    d_max = d.count(max(d, key=d.count))
                    if d_max >= matched: # Stuck 3 hours on > instead of >=, yay
                        matched, i_orient, offset = d_max, n, max(d, key=d.count)
                    if matched >= 12:
                        scan_t, diffs = orients[i_orient], []
                        for bea in scan_t:
                            for bea_r in scan_r:
                                if sum([abs(x-y) for x, y in zip(bea_r, bea)]) == offset:
                                    diffs.append([x - y for x, y in zip(bea_r, bea)]) 
                        d_common = max(diffs, key=diffs.count)
                        same_d = diffs.count(d_common)
                        if same_d >= 12:
                            bea_c = [[x + y for x, y in zip(bea, d_common)] for bea in scan_t]
                            scan_p.append(d_common)
                            i_cmps.remove(i_cmp)
                            i_refs.append(i_cmp)
                            scans_0.update({i_cmp:bea_c})
                            return scan_p, cmp_mat, scans_0, i_cmps, i_ref
                        else: cmp_mat[i_cmp][i_ref] = 1
                else: cmp_mat[i_cmp][i_ref] = 1

scans = parse([l.rstrip() for l in open('input').readlines() if l.rstrip() != ''])
i_refs, i_cmps, scans_0 = [0], list(range(1, len(scans))), {0:scans[0]}
cmp_mat, scan_p = [[0 for _ in range(len(scans))] for _ in range(len(scans))],  []
while len(scans_0) != len(scans):
    scan_p, cmp_mat, scans_0, i_cmps, i_ref = step(scan_p, cmp_mat, scans, scans_0, i_cmps, i_refs)

print(f'part-1 answer : {len(set(tuple([*b]) for _, scan in scans_0.items() for b in scan ))}')
print(f'part-2 answer : {max(sum(abs(x - y) for x, y in zip(bi, bj)) for bj in scan_p for bi in scan_p)}')