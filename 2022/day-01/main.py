bags = open('input').read().split('\n\n')
calories = [sum(map(int, bag.split('\n'))) for bag in bags]

print(f'part-1 answer : {max(calories)}')
print(f'part-2 answer : {sum(sorted(calories)[-3:])}')