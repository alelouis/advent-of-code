from itertools import accumulate

iamdumb = (f'{l[0]}1' for l in open('input').readlines() for _ in range(int(l[1:])))
move_mod = lambda dial, ins: (dial + (-1 if ins[0] == 'L' else 1) * int(ins[1:])) % 100
part1 = sum(d == 0 for d in accumulate(open('input').readlines(), move_mod, initial=50))
part2 = sum(d == 0 for d in accumulate(iamdumb, move_mod, initial=50))

print(part1, part2)