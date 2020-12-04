filepath = 'input'

import numpy as np

""" --> Part 1 <--"""

with open(filepath) as fp:
    row_len = len(fp.readline().rstrip('\n'))

char_array = np.empty((0, row_len), dtype='|S5')
with open(filepath) as fp:
    for line in fp:
        char_row = line.rstrip('\n')
        char_row_array = np.chararray((1, len(char_row)))
        for char_index in range(len(char_row)):
            char_row_array[0, char_index] = char_row[char_index]
        char_array = np.append(char_array, char_row_array, axis = 0)

char_array = np.tile(char_array, (1, 33))

row = 0
col = 0
d_row = 1
d_col = 3
tree_encountered = 0
while row < char_array.shape[0]:
    if char_array[row, col] == b'#':
        tree_encountered += 1
    row += d_row
    col += d_col

answer = tree_encountered
print(f'part-1 answer: {answer}')

""" --> Part 2 <--"""

with open(filepath) as fp:
    row_len = len(fp.readline().rstrip('\n'))

char_array = np.empty((0, row_len), dtype='|S5')
with open(filepath) as fp:
    for line in fp:
        char_row = line.rstrip('\n')
        char_row_array = np.chararray((1, len(char_row)))
        for char_index in range(len(char_row)):
            char_row_array[0, char_index] = char_row[char_index]
        char_array = np.append(char_array, char_row_array, axis = 0)

char_array = np.tile(char_array, (1, 1000))

slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
product = 1
for slope in slopes:
    row = 0
    col = 0
    d_row = slope[0]
    d_col = slope[1]
    tree_encountered = 0
    while row < char_array.shape[0]:
        if char_array[row, col] == b'#':
            tree_encountered += 1
        row += d_row
        col += d_col
    product *= tree_encountered

answer = product
print(f'part-2 answer: {answer}')