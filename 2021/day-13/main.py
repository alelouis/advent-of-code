lines = [l.rstrip().split(',') for l in open('input')]
dots = list(map(lambda x: [int(x[0]), int(x[1])], lines[:lines.index([''])]))
folds = list(map(lambda x: x[0].split('='), lines[lines.index([''])+1:]))

def pdots(dots):
    m = [[' ' for _ in range(6)] for _ in range(39)]
    for p in dots: m[p[0]][p[1]] = '+'
    return ''.join([str(m[j][i]) + ('\n' if j==38 else '') for i in range(6) for j in range(39)])

def fold(dots, folds):
    for fold in folds:
        ax, p = 1 if fold[0][-1] == 'y' else 0, int(fold[1])
        for dot in dots: dot[ax] = (p-dot[ax]%p)%p if dot[ax] > p else dot[ax] 
    return dots

print(f'part-1 answer : {len(set((p[0], p[1]) for p in fold(dots, folds[0:1])))}')
print(f'part-2 answer : \n{pdots(fold(dots, folds))}')