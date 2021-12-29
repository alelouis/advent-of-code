import numpy as np
from numba import jit

lines = [l.strip().split(',') for l in open('example')]
for l in lines:
    first = l.pop(0).split(' ')
    for i, f in enumerate(first): l.insert(i, f)

cuboids = []
for l in lines:
    x0, x1 = l[1].split('=')[1].split('..')
    y0, y1 = l[2].split('=')[1].split('..')
    z0, z1 = l[3].split('=')[1].split('..')
    cuboid = np.array([l[0], [int(x0), int(x1)], [int(y0), int(y1)], [int(z0), int(z1)]])
    cuboids.append(cuboid)

cuboids = np.array(cuboids)

def print_mat(mat):
    for l in mat:
        for e in l:
            print(e, end = ' ')
        print('')

x_sorted = sorted(set(c[1][i] for c in cuboids for i in [0, 1]))
y_sorted = sorted(set(c[2][i] for c in cuboids for i in [0, 1]))
z_sorted = sorted(set(c[3][i] for c in cuboids for i in [0, 1]))

x_pos = {}
y_pos = {}
z_pos = {}

for i, x in enumerate(x_sorted): x_pos.update({x:i})
for i, y in enumerate(y_sorted): y_pos.update({y:i})
for i, z in enumerate(z_sorted): z_pos.update({z:i})

print(x_pos)

def get_size(c):
    print(c)
    x_range = c[1][1]-c[1][0]+1
    y_range = c[2][1]-c[2][0]+1
    z_range = c[3][1]-c[3][0]+1
    return x_range*y_range*z_range

"""
for cuboid in cuboids[0:1]:
    print(get_size(cuboid))
    print(f'x range is {cuboid[1][0]}, {cuboid[1][1]}')
    index_x_min = x_sorted.index(cuboid[1][0])
    index_x_max = x_sorted.index(cuboid[1][1])
    print(f'filling x_sorted from {index_x_min}, {index_x_max-1}')
    index_y_min = y_sorted.index(cuboid[2][0])
    index_y_max = y_sorted.index(cuboid[2][1])
    index_z_min = z_sorted.index(cuboid[3][0])
    index_z_max = z_sorted.index(cuboid[3][1])
    changes = 0
    for xi in range(index_x_min, index_x_max+1):
        for yi in range(index_y_min, index_y_max+1):
            for zi in range(index_z_min, index_z_max+1):
                value = 1 if cuboid[0] == 'on' else 0
                if value == 1:
                    if fill_mat[2*xi][2*yi][2*zi] != 1:
                        print(f'filling corner ({x_sorted[xi]},{x_sorted[xi]}),({y_sorted[yi]},{y_sorted[yi]}),({z_sorted[zi]},{z_sorted[zi]})')
                        fill_mat[2*xi][2*yi][2*zi] = value
                        changes += 1
                    #if xi != index_x_max and yi != index_y_max and zi != index_z_max:
                        try:
                            print(f'filling interv ({x_sorted[xi]}->{x_sorted[xi+1]}),({y_sorted[yi]}->{y_sorted[yi+1]}),({z_sorted[zi]}->{z_sorted[zi+1]})')
                        except:
                            pass
                        fill_mat[min(2*xi+1, len(fill_mat)-1)][min(2*yi+1, len(fill_mat[0])-1)][min(2*zi+1, len(fill_mat[0][0])-1)] = value
                else:
                    if fill_mat[2*xi][2*yi][2*zi] == 1:
                        print(f'single turning off ({x_sorted[xi]},{x_sorted[xi]}),({y_sorted[yi]},{y_sorted[yi]}),({z_sorted[zi]},{z_sorted[zi]})')
                        fill_mat[2*xi][2*yi][2*zi] = value
                        changes += 1
                        if xi != index_x_max and yi != index_y_max and zi != index_z_max:
                            print(f'turning off ({x_sorted[xi+1]},{x_sorted[xi+1]}),({y_sorted[yi+1]},{y_sorted[yi+1]}),({z_sorted[zi+1]},{z_sorted[zi+1]})')
                            fill_mat[2*xi+1][2*yi+1][2*zi+1] = value
    print(f'changes : {changes}')
"""

def print_mat(mat, x = 0):
    for y in mat[x]:
        for z in y:
            print(z, end = ' ')
        print('')

import numpy as np

@jit(nopython=True)
def build_matrix(x_sorted, y_sorted, z_sorted):
    len_x = len(x_sorted)
    len_y = len(y_sorted)
    len_z = len(z_sorted)
    mat = np.zeros((2*len(x_sorted)+1, 2*len(y_sorted)+1, 2*len(z_sorted)+1), dtype = np.int64)
    for xi in range(len_x):
        print(xi)
        for yi in range(len_y):
            for zi in range(len_z):
                xi_good = xi+1 < len_x
                yi_good = yi+1 < len_y
                zi_good = zi+1 < len_z
                if xi_good: x_range = x_sorted[xi+1] - x_sorted[xi] - 1
                if yi_good: y_range = y_sorted[yi+1] - y_sorted[yi] - 1
                if zi_good: z_range = z_sorted[zi+1] - z_sorted[zi] - 1
                mat[1+2*xi,1+2*yi,1+2*zi] = 1
                if xi_good and yi_good and zi_good:
                    mat[1+2*xi+1,1+2*yi+1,1+2*zi+1] = x_range * y_range * z_range

                # edges
                if xi_good: 
                    mat[1+2*xi+1,1+2*yi,1+2*zi] = x_range
                    if yi_good: 
                        mat[1+2*xi+1,1+2*yi+1,1+2*zi] = (x_range) * (y_range)
                    if zi_good:
                        mat[1+2*xi+1,1+2*yi,1+2*zi+1] = (x_range) * (z_range)
                if yi_good: 
                    mat[1+2*xi,1+2*yi+1,1+2*zi] = y_range
                    if zi_good: 
                        mat[1+2*xi,1+2*yi+1,1+2*zi+1] = y_range * z_range
                if zi_good: 
                    mat[1+2*xi,1+2*yi,1+2*zi+1] = z_range

                
    #print_mat(mat, x = 1)
    return mat

"""
def count_bins(fill_mat):
    bins = 0
    for x in range(0, len(x_sorted)):
        for y in range(0, len(y_sorted)):
            for z in range(0, len(z_sorted)):
                #print(f'{x}, {y}, {z}')
                if fill_mat[2*x][2*y][2*z]:
                    add = 1
                    print(f'single adding {add} ({x_sorted[x]},{x_sorted[x]}),({y_sorted[y]},{y_sorted[y]}),({z_sorted[z]},{z_sorted[z]})')  
                    bins += add
                if fill_mat[2*x+1][2*y+1][2*z+1]:
                    prod = 1
                    if x+1 < len(x_sorted):  x_range = x_sorted[x+1] - x_sorted[x] - 1
                    if y+1 < len(y_sorted):  y_range = y_sorted[y+1] - y_sorted[y] - 1
                    if z+1 < len(z_sorted):  z_range = z_sorted[z+1] - z_sorted[z] - 1
                    xy_face = x_range * y_range
                    xz_face = x_range * z_range
                    zy_face = z_range * y_range
                    prod = x_range * y_range * z_range
                    total = prod + xy_face + xz_face + zy_face + x_range + y_range + z_range
                    print(f'interleave adding {total} ({x_sorted[x]}->{x_sorted[x+1]}),({y_sorted[y]}->{y_sorted[y+1]}),({z_sorted[z]}->{z_sorted[z+1]})')  
                    bins += total
    
    all_x_range = max(x_sorted) - min(x_sorted) 
    all_y_range = max(y_sorted) - min(y_sorted) 
    all_z_range = max(z_sorted) - min(z_sorted)
    all_xy_plane = all_x_range * all_y_range
    all_xz_plane = all_x_range * all_z_range
    all_yz_plane = all_y_range * all_z_range
    #print(7 + all_xy_plane + all_xz_plane + all_yz_plane + all_x_range + all_y_range + all_z_range)
    #bins += 7 + all_xy_plane + all_xz_plane + all_yz_plane + all_x_range + all_y_range + all_z_range
    return bins
                    
"""

#print(f'bins : {count_bins(fill_mat)}')
#print(f'bins true : {get_size(cuboids[0])}')
mat = build_matrix(x_sorted, y_sorted, z_sorted)

mask = np.zeros(shape = np.shape(mat), dtype = np.int64)

x_sorted = np.array(x_sorted)
y_sorted = np.array(y_sorted)
z_sorted = np.array(z_sorted)

def doit(cuboids):
    for cuboid in cuboids:
        value = 1 if cuboid[0] == 'on' else 0
        xmin = x_pos[cuboid[1][0]]
        xmax = x_pos[cuboid[1][1]]
        ymin = y_pos[cuboid[2][0]]
        ymax = y_pos[cuboid[2][1]]
        zmin = z_pos[cuboid[3][0]]
        zmax = z_pos[cuboid[3][1]]
        mask[1+2*xmin:1+2*xmax+1, 1+2*ymin:1+2*ymax+1, 1+2*zmin:1+2*zmax+1] = value
    #all = (mat*mask)
    #print('did the prod')
    #print(np.sum(all))
doit(cuboids)

@jit(nopython=True)
def compute(mask, mat):
    s = 0
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            for k in range(mask.shape[2]):
                if mask[i][j][k]:
                    s+=mat[i][j][k]
    print(s)


compute(mask, mat)