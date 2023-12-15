def hash_step(step, current_value=0):
    for c in step:
        current_value = ((current_value + ord(c)) * 17) % 256
    return current_value


def score(boxes):
    return sum((ib + 1) * (il + 1) * int(f) for ib, box in enumerate(boxes) for il, (l, f) in enumerate(box))


def solve(steps):
    boxes = [[] for _ in range(256)]
    for step in steps:
        label, focal = (step[:-1], None) if "-" in step else step.split("=")
        if focal is None:
            for box in boxes[(box_index := hash_step(label))]:
                if box[0] == label:
                    boxes[box_index].pop(boxes[box_index].index(box))
        else:
            box_index = hash_step(label)
            if label in [l for l, _ in boxes[box_index]]:
                for box in boxes[box_index]:
                    if box[0] == label:
                        box[1] = focal
            else:
                boxes[box_index].append([label, focal])
    return boxes


steps = open("input").read().split(",")
print(sum(hash_step(step) for step in steps))
print(score(solve(steps)))
