z_div = [1, 1, 1, 26, 1, 1, 1, 26, 1, 26, 26, 26, 26, 26]
x_add = [13, 12, 10, -11, 14, 13, 12, -5, 10, 0, -11, -13, -13, -11]
y_add = [8, 16, 4, 1, 13, 5, 0, 10, 7, 2, 13, 15, 14, 9]

stack, rules= [], {}
rules = {}
for i in range(14):
    if x_add[i] > 0: # push on stack input + y_add
        stack.append((i, y_add[i]))
    else: # pop stack and save inputs condition for no subsequent push
        i_, y = stack.pop()
        rules.update({(i, i_) : (y + x_add[i])})

part1 = [9]*14
for i, j in rules: # applying rules left to right from 9*14
    if rules[(i, j)] < 0: part1[i] = part1[j] + rules[(i, j)]
    else: part1[j] = part1[i] - rules[(i, j)]

part2 = [1]*14  # applying rules right to left from 1*14
for i, j in rules:
    if rules[(i, j)] < 0: part2[j] = part2[i] - rules[(i, j)]
    else: part2[i] = part2[j] + rules[(i, j)]

print(f"part-1 answer: {''.join(map(str, part1))}")
print(f"part-2 answer: {''.join(map(str, part2))}")