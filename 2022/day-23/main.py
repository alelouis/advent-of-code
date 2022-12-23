def add(p, q): return (p[0]+q[0], p[1]+q[1])
def get_area(elves):
    rows, cols = [elf[0] for elf in elves], [elf[1] for elf in elves]
    return (max(rows) - min(rows) + 1) * (max(cols) - min(cols) + 1)

mov = {'N': (-1, 0),'NE': (-1, 1), 'E': (0, 1), 'SE': (1, 1), 'S': (1, 0), 'SW': (1, -1),'W': (0, -1), 'NW': (-1, -1)}
di = {'N': {'N', 'NE', 'NW'}, 'S': {'S', 'SE', 'SW'}, 'E': {'E', 'SE', 'NE'}, 'W': {'W', 'SW', 'NW'}}
all_dir, cycles = {v for v in mov.values()}, ['N', 'S', 'W', 'E']

cycle, max_round, cround, moving = 0, 10, 0, True
data = open('input').read().splitlines()
elves = {(r, c) for c in range(len(data[0])) for r in range(len(data)) if data[r][c] == "#"}
while moving:
    if cround == 10: print(f'part-1: {get_area(elves)-len(elves)}')
    old_elves, props = {e for e in elves}, {}
    for elf in elves:
        adj = {add(elf, v) for v in mov.values()}
        if len(adj & elves) > 0:
            for i in range(4):
                look = {add(elf, mov[d]) for d in di[cycles[(cycle+i)%4]]}
                if len(look & elves)==0:
                    props[elf] = add(elf, mov[cycles[(cycle+i)%4]])
                    break
    rem_add = {(elf, prop) for elf, prop in props.items() if sum(prop==p for p in props.values()) == 1}
    for r, a in rem_add: 
        elves.remove(r)
        elves.add(a)
    cround, cycle, moving = cround + 1, cycle + 1, not (old_elves == elves)
print(f'part-2: {cround}')