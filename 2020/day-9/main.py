numbers, N = [int(line) for line in open('input')], 25

def is_sum(number, numbers):
    return number in [n_j + n_i for i, n_i in enumerate(numbers[:-1]) for j, n_j in enumerate(numbers[i+1:])]
answer = numbers[[is_sum(numbers[k], numbers[k-N:k]) for k in range(N, len(numbers))].index(False)+N]
print(f'part-1 answer: {answer}')

for l in range(2,100): #hmm, that's ugly, idc
    for m in range(len(numbers)-l):
        if sum([n for n in numbers[m:m+l]]) == answer:
            print(f'part-2 answer: {max(numbers[m:m+l]) + min(numbers[m:m+l])}')