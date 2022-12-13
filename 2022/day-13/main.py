name = 'input'
lines = open(name).read().split('\n\n')

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if compare(eval(arr[j]), eval(arr[j+1])):
                arr[j], arr[j+1] = arr[j+1], arr[j]

def compare(left, right):
    lend = rend = False
    lgen, rgen = (l for l in left), (r for r in right)
    right_order = None
    while not lend and not rend and right_order is None:
        try: lelem = next(lgen)
        except StopIteration: lelem, lend = None, True
        try: relem = next(rgen)
        except StopIteration: relem, rend = None, True
        if rend and not lend: return False
        if lend and not rend: return True
        if isinstance(lelem, list) and isinstance(relem, list): right_order = compare(lelem, relem)
        if isinstance(lelem, int) and isinstance(relem, list): right_order = compare([lelem], relem)
        if isinstance(lelem, list) and isinstance(relem, int): right_order = compare(lelem, [relem])
        if isinstance(lelem, int) and isinstance(relem, int):
            if lelem < relem: return True
            if relem < lelem: return False
    return right_order

print(sum(i for i, pair in enumerate(lines, 1) if compare(eval(pair.split('\n')[0]), eval(pair.split('\n')[1]))))

lines = open(name).read().replace("\n\n", "\n").splitlines() + ['[[2]]', '[[6]]']
bubbleSort(lines)
print((1 + lines[::-1].index('[[2]]'))*(1 + lines[::-1].index('[[6]]')))