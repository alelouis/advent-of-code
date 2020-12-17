lines, N = open('input').read().replace('\n',''), 8
live_cells = set([(i%N, i//N, 0) for i, l in enumerate(lines) if l == '#'])
delta = [(x, y, z) for x in range(-1,2) for y in range(-1,2) for z in range(-1,2)]
neis = delta.copy()
neis.remove((0,0,0))

def next_state(c_cell):
    count = 0
    for n in neis:
        nei = (c_cell[0] + n[0], c_cell[1] + n[1], c_cell[2] + n[2])
        if nei in live_cells:
            count += 1
    if c_cell in live_cells and not (count == 2 or count == 3):
        next_live_cells.remove(c_cell)
    elif c_cell not in live_cells and count == 3:
        next_live_cells.add(c_cell)

cycles = 6
for cycle in range(cycles):
    print(len(live_cells))
    next_live_cells = live_cells.copy()
    checked_cells = set([(pos[0] + d[0], pos[1] + d[1], pos[2] + d[2]) for pos in live_cells for d in delta])
    for cell in checked_cells:
        next_state(cell)
    live_cells = next_live_cells.copy()

print(len(live_cells))
