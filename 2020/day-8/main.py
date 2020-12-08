import copy

def execute(op, arg, pos):
    global i
    if op == 'acc':
        i += arg
        return pos + 1
    if op == 'jmp':
        return pos + arg
    if op == 'nop':
        return pos + 1

def run(stack):
    global i
    pos, i = 0, 0
    call_history = []
    while pos not in call_history:
        call_history.append(pos)
        pos = execute(stack[pos][0], stack[pos][1], pos)
        if pos == len(stack):
            return i
            

stack = [[line.split(' ')[0], int(line.split(' ')[1][:-1])] for line in open('input')]

""" --> Part 1 <--"""

run(stack)
print(f'part-1 answer: {i}')

""" --> Part 2 <--"""

for idx, instruction in enumerate(stack):
    new_stack = copy.deepcopy(stack)
    if instruction[0] == 'jmp':
        new_stack[idx][0] = 'nop'
    elif instruction[0] == 'nop':
        new_stack[idx][0] = 'jmp'
    
    answer = run(new_stack)
    if answer is not None:
        break
            
print(f'part-2 answer: {answer}')