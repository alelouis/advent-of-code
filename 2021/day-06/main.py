from collections import deque

line = list(map(int, open('input').readline().split(',')))
counts = deque([line.count(i) for i in range(9)])

def life(n):
    for _ in range(n):
        counts.rotate(-1)
        counts[6] += counts[8]
    return sum(counts)

print(f'part-1 answer : {life(80)}')
print(f'part-2 answer : {life(256)}')