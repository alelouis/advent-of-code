import re
_in = [l for l in open('input')]

d, i = {}, 0
while _in[i] != '\n':
    r = _in[i].split(' ')
    d[r[0][:-1]]=[l.strip() for l in r[1:]]
    i+=1

ss, i = [], i+1
while _in[i] != '\n':
    ss.append(_in[i].strip())
    i+=1

def solve(i, rule):
    if rule[0] == 'a' or rule[0] == 'b': return rule[0]
    else:
        return [[[solve(r, d['42'])]+['+']] if r == '8' \
            else [[solve(r, d['42'])] + [solve(r, d['31'])] + \
                ['|'] + [solve(r, d['42'])] + ['{2}'] + [solve(r, d['31'])] + ['{2}'] + \
                ['|'] + [solve(r, d['42'])] + ['{3}'] + [solve(r, d['31'])] + ['{3}'] + \
                ['|'] + [solve(r, d['42'])] + ['{4}'] + [solve(r, d['31'])] + ['{4}'] + \
                ['|'] + [solve(r, d['42'])] + ['{5}'] + [solve(r, d['31'])] + ['{5}']] if r == '11' \
            else solve(r, d[r]) if r.isnumeric() \
            else r \
            for r in rule]

res = str(solve(0, d['0']))
reg = '^' + res.replace('[', '(').replace(']', ')').replace('\'', '').replace(', ', '') + '$'
answer = sum([bool(re.compile(reg).match(s)) for s in ss])
print(f'part-1/2 answer: {answer}')