from itertools import combinations

u = [list(s.strip()) for s in open('input').readlines()]
solve = lambda part: sum(abs(b[0] - a[0]) + abs(b[1] - a[1]) for a, b in combinations(set((i + sum(i > r for r in [row for row in range(len(u)) if all(r == '.' for r in u[row])]) * (1 if part == 1 else (1000000 - 1)), j + sum(j > c for c in [col for col in range(len(u[0])) if all(r == '.' for r in [u[row][col] for row in range(len(u))])]) * (1 if part == 1 else (1000000 - 1))) for i in range(len(u)) for j in range(len(u[0])) if u[i][j] == '#'), 2))

print(solve(1))
print(solve(2))
