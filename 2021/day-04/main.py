lines = [l.rstrip() for l in open('input') if l != '\n']
numbers = map(int, lines[0].split(','))
boards = [list(map(lambda l: list(map(int, l.split())), lines[b:b+5])) for b in range(1, len(lines)-1, 5)]
marked = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(int((len(lines)-1)/5))]
first = False

def sum_n_marked(b, m):
    return sum([b[i][j] for i in range(5) for j in range(5) if not m[i][j]])

def check_win(marked):
    for i in range(5):
        s_r, s_c = 0, 0
        for j in range(5):
            s_r += marked[i][j]
            s_c += marked[j][i]
        if s_r == 5 or s_c == 5:
            return True
    return False

while not all([check_win(m) for m in marked]):
    wins = [check_win(m) for m in marked]
    if any(wins) and not first:
        w_1, first = wins.index(True), True
        part_1 = n*sum_n_marked(boards[w_1], marked[w_1])
    n = next(numbers)
    for b, m in zip(boards, marked):
        for i in range(5):
            for j in range (5):
                if n == b[i][j]:
                    m[i][j] = 1

print(f'part-1 answer : {part_1}')
print(f'part-2 answer : {n*sum_n_marked(boards[wins.index(False)], marked[wins.index(False)])}')