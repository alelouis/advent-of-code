def count(game):
    m = {"red": 0, "green": 0, "blue": 0}
    for draw in game:
        for cubes in draw.split(", "):
            value, color = cubes.split(" ")
            m[color] = max(m[color], int(value))
    return m.values()


part_1 = part_2 = 0
for idx, game in enumerate(open("input").readlines(), start=1):
    r, g, b = count(game.split(": ")[1].strip().split("; "))
    part_1 += idx * (r <= 12 and g <= 13 and b <= 14)
    part_2 += r * g * b

print(part_1)
print(part_2)
