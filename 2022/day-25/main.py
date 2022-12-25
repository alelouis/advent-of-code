def to_base(n, b):
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

snafu = open('input').read().splitlines()
forward, backward = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}, {-2: '=', -1 : '-', 0: '0', 1: '1', 2: '2'}
acc = to_base(sum(5**i * forward[c] for s in snafu for i, c in enumerate(reversed(s))), 5)
convert = ''
for i in range(len(acc)-1, -1, -1):
    if acc[i] > 2:
        acc[i-1] += 1
        acc[i] -= 5
    convert += backward[acc[i]]

print(convert[::-1])
