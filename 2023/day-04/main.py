def parse(*nums):
    return (set(int(s[j:j + 2]) for j in range(0, len(s), 3)) for s in nums)


cards, total = open("input").readlines(), 0
instances = [1] * len(cards)

for ic, card in enumerate(cards):
    winners, numbers = parse(*card.strip().split(': ')[1].split(' | '))
    total += int(2 ** (len(numbers & winners) - 1))
    for i in range(ic + 1, ic + 1 + len(numbers & winners)):
        instances[i] += instances[ic]

print(total)
print(sum(instances))
