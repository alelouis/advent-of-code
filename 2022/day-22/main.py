import re
import copy

def maxi(l): 
    return max(int(l[r][c]) for c in range(len(l[0])) for r in range(len(l)) if isinstance(l[r][c], int))
    
def find_pos(label, edge_board): 
    return [(row, col) for col in range(len(edge_board[0])) for row in range(len(edge_board)) if any(label[:-2] == l[:-2] for l in edge_board[row][col])]

def opposite(di):
    if di == 'up': return 'down'
    if di == 'down': return 'up'
    if di == 'right': return 'left'
    if di == 'left': return 'right'

def find_end(di, pos, board):
    if di == 'up': return (pos[0]-[board[r][pos[1]] for r in range(pos[0]-1, -1, -1)].index('_'), pos[1])
    if di == 'down': return (pos[0]+[board[r][pos[1]] for r in range(pos[0]+1, len(board))].index('_'), pos[1])
    if di == 'right': return (pos[0], pos[1]+[board[pos[0]][c] for c in range(pos[1]+1, len(board[0]))].index('_'))
    if di == 'left': return (pos[0], pos[1]-[board[pos[0]][c] for c in range(pos[1]-1, -1, -1)].index('_'))

def turn(di, next_inst):
    cycle = cycles.index(di)
    if next_inst == 'R': cycle = (cycle + 1)%4
    if next_inst == 'L': cycle = (cycle - 1)
    if cycle < 0: cycle += 4
    return cycle

def get_next_position(pos, di):
    if di == 'up': return (pos[0]-1, pos[1])
    if di == 'down': return (pos[0]+1, pos[1])
    if di == 'left': return (pos[0], pos[1]-1)
    if di == 'right': return (pos[0], pos[1]+1)

def wrap(di, pos, edge_board):
    label = edge_board[pos[0]][pos[1]]
    if len(label)==2:
        if di in ['up', 'down']: label = [l for l in label if l.split('_')[-1] in ['l', 'r']][0]
        if di in ['left', 'right']: label = [l for l in label if l.split('_')[-1] in ['d', 'u']][0]
    else:
        label = next(iter(label))
    next_pos = find_pos(label, edge_board)
    next_pos.remove(pos)
    return next_pos[0]

def find_extent(label, board_face):
    minr, maxr = len(board), 0
    minc, maxc = len(board[0]), 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board_face[r][c] == label:
                minr, maxr, minc, maxc = min(r, minr), max(r, maxr), min(c, minc), max(c, maxc)
    return minr, maxr, minc, maxc

def find_face(board):
    board_face = copy.deepcopy(board)
    tile_size, uniques = 50, set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != '_':
                board_face[row][col] = ((col-1) // tile_size) + ((row-1) // tile_size) * tile_size
                uniques.add(board_face[row][col])
    for i, v in enumerate(uniques):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board_face[row][col] == v:
                    board_face[row][col] = i
    return board_face

def find_edge_board(board_face):
    edge_board =[[set() for _ in range(len(board[0]))] for _ in range(len(board))]
    for edge in edges:
        top, bottom, left, right = find_extent(edge, board_face)
        top_inst, right_inst, bottom_inst, left_inst = edges[edge]
        if top_inst is not None:
            for i, col in enumerate(range(left, right+1)):
                label, orient = top_inst.split('_')
                if orient == "r": edge_board[top][col].add(f"{label}_{i}_{orient}")
                else: edge_board[top][col].add(f"{label}_{right-left-i}_{orient}")
        if bottom_inst is not None:
            for i, col in enumerate(range(left, right+1)):
                label, orient = bottom_inst.split('_')
                if orient == "r": edge_board[bottom][col].add(f"{label}_{i}_{orient}")
                else: edge_board[bottom][col].add(f"{label}_{right-left-i}_{orient}")
        if left_inst is not None:
            for i, row in enumerate(range(top, bottom+1)):
                label, orient = left_inst.split('_')
                if orient == "d": edge_board[row][left].add(f"{label}_{i}_{orient}")
                else: edge_board[row][left].add(f"{label}_{bottom-top-i}_{orient}")
        if right_inst is not None:
            for i, row in enumerate(range(top, bottom+1)):
                label, orient = right_inst.split('_')
                if orient == "d": edge_board[row][right].add(f"{label}_{i}_{orient}")
                else: edge_board[row][right].add(f"{label}_{bottom-top-i}_{orient}")
    return edge_board

def move(board, part):
    cycle, pos = 3, (1, board[1].index('.'))
    di = cycles[cycle]
    edge_board = find_edge_board(find_face(board))
    while instructions:
        next_inst = instructions.pop(0)
        rotate, max_moves = next_inst[0], int(next_inst[1:])
        cycle = turn(di, rotate)
        di = cycles[cycle]
        move = 0
        while move < max_moves:
            next_position = get_next_position(pos, di)
            if board[next_position[0]][next_position[1]] == '_':
                if part == 2:
                    new = wrap(di, pos, edge_board)
                    if board[new[0]][new[1]] != '#':
                        labels = edge_board[pos[0]][pos[1]]
                        if di in ['up', 'down']: true_label = [l for l in labels if l.split('_')[-1] in ['r', 'l']]
                        if di in ['left', 'right']: true_label = [l for l in labels if l.split('_')[-1] in ['u', 'd']]
                        if isinstance(true_label, list):
                            assert len(true_label) == 1, f'True label not one sized {true_label}'
                            true_label = true_label[0]
                        next_labels = copy.deepcopy(adj[true_label.split('_')[0]])
                        next_labels.remove(true_label[-1])
                        new_orient = next_labels[0][-1]
                        if new_orient in ['r', 'l']:
                            p = get_next_position(new, 'up')
                            if board[p[0]][p[1]] == '_': di = 'down'
                            else: di = 'up'
                        if new_orient in ['u', 'd']:
                            p = get_next_position(new, 'right')
                            if board[p[0]][p[1]] == '_': di = 'left'
                            else: di = 'right'
                else:
                    new = find_end(opposite(di), pos, board)
                if board[new[0]][new[1]] != '#': next_position = new
                else: break
            elif board[next_position[0]][next_position[1]] == '#': break
            pos = next_position
            move += 1
    return pos[0], pos[1], cycle

data = open("input").read()

board, path = data.split("\n\n")
path = 'R' + path
instructions = re.findall(r'([RL]\d+)', path)
board = [[c if c in ['.', '#'] else '_' for c in b] for b in board.splitlines()]
max_col = max(len(row) for row in board) + 1
board.insert(0, ['_' for _ in range(max_col)])
board.append(['_' for _ in range(max_col)])
for row in board: 
    row.extend(['_' for _ in range(max_col-len(row))])
    row.insert(0, '_')

cycles = ['right', 'down', 'left', 'up']

edges = {0: ['f_l', None, None, 'g_d'], 1: ['d_r', 'e_u', 'a_r', None], 2: ['b_l', None, None, 'g_u'],
    3: [None, 'e_d', 'c_r', None], 4: [None, 'a_d', None, 'b_u'], 5: [None, 'c_d', 'd_r', 'f_u']}

adj = {'a': ['d', 'r'], 'b': ['u', 'l'], 'c': ['r', 'd'], 'd': ['r', 'r'], 'e': ['u', 'd'], 'f': ['l', 'u'], 'g': ['d', 'u']}

row, col, cycle = move(board, part = 1)
print(f"part-1: {1000*row + 4*col + cycle}")

row, col, cycle = move(board, part = 2)
print(f"part-2: {1000*row + 4*col + cycle}")

# UGGLLYYYY DAY 