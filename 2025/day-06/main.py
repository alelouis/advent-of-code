from functools import reduce
import operator


def part1():
    return sum(reduce(ops[[op[i] for op in li][-1]], map(int, [op[i] for op in li][:-1])) for i in range(len(li[0])))


def part2():
    operands, total = [], 0
    for c in range(longest := max(len(c) for c in ch)):
        n = [ch[r][c] if c < len(ch[r]) else " " for r in range(len(ch))]
        if n[-1] in ops:
            op = ops[n[-1]]
            operands.append(int("".join(n[:-1])))
        elif all(c == " " for c in n) or c == longest - 1:
            total += reduce(op, operands)
            operands = []
        else:
            operands.append(int("".join(n)))
    return total


li = [l.split() for l in open("input").readlines()]
ch = [l for l in open("input").readlines()]
ops = {"*": operator.mul, "+": operator.add}

print(part1(), part2())
