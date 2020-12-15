import numpy as np

_in = np.array([2,0,6,12,1,3])
t, n = 2020, len(_in) # t = 2020 for part 1
idx = -np.ones(t)
idx[_in] = np.arange(len(_in))
_in = np.concatenate([_in, np.zeros(t-len(_in))]).astype(int)

def _next(_in, turn):
    m = turn+n-1
    idx[_in[n+turn-2]] = n+turn-2
    l = idx[_in[n+turn-1]]
    _in[n+turn] = 0 if l == -1 else m-l

for turn in range(t-n):
    _next(_in, turn)

print(f'answer: {_in[t-1]}')

