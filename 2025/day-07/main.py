from collections import defaultdict


def split(active_beams):
    new_beams, remove_beams, timelines = set(), set(), 0
    for beam in active_beams:
        if beam in splitter:
            remove_beams.add(beam)
            new_beams |= {beam - 1j, beam + 1j}
            timelines += counts[beam]
            counts[beam - 1j] += counts[beam]
            counts[beam + 1j] += counts[beam]
            counts[beam] = 0
    return timelines, remove_beams, new_beams


def down(old_beams):
    for ob in old_beams:
        counts[ob + 1] = counts[ob]
        counts[ob] = 0
    return {b + 1 for b in active_beams}


map, counts = [l.strip() for l in open("input").readlines()], defaultdict(int)
start, void, splitter = (set(r + 1j * c for r in range(len(map)) for c in range(len(map[0])) if map[r][c] == k) for k in "S.^")
active_beams, counts[list(start)[0] + 1] = {list(start)[0] + 1}, 1

splits, timelines = 0, 1
while list(active_beams)[0].real < len(map):
    new_timelines, old_beams, new_beams = split(active_beams)
    timelines += new_timelines
    splits += len(old_beams)
    active_beams = active_beams.difference(old_beams).union(new_beams)
    active_beams = down(active_beams)

print(splits, timelines)
