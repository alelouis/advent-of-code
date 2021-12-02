lines = map(lambda x: (x[0], int(x[1])), (l.split(' ') for l in open('input')))

a, z, h = 0, 0, 0
for c, n in lines:
    a += n * ((c == 'down') - (c == 'up'))
    z += a * n * (c == 'forward')
    h += n * (c == 'forward')

print(f'part-1 answer : {h*a}')
print(f'part-2 answer : {h*z}')