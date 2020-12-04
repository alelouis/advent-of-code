filepath = 'input'
numbers = []
with open(filepath) as fp:
   for line in (fp):
       numbers.append(int(line))

def find_2020_sum(numbers):
    for number_1 in numbers:
        for number_2 in numbers:
            if number_1 + number_2 == 2020:
                return number_1 * number_2

answer = find_2020_sum(numbers)
print(answer)