from collections import deque
from math import lcm


def get_modules(conf):
    outputs = dict()
    types = dict()
    for mod in conf:
        left, right = mod.strip().split(" -> ")
        if left == "broadcaster":
            ty, na = ("bc", left)
        else:
            ty, na = (left[0], left[1:])
        destinations = right.split(", ")
        types[na] = ty
        outputs[na] = destinations

    outputs['rx'] = None
    types["output"] = "out"
    types["rx"] = "rx"
    inputs = {k: [] for k in types}

    for mod in outputs:
        for j in outputs:
            if outputs[j] is not None and mod in outputs[j]:
                inputs[mod].append(j)

    mods = {k: {"inputs": None, "outputs": None} for k in set(inputs.keys())}
    for mod in mods:
        mods[mod]["inputs"] = inputs[mod]
        if mod in outputs:
            mods[mod]["outputs"] = outputs[mod]

    return mods, types


def initialize_states(mods, types):
    states = dict()
    for module, ty in types.items():
        if ty == "&":
            states[module] = {k: False for k in mods[module]["inputs"]}
        if ty in ["rx", "out", "%"]:
            states[module] = False
    return states


def process_signal(mods, types, states, in_sig):
    (s, d, level), out_sig = in_sig, []
    if types[d] == "bc":
        out_sig = [(d, out, level) for out in mods[d]["outputs"]]
    elif types[d] == "%":
        if not level:
            states[d] = not states[d]
            out_sig = [(d, out, states[d]) for out in mods[d]["outputs"]]
    elif types[d] == "&":
        states[d][s] = level
        out_sig = [(d, out, not all(states[d].values())) for out in mods[d]["outputs"]]
    return out_sig


configuration = open("input").readlines()
modules, types = get_modules(configuration)
states = initialize_states(modules, types)
n_signals = high_signals = press = 0
search_for, found = modules[modules['rx']['inputs'][0]]['inputs'], dict()  # lol

signals = deque()
while True:
    press += 1
    signals.append(("button", "broadcaster", False))
    while signals:
        signal = signals.popleft()
        n_signals += 1
        high_signals += signal[-1]
        new_signals = process_signal(modules, types, states, signal)
        for new_signal in new_signals:
            signals.append(new_signal)
            _, d, level = new_signal
            if d in search_for and not level and d not in found:
                found[d] = press
    if press == 1000:
        print((n_signals - high_signals) * high_signals)
    if all(s in found for s in search_for):
        print(lcm(*found.values()))
        break
