from copy import deepcopy

target = {'A' : 2, 'B' : 4, 'C' : 6, 'D' : 8}
final = [['A']*4, ['B']*4, ['C']*4, ['D']*4]
cost_mul = {'A' : 1, 'B' : 10, 'C' : 100, 'D' : 1000}

def find_states(s):
    states = []
    hallway, rooms, cost = s
    for p_hall in range(len(hallway)): 
        if hallway[p_hall] != '.':
            nogo = [2, 4, 6, 8]
            nogo.remove(target[hallway[p_hall]])
            for direction in [-1, 1]:
                position = p_hall
                if direction == -1: vmin, vmax = 1, len(hallway)
                else: vmin, vmax = -1, len(hallway) - 2
                while vmin <= position <= vmax:
                    position += direction
                    if hallway[position] == '.' and position not in nogo:
                        if position == target[hallway[p_hall]]:
                            if rooms[position//2-1][3] == '.': 
                                _hallway, _rooms = deepcopy(hallway), deepcopy(rooms)
                                _rooms[position//2-1][3] = _hallway[p_hall]
                                _hallway[p_hall] = '.'
                                c = abs(position - p_hall) + 4
                                c *= cost_mul[hallway[p_hall]]
                                states.append([_hallway, _rooms, cost+c])

                            elif rooms[position//2-1][0] == '.' and \
                                rooms[position//2-1][1] == '.' and \
                                rooms[position//2-1][2] == '.' and \
                                rooms[position//2-1][3] == hallway[p_hall]: 
                                _hallway, _rooms = deepcopy(hallway), deepcopy(rooms)
                                _rooms[position//2-1][2] = _hallway[p_hall] 
                                _hallway[p_hall] = '.'
                                c = abs(position - p_hall) + 3
                                c *= cost_mul[hallway[p_hall]]
                                states.append([_hallway, _rooms, cost+c])

                            elif rooms[position//2-1][0] == '.' and \
                                rooms[position//2-1][1] == '.' and \
                                rooms[position//2-1][2] == hallway[p_hall] and \
                                rooms[position//2-1][3] == hallway[p_hall]: 
                                _hallway, _rooms = deepcopy(hallway), deepcopy(rooms)
                                _rooms[position//2-1][1] = _hallway[p_hall]
                                _hallway[p_hall] = '.'
                                c = abs(position - p_hall) + 2
                                c *= cost_mul[hallway[p_hall]]
                                states.append([_hallway, _rooms, cost+c])

                            elif rooms[position//2-1][0] == '.' and \
                                rooms[position//2-1][1] == hallway[p_hall] and \
                                rooms[position//2-1][2] == hallway[p_hall] and \
                                rooms[position//2-1][3] == hallway[p_hall]: 
                                _hallway, _rooms = deepcopy(hallway), deepcopy(rooms)
                                _rooms[position//2-1][0] = _hallway[p_hall]   # FIRST
                                _hallway[p_hall] = '.'
                                c = abs(position - p_hall) + 1
                                c *= cost_mul[hallway[p_hall]]
                                states.append([_hallway, _rooms, cost+c])

                    elif hallway[position] != '.': break
    
    for room_i in range(4): 
        for level in [0, 1, 2, 3]:
            if rooms[room_i][level:-1] != final[room_i][level:]: 
                if rooms[room_i][level] != '.' and all(rooms[room_i][l] == '.' for l in range(0, level)):
                    nogo = [2, 4, 6, 8]
                    nogo.remove(target[rooms[room_i][level]])
                    for direction in [-1, 1]:
                        position = rooms[room_i][-1]
                        if direction == -1: vmin, vmax = 1, len(hallway)
                        else: vmin, vmax = -1, len(hallway) - 2
                        while vmin <= position <= vmax:
                            position += direction
                            if hallway[position] == '.' and position not in nogo:
                                if position == target[rooms[room_i][level]]: 
                                    if rooms[position//2-1][3] == '.':
                                        _hallway, _rooms = deepcopy(hallway), deepcopy(rooms)
                                        _rooms[position//2-1][1] = _rooms[room_i][level]
                                        _rooms[room_i][level] = '.'
                                        c = level + 1 + abs(rooms[room_i][-1] - position) + 4
                                        c *= cost_mul[rooms[room_i][level]]
                                        states.append([_hallway, _rooms, cost+c])

                                    elif rooms[position//2-1][0] == '.' and \
                                        rooms[position//2-1][1] == '.' and \
                                        rooms[position//2-1][2] == '.' and \
                                        rooms[position//2-1][3] == rooms[room_i][level]: 
                                        _hallway, _rooms = deepcopy(hallway), deepcopy(rooms)
                                        _rooms[position//2-1][2] = _rooms[room_i][level] 
                                        _rooms[room_i][level] = '.'
                                        c = level + 1 + abs(position - rooms[room_i][-1]) + 3
                                        c *= cost_mul[rooms[room_i][level]]
                                        states.append([_hallway, _rooms, cost+c])

                                    elif rooms[position//2-1][0] == '.' and \
                                        rooms[position//2-1][1] == '.' and \
                                        rooms[position//2-1][2] == rooms[room_i][level] and \
                                        rooms[position//2-1][3] == rooms[room_i][level]: 
                                        _hallway, _rooms = deepcopy(hallway), deepcopy(rooms)
                                        _rooms[position//2-1][1] = _rooms[room_i][level] 
                                        _rooms[room_i][level] = '.'
                                        c = level + 1 + abs(position - rooms[room_i][-1]) + 2
                                        c *= cost_mul[rooms[room_i][level]]
                                        states.append([_hallway, _rooms, cost+c])

                                    elif rooms[position//2-1][0] == '.' and \
                                        rooms[position//2-1][1] == rooms[room_i][level] and \
                                        rooms[position//2-1][2] == rooms[room_i][level] and \
                                        rooms[position//2-1][3] == rooms[room_i][level]: 
                                        _hallway, _rooms = deepcopy(hallway), deepcopy(rooms)
                                        _rooms[position//2-1][0] = _rooms[room_i][level]  
                                        _rooms[room_i][level] = '.'
                                        c = level + 1 + abs(position - rooms[room_i][-1]) + 1
                                        c *= cost_mul[rooms[room_i][level]]
                                        states.append([_hallway, _rooms, cost+c])
                                else: 
                                    _hallway, _rooms = deepcopy(hallway), deepcopy(rooms)
                                    _hallway[position] = _rooms[room_i][level]
                                    _rooms[room_i][level] = '.'
                                    c = 1 + level + abs(rooms[room_i][-1] - position) 
                                    c *= cost_mul[rooms[room_i][level]]
                                    states.append([_hallway, _rooms, cost+c])
                                    
                            elif hallway[position] != '.': break
    return states

def check_win(s):
    return all(s[1][i][0:4] == final[i] for i in range(4))

def go_tree(s, ite, hist):
    if (str(s[0]), str(s[1]), str(s[2])) in hist: return hist[(str(s[0]), str(s[1]), str(s[2]))]
    next_states, min_cost = find_states(s), 2**32
    if next_states == [] and check_win(s) and s[2] < min_cost:  
                min_cost = s[2]
    else: 
        for next_state in next_states:
            n = go_tree(next_state, ite+1, hist)
            if n < min_cost: min_cost = n
    hist[(str(s[0]), str(s[1]), str(s[2]))] = min_cost
    return min_cost
    
hallway = list('...........')
rooms = [['C', 'D', 'D', 'D', 2], \
         ['A', 'C', 'B', 'D', 4], \
         ['B', 'B', 'A', 'B', 6], \
         ['C', 'A', 'C', 'A', 8]]

print(f'part-2 answer: {go_tree([hallway, rooms, 0], 0, {})}')