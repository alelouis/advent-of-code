import math

def parse(m):
    r = dict()
    m = m.splitlines()
    r['m_id'] = m[0].split(" ")[-1][0]
    r['items'] = list(map(int, m[1][18:].split(',')))
    r['cnt'], r['op'], r['div'] = 0, m[2][18:], int(m[3][21:])
    r['tgt_true'], r['tgt_false'] = int(m[4][-1]), int(m[5][-1])
    return r

def solve(monkeys, part, rounds):
    div_prod = math.prod(m['div'] for m in monkeys.values())
    for _ in range(rounds):
        for m in monkeys.values():
            while len(m['items']) > 0:
                old = m['items'].pop(0)
                worry = eval(m['op']) // 3 if part == 1 else eval(m['op']) % div_prod  # lol
                monkeys[m["tgt_false" if worry % m['div'] else "tgt_true"]]['items'].extend([worry])
                m['cnt'] += 1
    return math.prod(sorted([m['cnt'] for m in monkeys.values()])[-2:])

monkeys = open("input").read().split('\n\n')
print(solve({int(parse(m)['m_id']):parse(m) for m in monkeys}, 1, 20))
print(solve({int(parse(m)['m_id']):parse(m) for m in monkeys}, 2, 10000))    