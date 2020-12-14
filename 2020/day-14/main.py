lines = [l.split(' = ') for l in open('input')]

memory = {}
for l in lines:
    if l[0] == 'mask':
        mask = l[1][:-1]
        or_mask = int(mask.replace('X', '0'), base=2)
        and_mask = int(mask.replace('X', '1'), base=2)
    else:
        index, value = l[0].split('[')[1].split(']')[0], int(l[1][:-1])
        value = (value | or_mask) & and_mask
        memory[index] = value

answer = sum([v for k, v in memory.items()])
print(f'part-1 answer: {answer}')


def comb(addr, mask):
    if 'X' in mask:
        return addr + comb(addr, mask.replace('X', '0', 1))\
                    + comb(addr, mask.replace('X', '1', 1))
    else: return addr + [mask]

memory = {}
for l in lines:
    if l[0] == 'mask':
        mask = l[1][:-1]
        or_mask = int(mask.replace('X', '0'), base=2)
    else:
        addr, value = int(l[0].split('[')[1].split(']')[0]), int(l[1][:-1])
        addr = list(format(addr | or_mask, '#038b')[2:])
        for i, c in enumerate(mask): 
            if c == 'X': addr[i] = 'X'
        addresses = comb([], ''.join(addr))
        for addr in addresses:
            memory[int(addr, base=2)] = value

answer = sum([v for k, v in memory.items()])
print(f'part-2 answer: {answer}')

