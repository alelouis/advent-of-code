import math

def explode(num, depth = 0):
    for pos, c in enumerate(num):
        depth += 1 if c=='[' else -1 if c == ']' else 0
        if depth == 5:
            ki = kj = k = 0
            rrn = lln = []
            while not num[pos+k+1].isnumeric(): k+=1
            start, end = pos+k, num.find(']',pos+k)+1
            ln, rn = num[start+1:end-1].split(',')
            num = num[0:start] + '0' + num[end:]
            for i in range(start+1, len(num)):
                if num[i].isnumeric():
                    while num[i+ki].isnumeric(): ki+=1
                    rrn = [num[i:i+ki], i, ki]
                    break
            for j in range(start-1, 0, -1):
                if num[j].isnumeric():
                    while num[j-kj].isnumeric(): kj+=1
                    lln = [num[j-kj+1:j+1], j-kj+1, kj]
                    break
            if lln != [] and rrn == []: 
                return num[:lln[1]] + str(int(lln[0]) + int(ln)) + num[lln[1]+lln[2]:]
            if rrn != [] and lln == []: 
                return num[:rrn[1]] + str(int(rrn[0]) + int(rn)) + num[rrn[1]+rrn[2]:]
            if rrn != [] and lln != []:
                return num[:lln[1]] + str(int(lln[0]) + int(ln)) + num[lln[1]+lln[2]:rrn[1]] + str(int(rrn[0]) + int(rn)) + num[rrn[1]+rrn[2]:]
    
def split(num):
    for n in num.replace(']', '').replace('[', '').replace(' ', '').split(','):
        if int(n) >= 10: return num.replace(str(n), f'[{math.floor(float(n)/2)},{math.ceil(float(n)/2)}]', 1)

def reduce(number):
    exploded = explode(number)
    if exploded is not None: return reduce(exploded)
    else:
        splitted = split(number)
        if splitted is not None: return reduce(splitted)
        else: return number

def collapse(num):
    num = str(num).replace(' ', '')
    for i, c in enumerate(num):
        if c == ',' and num[i-1].isnumeric() and num[i+1].isnumeric():
            ki = kj = 0
            while num[i-1-ki].isnumeric(): ki+=1
            while num[i+1+kj].isnumeric(): kj+=1
            lln, rrn = num[i-ki:i], num[i+1:i+1+kj]
            return num[:i-1-ki] + str(3*int(lln) + 2*int(rrn)) + num[i+2+kj:]

def collapse_all(s):
    s = collapse(s)
    while ',' in s: s = collapse(s)
    return int(s)

# part-1
lines = [l.rstrip() for l in open('input').readlines()]
add = lambda x, y: '[' + x + ',' + y +' ]'
while len(lines) != 1:
    reduced = reduce(add(lines[0], lines[1]))
    for _ in range(2): lines.pop(0)
    lines.insert(0, reduced)
print(f'part-1 answer : {collapse_all(lines[0])}')

# part-2
lines = [l.rstrip() for l in open('input').readlines()]
magnitudes = []
for i in range(len(lines)):
    for j in range(len(lines)):
        magnitudes.append(collapse_all(reduce(add(lines[i], lines[j]))))
        magnitudes.append(collapse_all(reduce(add(lines[j], lines[i]))))
print(f'part-2 answer : {max(magnitudes)}')