lines = [list(map(int, list(l.rstrip()))) for l in open('input')]
bindec = lambda l: sum([e * 2**p for p, e in enumerate(l[::-1])])

most_bin = [n>=(len(lines)/2) for n in [sum(b) for b in zip(*lines)]]
print(f'part-1 answer : {bindec(most_bin) * bindec([not b for b in most_bin])}')

def decode(lines, crit):
    sub, i = lines, 0
    while len(sub) > 1:
        bin = [n>=(len(sub)/2) for n in [sum(b) for b in zip(*sub)]]
        sub = [l for l in sub if l[i]==(bin[i] if crit else not bin[i])]
        i += 1
    return bindec(sub[0])

print(f'part-2 answer : {decode(lines, 1) * decode(lines, 0)}')