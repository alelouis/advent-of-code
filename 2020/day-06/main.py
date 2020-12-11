from collections import Counter

""" --> Part 1 <--"""

filepath = 'input'
group=''
count=0
with open(filepath) as fp:
    for line in fp:
        if line == '\n':
            count+=len(set(group)); group = '' 
        else:
            group += line.rstrip('\n')

answer = count
print(f'part-1 answer: {answer}')

""" --> Part 2 <--"""

filepath = 'input'
group=""
count=0
with open(filepath) as fp:
    for line in fp:
        if line == '\n':
            peoples = group.split('/')[:-1]
            answers = set(''.join(peoples))
            for answer in answers:
                all_yes = all(answer in p for p in peoples)
                count+=all_yes
            group = "" 
        else:
            group += line.rstrip('\n') + '/'

answer = count
print(f'part-2 answer: {answer}')