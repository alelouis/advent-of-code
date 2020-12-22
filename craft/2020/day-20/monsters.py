import numpy as np
from scipy import signal

lines, answer = [l.strip() for l in open('input')], 1
tiles = {lines[i][5:-1] : lines[i+1:i+11] for i in range(0, len(lines), 12)}
top, bot = lambda t: t[0], lambda t: t[-1]
left, right = lambda t: ''.join([l[0] for l in t]), lambda t: ''.join([l[-1] for l in t])

def match(tile_1, tile_2, side):
    if side == 'top':   return top(tile_1) == bot(tile_2)
    if side == 'bot':   return bot(tile_1) == top(tile_2)
    if side == 'left':  return left(tile_1) == right(tile_2)
    if side == 'right': return right(tile_1) == left(tile_2)

def flip(tile, axis):
    if axis == 'no' : return [l for l in tile]
    if axis == 'h': return [l[::-1] for l in tile]
    if axis == 'v': return [l for l in tile[::-1]]

def rotate(tile, angle): #clockwise
    if angle == 0:   return [l for l in tile]
    if angle == 90:  return [''.join(l) for l in list(zip(*tile[::-1]))]
    if angle == 180: return rotate(rotate(tile, 90), 90)
    if angle == 270: return rotate(rotate(rotate(tile, 90), 90), 90)


def tile_from_id_ex(_id_ex):
    _id, axis, angle = _id_ex.split('_') 
    return rotate(flip(tiles[_id], axis), int(angle))
    
def find_right_candidate(id_list):
    if len(id_list)%12 != 0: _id_ex = id_list[-1]
    else: _id_ex = id_list[-12]
    tile = tile_from_id_ex(_id_ex)
    for _id_ot in tiles:
        if _id_ot not in [l.split('_')[0] for l in id_list]:
            for angle in [0, 90, 180, 270]:   
                for axis in ['no', 'h']:
                    o_tile = rotate(flip(tiles[_id_ot], axis), angle)
                    if len(id_list)%12 != 0:
                        if right(tile) == left(o_tile):
                            return [_id_ot + '_' + axis + '_' + str(angle)]
                    elif bot(tile) == top(o_tile):
                        return [_id_ot + '_' + axis + '_' + str(angle)]
    return []

def explore(list_id):
    return list_id if find_right_candidate(list_id) == [] else explore(list_id + find_right_candidate(list_id))

list_id = explore(['1327_no_0'])

def reconstruct_image(list_id):
    image = np.zeros(shape = (12, 12, 8, 8))
    for i, _id_ex in enumerate(list_id):
        tile = tile_from_id_ex(_id_ex)
        tile_np = np.array([c=='#' for t in tile for c in t]).reshape(10, 10)[1:9,1:9]
        image[int(i//12), int(i%12)] = tile_np
    return np.concatenate(np.concatenate(image, axis = 1), axis = 1)

monster = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                    [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1],
                    [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0]])

import matplotlib.pyplot as plt

image = [['#' if l == 1.0 else '.' for l in t] for t in reconstruct_image(list_id).tolist()]
for angle in [0, 90, 180, 270]:   
    for axis in ['no', 'h']:
        t_image = np.array([c=='#' for t in rotate(flip(image, axis), angle) for c in t]).reshape(12*8, 12*8)
        conv_result = signal.convolve2d(t_image, monster)
        if np.max(conv_result) == np.sum(monster): 
            sea = conv_result.copy()
            monster_count = np.sum(conv_result==np.sum(monster))

monster_positions = np.argwhere(sea == 15)
for monster_pos in monster_positions:
    monster_extent = sea[monster_pos[0]-1:monster_pos[0]+2, monster_pos[1]-10:monster_pos[1]+10]
    if np.shape(monster_extent) == (3, 20):
        sea[monster_pos[0]-1:monster_pos[0]+2, monster_pos[1]-10:monster_pos[1]+10] |= monster*50
fig = plt.figure(frameon=False)
fig.set_size_inches(5, 5)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)
ax.imshow(sea, aspect='auto', cmap = 'gnuplot2')
fig.savefig('monsters.png', bbox_inches='tight',transparent=True, pad_inches=0, dpi = 300) 