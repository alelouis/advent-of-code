import re

def parse(text):
    res = {}
    for match in re.findall(r'(\w+):\s*(?:X\+?(\d+),?\s*Y\+?(\d+)|X=(\d+),?\s*Y=(\d+))', text):
        x, y = (int(match[1]), int(match[2])) if (match[1] and match[2]) else (int(match[3]), int(match[4]))
        res[f"x{match[0].lower()}"], res[f"y{match[0].lower()}"] = x, y
    return res


def cramer(xa, xb, ya, yb, xprize, yprize, part):
    # https://en.wikipedia.org/wiki/Cramer%27s_rule
    if part == 2:
        xprize += 10000000000000
        yprize += 10000000000000

    a_num, b_num = xprize * yb - xb * yprize, xprize * ya - xa * yprize
    a_den = xa * yb - xb * ya
    b_den = -a_den

    if a_den != 0 and b_den != 0 and a_num % a_den == 0 and b_num % b_den == 0:
        a = a_num // a_den
        b = b_num // b_den
        return 3 * a + b
    return 0


machines = [parse(m) for m in open('input').read().split('\n\n')]
print(sum([cramer(**machine, part=1) for machine in machines]))
print(sum([cramer(**machine, part=2) for machine in machines]))
