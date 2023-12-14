def string_rep(moving_rocks, rows, cols):
    return "".join('.' if (r, c) in moving_rocks else '#' for r in range(rows) for c in range(cols))


def score(moving_rocks, rows):
    return sum(rows - r for r, _ in moving_rocks)


def step(static_rocks, moving_rocks, rd, cd, rows, cols):
    new_state, has_moved = set(s for s in moving_rocks), False
    for (r, c) in moving_rocks:
        if 0 <= (rc := r + rd) < rows and 0 <= (cc := c + cd) < cols:
            if ((rc, cc) not in moving_rocks) and ((rc, cc) not in static_rocks):
                new_state.remove((r, c))
                new_state.add((rc, cc))
                has_moved = True
    return has_moved, new_state


lines = [list(s.strip()) for s in open('input').readlines()]
rows, cols, has_moved, store_cycle, stored_count, cycle = len(lines), len(lines[0]), True, dict(), 0, 0
static_rocks, moving_rocks = (set((r, c) for r in range(rows) for c in range(cols) if lines[r][c] == rock) for rock in '#O')

while 1:
    for rd, cd in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        has_moved = True
        while has_moved:
            has_moved, moving_rocks = step(static_rocks, moving_rocks, rd, cd, rows, cols)
        if cycle == 0 and (rd, cd) == (-1, 0):
            print(score(moving_rocks, rows))  # part 1
    if (h := hash(string_rep(moving_rocks, rows, cols))) in store_cycle:
        for s, (u, v) in store_cycle.items():
            if u == store_cycle[h][0] + (1000000000 - cycle - 1) % (cycle - store_cycle[h][0] + 1):
                print(v)  # part 2
        break
    else:
        store_cycle[h] = ((stored_count := stored_count + 1), score(moving_rocks, rows))
        cycle += 1
