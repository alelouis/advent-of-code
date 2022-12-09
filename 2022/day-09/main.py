def move_tail(T, H):
    if T[0] == H[0]: 
        T[1] -= (T[1] - H[1]) // 2 if abs((T[1] - H[1])) == 2 else 0
    elif T[1] == H[1]:
        T[0] -= (T[0] - H[0]) // 2 if abs((T[0] - H[0])) == 2 else 0
    elif abs(T[0] - H[0]) + abs(T[1] - H[1]) != 2:
        T[0] -= 1 if T[0] > H[0] else -1
        T[1] -= 1 if T[1] > H[1] else -1

def move_head(H, direction):
    match direction:
        case "U": H[1] += 1
        case "D": H[1] -= 1
        case "L": H[0] -= 1
        case "R": H[0] += 1

instructions = open("input").readlines()
H, tails, markers = [0, 0], [[0, 0] for i in range(9)], {i: set() for i in range(9)}

for inst in instructions:
    direction, amount = inst.split()
    for _ in range(int(amount)):
        move_head(H, direction)
        for i, (a, b) in enumerate(zip([H, *tails], [H, *tails][1:])):
            move_tail(b, a)
            markers[i].add(f"{tails[i][0], tails[i][1]}")

print(f"part-1 answer: {len(set(markers[0]))}")
print(f"part-2 answer: {len(set(markers[8]))}")