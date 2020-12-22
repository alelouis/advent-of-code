lines = [int(l.strip()) for l in open('input_example') if l.strip().isnumeric()]
d_1, d_2 = lines[0:int(len(lines)/2)], lines[int(len(lines)/2):]
while len(d_1) != 0 and len(d_2) != 0:
    d_1 += [d_1[0], d_2[0]] if d_1[0] > d_2[0] else []
    d_2 += [d_2[0], d_1[0]] if d_1[0] < d_2[0] else []
    d_1.pop(0)
    d_2.pop(0)

answer = sum([d*(len(deck)-i) for deck in [d_1, d_2] for i, d in enumerate(deck)])
print(f'part-1 answer: {answer}')

def game(d_1, d_2):
    d_hist = []
    while len(d_1) != 0 and len(d_2) != 0:
        if any([[d_1, d_2] == d for d in d_hist]): return 1
        else: d_hist.append([d_1.copy(), d_2.copy()])
        if len(d_1)-1 >= d_1[0] and len(d_2)-1 >= d_2[0]:
            w = game(d_1.copy()[1:d_1[0]+1], d_2.copy()[1:d_2[0]+1])
        else:
            w = 1 if d_1[0] > d_2[0] else 2
        d_1 += [d_1[0], d_2[0]] if w == 1 else []
        d_2 += [d_2[0], d_1[0]] if w == 2 else []
        d_1.pop(0)
        d_2.pop(0)
    return 1 if len(d_1) != 0 else 2

d_1, d_2 = lines[0:int(len(lines)/2)], lines[int(len(lines)/2):]
w = game(d_1, d_2)
answer = sum([d*(len(deck)-i) for deck in [d_1, d_2] for i, d in enumerate(deck)])
print(f'part-2 answer: {answer}')