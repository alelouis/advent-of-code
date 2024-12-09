def get_input(part):
    fs, cid, p = {}, 0, 0
    for n, d in enumerate(disk):
        length = int(d)
        if n % 2 == 0:
            if part == 2:
                fs[p] = [str(cid), length]
            else:
                for a in range(length):
                    fs[p + a] = str(cid)
            cid += 1
        else:
            if part == 2:
                fs[p] = ['.', length]
            else:
                for a in range(length):
                    fs[p + a] = '.'
        p += length
    return fs


def part1(fs):
    num, free = [k for k, v in fs.items() if v.isdigit()], [k for k, v in fs.items() if not v.isdigit()]
    for idx in range(sum(v == "." for k, v in fs.items() if k <= sum(list(map(int, disk))[::2]))):
        fs[free[idx]], fs[num[::-1][idx]] = fs[num[::-1][idx]], '.'
    return sum(k * int(fs[k]) for k, v in fs.items() if v != '.')


def part2(fs):
    files, free = {pos: id for pos, id in fs.items() if id[0] != '.'}, {pos: id for pos, id in fs.items() if id[0] == '.'}
    for pfile, (fid, fsize) in reversed(files.items()):
        for pfree, (frid, frsize) in sorted(free.items()):
            if fsize <= frsize and frid == '.' and pfree <= pfile:
                files[pfile][0], free[pfree] = '.', [str(fid), fsize]
                if frsize - fsize > 0:
                    free[pfree + fsize] = [".", frsize - fsize]
                break
    acc = sum((p + i) * int(f) for p, (f, s) in {**files, **free}.items() for i in range(s) if f != '.')
    return acc


disk = open('test').read().strip()
print(part1(get_input(1)))
print(part2(get_input(2)))
