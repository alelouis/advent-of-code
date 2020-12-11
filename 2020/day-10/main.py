def diff(r, n):
    return sum([j-i == n for i, j in zip(sorted(r), sorted(r)[1:])])

ratings = [int(line) for line in open('input')]
ratings.insert(0, 0)
ratings.insert(len(ratings), max(ratings)+3)
print(f'part-1 answer: {diff(ratings, 1) * diff(ratings, 3)}')

can_remove = [(j-i)<=3 for i, j in zip(sorted(ratings), sorted(ratings)[2:])]
rem = sorted([sorted(ratings)[i+1] for i, x in enumerate(can_remove) if x])
count = sum(i==j-1 and k==j+1 for i, j, k in zip(rem, rem[1:], rem[2:]))
answer = 2**(len(rem)-count*3)*7**count
print(f'part-2 answer: {answer}')