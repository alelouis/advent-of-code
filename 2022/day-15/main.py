import re

def merge(inter):
    inter.sort()
    s = [inter[0]]
    for i in inter[1:]:
        if s[-1][0] <= i[0] <= s[-1][-1]: s[-1][-1] = max(s[-1][-1], i[-1])
        else: s.append(i)
    return s

def get_range(a, b, c, d, y):
    st, en = a - abs(a-c) - abs(b-d) + abs(b - y), a + abs(a-c) + abs(b-d) - abs(b - y)
    return [] if abs(b - y) > abs(a-c) + abs(b-d) else [st, en+1]

def line_scan(line_no):
    intervals = [get_range(*list(map(int, re.findall(r'-?\d+', line))), line_no) for line in lines]
    return merge([i for i in intervals if i != []])

lines, lim = open('input').read().splitlines(), 4_000_000
print(f"part-1: {sum(m[1]-m[0] for m in line_scan(lim//2))-1}")
print(f"part-2: {next(l + r[0][-1] * lim for l in range(0, lim) if len(r := line_scan(l)) > 1)}")

# Better take a coffee right now ٩(◕‿◕｡)۶