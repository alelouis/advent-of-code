blocks = open('input').read().split('\n\n')
b_area = {idx : sum(c == '#' for c in ''.join(b)) for idx, b in enumerate(blocks[:-1])}

valid_zones = 0
for z in blocks[-1].split('\n'):
    area, indices = eval(z.split(':')[0].replace('x', '*')), map(int, z.split(':')[1].split()[:])
    valid_zones += sum([c * b_area[i] for i, c in enumerate(indices)]) < area

print(valid_zones)