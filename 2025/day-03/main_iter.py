def itersolve(n_batteries):
    total = 0
    for bank in banks:
        total_joltage, start_range = '', 0
        while len(total_joltage) < n_batteries:
            look_range = [bank[i] for i in range(start_range, len(bank) - (n_batteries - len(total_joltage ) - 1))]
            max_joltage = max(look_range)
            start_range += look_range.index(max_joltage) + 1
            total_joltage += str(max_joltage)
        total += int(total_joltage)
    return total

banks = [b.strip() for b in open('input').readlines()]
print(itersolve(2), itersolve(12))
