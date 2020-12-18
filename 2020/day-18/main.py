import re

def left_right(string):
    str_sp = re.findall('[+*]|\d+', string)
    if len(str_sp) == 3: return eval(''.join(str_sp[0:3]))
    else: return left_right(str(eval(''.join(str_sp[0:3])))+''.join(str_sp[3:]))

def plus_domination(string):
    str_sp, i = re.findall('[+*]|\d+', string), 0
    while '+' in str_sp:
        i += 1
        if str_sp[i] == '+':
            r = str(int(str_sp[i-1]) + int(str_sp[i+1]))
            del str_sp[i-1:i+2]
            str_sp.insert(i-1, r); i = 0
    return eval(''.join(str_sp))

def find_braces(string):
    co, indexes, braces = 0, [], []
    for c in string:
        if c == '(': co += 1
        if c == ')': co -= 1
        indexes.append(co)
    indexes.insert(0, 0)
    for e, ij in enumerate(zip(indexes, indexes[1:])):
        if [ij[0], ij[1]] == [0, 1] or [ij[0], ij[1]] == [1, 0]: braces.append(e)
    return braces

def solve(string, func):
    braces = find_braces(string)
    if braces == []: 
        return str(func(string))
    else:
        str_sp, dec = re.findall('[+*()]|\d+', string), 0
        for i in range(0, len(braces), 2):
            s, e = braces[i]+1-dec, braces[i+1]-dec
            r = solve(''.join(str_sp[s:e]), func = func)
            if '*' in r or '+' in r: r = str(func(r))
            del str_sp[s-1:e+1]
            dec += e - s + 1
            str_sp.insert(s-1, r)
        return ''.join(str_sp)

ops = [l.strip().replace(' ','') for l in open('input')]
f = left_right
print(f"part-1 answer: {sum([f(solve(op, f)) if '(' in op else int(solve(op, f)) for op in ops])}")
f = plus_domination
print(f"part-2 answer: {sum([f(solve(op, f)) if '(' in op else int(solve(op, f)) for op in ops])}")
