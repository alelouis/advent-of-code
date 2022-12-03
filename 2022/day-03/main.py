d, c = open('input').read().splitlines(), 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(sum([c.index(''.join(set.intersection(set(l[:len(l)//2]), l[len(l)//2:])))+1 for l in d]))
print(sum([c.index(''.join(set.intersection(set(d[i]), d[i+1], d[i+2])))+1 for i in range(0, len(d)-2, 3)]))