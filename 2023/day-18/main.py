def lava(trenches, total_length):
    area = abs(sum(p0[0] * p1[1] - p0[1] * p1[0] for p0, p1 in zip(trenches, trenches[1::])) / 2)
    return int(1 + area - total_length / 2 + total_length)


def solve(part, total_length=0):
    for dig in plan:
        dir, amount, hexa = dig
        if part == 2:
            amount, dir = int(hexa[2:-2], base=16), list("RDLU")[int(hexa[-2])]
        total_length += int(amount)
        tr.append((tr[-1][0] + int(amount) * moves[dir][0], tr[-1][1] + int(amount) * moves[dir][1]))
    return lava(tr, total_length)


plan, tr = [l.strip().split(" ") for l in open("input")], [(0, 0)]
moves = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

print(solve(1))
print(solve(2))
