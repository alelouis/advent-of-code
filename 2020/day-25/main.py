ck, dk = 1614360, 7734663

def loop(v, sn):
    return (v*sn)%20201227

def find_loop_size(k):
    v, ls = 1, 0
    while v != k:
        ls += 1
        v = loop(v, 7)
    return ls

ek = 1
for _ in range(find_loop_size(dk)):
    ek = loop(ek, ck)

print(f'part-1 answer: {ek}')