def find_first_plant_not_labeled(garden, target_plant_type, ccl):
    for pos, plant_type in garden.items():
        if pos not in ccl and plant_type == target_plant_type:
            return pos
    return -1


def get_neighbors(pos, garden, plant_type):
    return [(pos + d, s) for (d, s) in zip([1j, 1, -1j, -1], ['>', 'v', '<', '^']) if
            (pos + d in garden) and (garden[pos + d] == plant_type)]


def spread(pos, plant_type, ccl, label):
    nn = get_neighbors(pos, garden, plant_type)
    ccl[pos] = (label, len(nn), set(s for p, s in nn))
    for next_pos in [p for p, _ in nn if p not in ccl]:
        spread(next_pos, plant_type, ccl, label)


def areas(plant_type, ccl, groups):
    return [sum(l == clab for _, (l, _, _) in ccl.items()) for clab in groups[plant_type]]


def perimeters(plant_type, ccl, groups):
    return [sum((l == clab) * (4 - n) for _, (l, n, _) in ccl.items()) for clab in groups[plant_type]]


def corners(plant_type, ccl, groups):
    positions = [[(p, w) for p, (l, _, w) in ccl.items() if l == clab] for clab in groups[plant_type]]
    return [sum([get_corners(pos, where, garden) for pos, where in p_label]) for p_label in positions]


def get_corners(pos, where, garden):
    corner_count = 4 if set() == where else 0
    corner_count += sum((set(c) == where) for c in [['^', '<'], ['^', '>'], ['v', '<'], ['v', '>']])
    corner_count += sum(2 * (set(c) == where) for c in 'v>^<')
    for c, delta in zip([['^', '<'], ['^', '>'], ['v', '<'], ['v', '>']], [-1 - 1j, -1 + 1j, +1 - 1j, +1 + 1j]):
        corner_count += all(d in where for d in set(c)) and (garden.get(pos + delta, False) != garden[pos])
    return corner_count


def compute_total_price(ccl, groups, up, part):
    f = perimeters if part == 1 else corners
    return sum(sum([a * p for a, p in zip(areas(pt, ccl, groups), f(pt, ccl, groups))]) for pt in sorted(up))


garden_l = [[c for c in l.strip()] for l in open('input').readlines()]
garden = {r + 1j * c: garden_l[r][c] for r in range(len(garden_l)) for c in range(len(garden_l[0]))}
unique_plants, ccl, label = set(v for v in garden.values()), dict(), 0
groups = {plant_type: [] for plant_type in unique_plants}

for plant_type in sorted(unique_plants):
    while (pos := find_first_plant_not_labeled(garden, plant_type, ccl)) != -1:
        spread(pos, plant_type, ccl, label)
        groups[plant_type].append(label)
        label += 1

print(compute_total_price(ccl, groups, unique_plants, 1))
print(compute_total_price(ccl, groups, unique_plants, 2))
