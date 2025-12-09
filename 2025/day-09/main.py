def intersects(c1, c2, p1, p2):
    x_min, x_max = min(c1.real, c2.real), max(c1.real, c2.real)
    y_min, y_max = min(c1.imag, c2.imag), max(c1.imag, c2.imag)
    x1, y1, x2, y2 = p1.real, p1.imag, p2.real, p2.imag
    if y1 == y2:
        return y_min < y1 < y_max and min(x1, x2) < x_max and max(x1, x2) > x_min
    if x1 == x2:
        return x_min < x1 < x_max and min(y1, y2) < y_max and max(y1, y2) > y_min


def area(p1, p2):
    return int((abs((p1 - p2).real) + 1) * (abs((p1 - p2).imag) + 1))


def sign(a):
    return 1 if a > 0 else -1


def generate_segments(tiles):
    segments = set()
    for t1, t2 in zip(tiles, tiles[1:]):
        if (t1 - t2).real == 0:
            segments.add((t1 - 1j * sign((t1 - t2).imag), t2 + 1j * sign((t1 - t2).imag)))
        else:
            segments.add((t1 - 1 * sign((t1 - t2).real), t2 + 1 * sign((t1 - t2).real)))
    return segments


tiles = [eval(l.strip().replace(",", "+") + "j") for l in open("input").readlines()]
rectangles, segments = set(((t1, t2), area(t1, t2)) for t1 in tiles for t2 in tiles), generate_segments(tiles)
part1 = max(rectangles, key=lambda e: e[-1])[-1]

for rectangle, area in sorted(rectangles, key=lambda e: e[-1], reverse=True):
    if not any(intersects(*rectangle, *seg) for seg in segments):
        part2 = area
        break

print(part1, part2)
