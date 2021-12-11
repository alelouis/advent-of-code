grid = [list(map(int, list(l.rstrip()))) for l in open('input')]
checks = set((i, j) for i in (-1, 0, 1) for j in (-1, 0, 1)) - set((0, 0))
octoflash, s = 0, 0

def flash(octo_to_flash, flashed, grid):
    next_octo = set()
    if len(octo_to_flash) == 0:
        for octo in flashed: grid[octo[0]][octo[1]] = 0
        return len(flashed)
    else:
        for octo in octo_to_flash:
            for c in checks:
                i, j = octo[0]+c[0], octo[1]+c[1]
                if (0 <= i < 10) and (0 <= j < 10): 
                    grid[i][j] += 1
                    if grid[i][j] > 9: next_octo.add((i, j))
            flashed.add(octo)
        return flash(next_octo - flashed, flashed, grid)

def inc_one(grid):
    octo_to_flash = set()
    for i in range(10):
        for j in range(10):
            grid[i][j] += 1
            if grid[i][j] > 9: 
                octo_to_flash.add((i, j))
    return octo_to_flash

print(f'part-1 answer : {sum([flash(inc_one(grid), set(), grid) for s in range(100)])}')
while octoflash != 100: octoflash, s = flash(inc_one(grid), set(), grid), s+1
print(f'part-2 answer : {s+100}')