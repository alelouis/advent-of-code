def update_cycle(cycle, X, pixels, strength):
    cycle += 1
    pixels.extend(get_sprite(X)[(cycle-1)%40])
    strength += cycle * X if (cycle-20)%40==0 else 0
    return cycle, X, pixels, strength

def get_sprite(X):
    sprite = [" "] * 40
    sprite[max(X-1, 0):min(X+2, 40)] = ["#"] * (min(X+2, 40) - max(X-1, 0))
    return sprite

cycle, X, strength, pixels = 0, 1, 0, []
for inst in open('input').read().splitlines():
    match inst.split():
        case ["noop"]: 
            cycle, X, pixels, strength = update_cycle(cycle, X, pixels, strength)
        case ["addx", V]:
            cycle, X, pixels, strength = update_cycle(*update_cycle(cycle, X, pixels, strength))
            X += int(V)

print(f"part-1 answer: {strength}")
print("part-2 answer:")
for row in range(6): print("".join(pixels[row*40:(row+1)*40]))