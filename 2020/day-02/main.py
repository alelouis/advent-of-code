import re

regex = re.compile('(\d+)-(\d+)\s(\w):\s(\w+)')

filepath = 'input'
correct_passwords = 0

""" --> Part 1 <--"""

with open(filepath) as fp:
    for line in (fp):
        letter_count = 0
        char_min, char_max, letter, password = regex.match(line).groups()
        for i in re.finditer(letter, password):
            letter_count += 1
        if int(char_min) <= letter_count <= int(char_max):
            correct_passwords += 1

answer = correct_passwords
print(f'part-1 answer: {answer}')

""" --> Part 2 <--"""

correct_passwords = 0
with open(filepath) as fp:
    for line in (fp):
        char_min, char_max, letter, password = regex.match(line).groups()
        if (password[int(char_min) - 1] == letter) ^ (password[int(char_max) - 1] == letter):
            correct_passwords += 1

answer = correct_passwords
print(f'part-2 answer: {answer}')