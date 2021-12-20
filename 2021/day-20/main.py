def slide(im, fill):
    for _ in range(3): im = [fill*len(im[0])] + im + [fill*len(im[0])]
    for r in range(len(im)): im[r] = fill*3 + im[r] +  fill*3
    out = [[fill for _ in range(len(im[0])-3)] for _ in range(len(im)-3)]
    for row in range(0, len(im)-3):
        for col in range(0, len(im[0])-3):
            win = [im[row+i][col:col+3] for i in range(3)]
            index = int(''.join([w.replace('.', '0').replace('#', "1") for w in win]), 2)
            out[row][col] = algo[index]
    return [''.join(row) for row in out]

def iter(im, n):
    for ite in range(n): im = slide(im, algo[0] if ite%2 else algo[1])
    return im

count_lit = lambda im: sum([c == '#' for r in im for c in r ])
lines = [l.rstrip() for l in open('input').readlines()]
algo, im = lines[0], lines[2:]

print(f'part-1 answer : {count_lit(iter(im, 2))}')
print(f'part-2 answer : {count_lit(iter(im, 50))}')