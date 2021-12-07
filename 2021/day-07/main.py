line = list(map(int, open('input').readline().split(',')))

def solve(line, f): return min([sum([f(n-t) for n in line]) for t in line])

print(f'part-1 answer : {solve(line, lambda x: abs(x))}')
print(f'part-2 answer : {solve(line, lambda x: abs(x)*(abs(x)+1)/2)}')