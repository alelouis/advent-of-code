filepath = 'input'
numbers = []
with open(filepath) as fp:
   for line in (fp):
       numbers.append(int(line))

""" --> Part 1 <--"""

def find_2020_sum(numbers):
    for number_1 in numbers:
        for number_2 in numbers:
            if number_1 + number_2 == 2020:
                return number_1 * number_2

answer = find_2020_sum(numbers)
print(f'part-1 answer: {answer}')

""" --> Part 2 <--"""

def find_2020_sum_3_numbers(numbers):
    for number_1 in numbers:
        for number_2 in numbers:
            for number_3 in numbers:
                if number_1 + number_2 + number_3 == 2020:
                    return number_1 * number_2 * number_3

answer = find_2020_sum_3_numbers(numbers)
print(f'part-2 answer: {answer}')