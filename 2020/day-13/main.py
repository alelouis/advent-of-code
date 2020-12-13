from math import ceil
from operator import mul
from functools import reduce

lines = open('input').readlines()
timestep, ids = int(lines[0]), list(map(int, list(filter(lambda x: x!='x', lines[1][:-1].split(',')))))
d_times = [i*ceil(timestep/i)-timestep for i in ids]
min_t, bus_id = min(d_times), int(ids[d_times.index(min(d_times))])
print(f'part-1 answer: {bus_id*min_t}')

# https://en.wikipedia.org/wiki/Chinese_remainder_theorem
m = reduce(mul, ids, 1)
ids, x = lines[1][:-1].split(','), 0
for i in range(len(ids)):
    if ids[i] != 'x':
        a_i = int(ids[i]) - i
        m_i = int(m/int(ids[i]))
        y_i = pow(m_i, -1, int(ids[i]))
        x += a_i * m_i * y_i
print(f'part-2 answer: {x%m}')
