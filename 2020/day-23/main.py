def pch(ch, e, c):
    return '' if c == len(ch) else str(e) + pch(ch, ch[e], c+1)

def solve(_in, m):
    ch = {i:_in[(p+1)%len(_in)] for p, i in enumerate(_in)}
    cc = _in[0]
    for move in range(m):
        fc, mc, lc   = ch[cc], ch[ch[cc]], ch[ch[ch[cc]]]
        ch[cc] = ch[lc]
        d = cc-1
        if d < 1: d = max(_in)
        while d in [fc, mc, lc]:
            d -= 1
            if d < 1: d = max(_in)
        _d = ch[d]
        ch[d], ch[lc], cc = fc, _d, ch[cc]
    return ch

_in = [1,6,7,2,4,8,3,5,9]
ch = solve(_in, 100)
print(f'part-1 answer: {pch(ch, 1, 0)[1:]}')

_in += list(range(max(_in)+1, 1000000+1))
ch = solve(_in, 10000000)
print(f'part-2 answer: {ch[1] * ch[ch[1]]}')