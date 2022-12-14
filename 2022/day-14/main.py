def iterate(cave, part):
    iterations = 0
    while True:
        (sr, sc), sand_moved = [0, 500], True
        while sand_moved:
            sand_moved = True
            if sr + 1 == endless_void + 2: sand_moved, cave[sr][sc] = False, "o"
            elif cave[sr + 1][sc] == ".": sr += 1
            elif cave[sr + 1][sc - 1] == ".": sc -= 1
            elif cave[sr + 1][sc + 1] == ".": sc += 1
            else: sand_moved, cave[sr][sc] = False, "o"
            if part == 1 and sr > endless_void: return iterations
            if part == 2 and cave[0][500] == "o": return iterations + 1
        iterations += 1

lines = open("input").read().splitlines()
cave, endless_void = [["." for _ in range(700)] for _ in range(200)], 0

for line in lines:
    for p1, p2 in zip(line.split(" -> "), line.split(" -> ")[1:]):
        (x_p1, y_p1), (x_p2, y_p2) = list(map(int, p1.split(","))), list(map(int, p2.split(",")))
        endless_void = max([endless_void, y_p1, y_p2])
        if x_p1 == x_p2:
            for y in range(min(y_p1, y_p2), max(y_p1, y_p2) + 1): cave[y][x_p1] = "#"
        if y_p1 == y_p2:
            for x in range(min(x_p1, x_p2), max(x_p1, x_p2) + 1): cave[y_p1][x] = "#"

print(iterate(cave, part=1))
print(iterate(cave, part=2))
