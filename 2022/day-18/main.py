def move(dx, dy, dz, cube): return (cube[0]+dx, cube[1]+dy, cube[2]+dz)
def mind(cubes, dim): return min(cube[dim] for cube in cubes)
def maxd(cubes, dim): return max(cube[dim] for cube in cubes)
def surrounding(cube): return {move(x, y, z, cube) for x, y, z in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))}
def surface(cubes): return sum(6 - sum(s in cubes for s in surrounding(cube)) for cube in cubes)

cubes = {(eval(cube)) for cube in open('input').read().splitlines()}
box = {(x, y, z) for z in range(mind(cubes, 2)-2, maxd(cubes, 2)+2) for y in range(mind(cubes, 1)-2, maxd(cubes, 1)+2) for x in range(mind(cubes, 0)-2, maxd(cubes, 0)+2)}

stack, visited = [(mind(cubes, 0)-2, mind(cubes, 1)-2, mind(cubes, 1)-2)], set()
while stack:
    node = stack.pop()
    visited.add(node)
    for n in (surrounding(node) & box) - cubes:
        if n not in visited:
            stack.append(n)

print(surface(cubes))
print(surface(cubes)-surface(box-visited-cubes))