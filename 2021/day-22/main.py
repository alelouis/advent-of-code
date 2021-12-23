import numpy as np
from numba import jit

lines, cuboids = [l.strip().split(',') for l in open('input')], []
for l in lines:
    for i, f in enumerate(l.pop(0).split(' ')): l.insert(i, f)

for l in lines:
    x0, x1 = l[1].split('=')[1].split('..')
    y0, y1 = l[2].split('=')[1].split('..')
    z0, z1 = l[3].split('=')[1].split('..')
    cuboids.append(np.array([l[0], [int(x0), int(x1)], [int(y0), int(y1)], [int(z0), int(z1)]], dtype = object))

sortx = np.array(sorted(set(c[1][i] for c in cuboids for i in [0, 1])))
sorty = np.array(sorted(set(c[2][i] for c in cuboids for i in [0, 1])))
sortz = np.array(sorted(set(c[3][i] for c in cuboids for i in [0, 1])))

x_pos = {x:i for i, x in enumerate(sortx)}
y_pos = {y:i for i, y in enumerate(sorty)}
z_pos = {z:i for i, z in enumerate(sortz)}

@jit(nopython=True)
def build_matrix(sortx, sorty, sortz):
    len_x, len_y, len_z = len(sortx), len(sorty), len(sortz)
    mat = np.zeros((2*len_x+1, 2*len_y+1, 2*len_z+1), dtype = np.int64)
    for xi in range(len_x):
        for yi in range(len_y):
            for zi in range(len_z):
                xib, yib, zib = xi+1 < len_x, yi+1 < len_y, zi+1 < len_z
                if xib: dx = sortx[xi+1] - sortx[xi] - 1
                if yib: dy = sorty[yi+1] - sorty[yi] - 1
                if zib: dz = sortz[zi+1] - sortz[zi] - 1
                mat[1+2*xi,1+2*yi,1+2*zi] = 1 # corner
                if xib and yib and zib: 
                    mat[1+2*xi+1,1+2*yi+1,1+2*zi+1] = dx * dy * dz # inner volume
                if xib: 
                    mat[1+2*xi+1,1+2*yi,1+2*zi] = dx # edge
                    if yib: mat[1+2*xi+1,1+2*yi+1,1+2*zi] = dx * dy # area
                    if zib: mat[1+2*xi+1,1+2*yi,1+2*zi+1] = dx * dz # area
                if yib: 
                    mat[1+2*xi,1+2*yi+1,1+2*zi] = dy # edge
                    if zib: mat[1+2*xi,1+2*yi+1,1+2*zi+1] = dy * dz # area
                if zib: mat[1+2*xi,1+2*yi,1+2*zi+1] = dz # edge
    return mat

def compute_mask(cuboids):
    mask = np.zeros(shape = np.shape(mat), dtype = np.int64)
    for c in cuboids:
        v = 1 if c[0] == 'on' else 0
        x, _x = x_pos[c[1][0]], x_pos[c[1][1]]
        y, _y = y_pos[c[2][0]], y_pos[c[2][1]]
        z, _z = z_pos[c[3][0]], z_pos[c[3][1]]
        mask[1+2*x:1+2*_x+1, 1+2*y:1+2*_y+1, 1+2*z:1+2*_z+1] = v
    return mask

@jit(nopython=True)
def compute_sum(mask, mat):
    s, x, y, z = 0, *mask.shape
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if mask[i][j][k]: s += mat[i][j][k]
    return s

mat = build_matrix(sortx, sorty, sortz)
mask = compute_mask(cuboids)

x, _x, y, _y, z, _z = x_pos[-47], x_pos[48], y_pos[-46], y_pos[48], z_pos[-47], z_pos[49]
ans_1 = compute_sum(mask[1+2*x:1+2*_x+1, 1+2*y:1+2*_y+1, 1+2*z:1+2*_z+1], mat[1+2*x:1+2*_x+1, 1+2*y:1+2*_y+1, 1+2*z:1+2*_z+1])
ans_2 = compute_sum(mask, mat)
print(f'part-1 answer : {ans_1}')
print(f'part-2 answer : {ans_2}')