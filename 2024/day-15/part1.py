map, instructions = open('input').read().split('\n\n')
instructions = instructions.replace('\n', '')
map = [[d for d in l] for l in map.splitlines()]
rows, cols = len(map), len(map[0])
rocks, walls, free = [set(r + 1j * c for r in range(rows) for c in range(cols) if map[r][c] == s) for s in "O#."]

current_pos = [r + 1j * c for r in range(rows) for c in range(cols) if map[r][c] == "@"][0]

vec = {">": 1j, "<": -1j, "v": 1, "^": -1}
for ins in instructions:
    current_rocks = set()
    look_at = current_pos + vec[ins]
    while look_at in rocks:
        current_rocks.add(look_at)
        look_at += vec[ins]
    if look_at in free:
        moved_rocks = set(c + vec[ins] for c in current_rocks)
        rocks -= current_rocks
        rocks |= moved_rocks
        free |= current_rocks
        free -= moved_rocks
        free.add(current_pos)
        current_pos += vec[ins]
        free.remove(current_pos)

print(int(sum(100 * c.real + c.imag for c in rocks)))



