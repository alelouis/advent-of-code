filepath = 'input'

""" --> Part 1 <--"""

high_seat_id = 0
with open(filepath) as fp:
    for line in (fp):
        row_dec = 0
        col_dec = 0
        for i, char in enumerate(line[0:7]):
            row_dec += 2**(len(line[0:7])-i-1) if char == 'B' else 0
        for i, char in enumerate(line[7:10]):
            col_dec += 2**(len(line[7:10])-i-1) if char == 'R' else 0
        seat_id = row_dec*8+col_dec
        if seat_id > high_seat_id:
            high_seat_id = seat_id
        
answer = high_seat_id
print(f'part-1 answer: {answer}')

""" --> Part 2 <--"""

all_possible_ids = [row * 8 + col for row in range(128) for col in range(8)]
with open(filepath) as fp:
    for line in (fp):
        row_dec = 0
        col_dec = 0
        for i, char in enumerate(line[0:7]):
            row_dec += 2**(len(line[0:7])-i-1) if char == 'B' else 0
        for i, char in enumerate(line[7:10]):
            col_dec += 2**(len(line[7:10])-i-1) if char == 'R' else 0
        seat_id = row_dec*8+col_dec
        if seat_id in all_possible_ids:
            all_possible_ids.remove(seat_id)

answer = all_possible_ids
print(f'part-2 answer: {answer}')