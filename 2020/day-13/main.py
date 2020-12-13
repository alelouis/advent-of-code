from math import ceil
from operator import mul
from functools import reduce

lines = open('input').readlines()
timestep, ids = int(lines[0]), list(map(int, list(filter(lambda x: x!='x', lines[1][:-1].split(',')))))
d_times = [i*ceil(timestep/i)-timestep for i in ids]
min_t, bus_id = min(d_times), int(ids[d_times.index(min(d_times))])
print(f'part-1 answer: {bus_id*min_t}')

M = reduce(mul, ids, 1)
ids, x = lines[1][:-1].split(','), 0
for i in range(len(ids)):
    if ids[i] != 'x':
        a_i = int(ids[i]) - i
        M_i = int(M/int(ids[i]))
        y_i = pow(M_i, -1, int(ids[i]))
        x += a_i * M_i * y_i
print(f'part-2 answer: {x%M}')
