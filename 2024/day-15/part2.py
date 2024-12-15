
def find(look, frr, flr):
    if look not in rr and look not in lr:
        return look in free
    if look in rr:
        frr.add(look)
        flr.add(look - 1j)
        return all([find(la, frr, flr) for la in [look + vec[ins], look + vec[ins] - 1j]]) if ins in "v^" else find(
            look + 2 * vec[ins], frr, flr)
    elif look in lr:
        flr.add(look)
        frr.add(look + 1j)
        return all([find(la, frr, flr) for la in [look + vec[ins], look + vec[ins] + 1j]]) if ins in "v^" else find(
            look + 2 * vec[ins], frr, flr)


map, instructions = open('input').read().split('\n\n')
instructions = instructions.replace('\n', '')
map = [[d for d in l] for l in map.splitlines()]
rows, cols = len(map), len(map[0])
rocks, walls, free = [set(r + 1j * c for r in range(rows) for c in range(cols) if map[r][c] == s) for s in "O#."]
cp = [r + 1j * c for r in range(rows) for c in range(cols) if map[r][c] == "@"][0]

# Transform input
free, rocks, walls = [set(2j * f.imag + f.real for f in s) for s in (free, rocks, walls)]
new_free, new_rocks, new_walls = [set(f + 1j for f in s) for s in (free, rocks, walls)]

free |= new_free
lr, rr = rocks, new_rocks
walls |= new_walls

cp = 2j * cp.imag + cp.real
free.add(cp + 1j)
cols *= 2
vec = {">": 1j, "<": -1j, "v": 1, "^": -1}

for ins in instructions:
    flr, frr = set(), set()
    if find(cp + vec[ins], frr, flr):
        lr -= flr
        lr |= (mlr := set(c + vec[ins] for c in flr))
        rr -= frr
        rr |= (mrr := set(c + vec[ins] for c in frr))
        free |= flr | frr
        free -= mlr | mrr
        free.add(cp)
        cp += vec[ins]
        free.remove(cp)

print(int(sum(100 * c.real + c.imag for c in lr)))
