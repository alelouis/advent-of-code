map = [l.strip() for l in open('input').readlines()]
rows, cols = len(map), len(map[0])
rolls, total_rolls = set(r + 1j * c for r in range(rows) for c in range(cols) if map[r][c] == '@'), 0
count = lambda p: sum((p + d) in rolls for d in [1j, -1j, 1, -1, 1+1j, 1-1j, -1+1j, -1-1j])

print(sum(count(p) < 4 for p in rolls))
while len(removable_rolls := set(p for p in rolls if count(p) < 4)) > 0:
    total_rolls += len(removable_rolls)
    rolls -= removable_rolls

print(total_rolls)