move = lambda dx, dy, rock: [[x+dx, y+dy] for x, y in rock]
down, right, left = lambda r: move(0, -1, r), lambda r: move(1, 0, r), lambda r: move(-1, 0, r)
min_x, max_x = lambda rock: min([r[0] for r in rock]), lambda rock: max([r[0] for r in rock])
min_y, max_y = lambda rock: min([r[1] for r in rock]), lambda rock: max([r[1] for r in rock])
def is_collision(cells, rock): return any([(r[0], r[1]) in cells for r in rock])
def try_move(m, rock): return m(rock) if not is_collision(cells, m(rock)) else rock
def height_at_rock(ri, rp, hp, pn, sp): return (ri + rp - sp) // rp * hp + pn[(ri + rp - sp) % rp]

rocks = [[[0, 0], [1, 0], [2, 0], [3, 0]],[[0, 1], [1, 0], [1, 1], [1, 2], [2, 1]], [[1, 0], [2, 0], [2, 1], [0, 0], [2, 2]],[[0, 0], [0, 1], [0, 2], [0, 3]],[[0, 0], [0, 1], [1, 0], [1, 1]]]
directions = open('input').readline()
n_stop = iteration = rock_cycle = 0
cells, heights = {(i, 0) for i in range(7)}, []
current_max = max_y(cells)

while n_stop < 5000:
    heights.append(current_max)
    rock, stopped = move(2, current_max+4, rocks[rock_cycle%5]), False
    rock_cycle += 1
    while not stopped:
        if iteration%2:
            if not is_collision(cells, down(rock)): 
                rock = down(rock)
            else:
                stopped, n_stop, current_max = True, n_stop + 1, max(current_max, max_y(rock))
                cells |= set((r[0], r[1]) for r in rock)
        else:
            d = directions[(iteration//2)%len(directions)]
            if d == ">" and max_x(rock) < 6: rock = try_move(right, rock)
            if d == "<" and min_x(rock) > 0: rock = try_move(left, rock)
        iteration += 1

inter = [sum((c[0], c[1]+i) in cells for c in cells) for i in range(len(heights))]
hp = [inter.index(q) for p, q, r in zip(inter, inter[1:], inter[2:]) if q > p and q > r and q - r > 1000][0]
sp, rp = heights.index(hp), heights.index(2*hp)-heights.index(hp)
pn = [h - heights[sp:sp+rp][0] for h in heights[sp:sp+rp]]

print(height_at_rock(2022, rp, hp, pn, sp))
print(height_at_rock(1000000000000, rp, hp, pn, sp))
