from functools import cmp_to_key


def convert_j(counts):
    no_j = {s: v for s, v in counts.items() if s != "J"}
    if len(no_j) == 0:
        counts = {"K": 5}
    else:
        max_symbs = [s for s, v in no_j.items() if v == max(no_j.values())]
        counts[max(max_symbs, key=lambda x: symbols[x])] += counts["J"]
        counts.pop("J")
    return counts


def kind(hand, part):
    counts = {s: hand.count(s) for s in set(hand)}
    if part == 2 and "J" in counts:
        counts = convert_j(counts)
    match len(counts):
            case 1: return "five-of-a-kind"
            case 2: return "full-house" if 2 in counts.values() else "four-of-a-kind"
            case 3: return "two-pair" if 2 in counts.values() else "three-of-a-kind"
            case 4: return "one-pair"
            case _: return "high-card"


def compare(kind, hand_1, hand_2):
    if kinds[kind(hand_1)] == kinds[kind(hand_2)]:
        for s1, s2 in zip(hand_1, hand_2):
            if symbols[s1] != symbols[s2]:
                return symbols[s1] - symbols[s2]
    else:
        return kinds[kind(hand_1)] - kinds[kind(hand_2)]


lines = [m for m in [l.strip().split(" ") for l in open("input").readlines()]]
hands, bids = [l[0] for l in lines], [int(l[1]) for l in lines]
symbols = {s: 13 - i for i, s in enumerate(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])}
kinds = {k: 13 - i for i, k in enumerate(["five-of-a-kind", "four-of-a-kind", "full-house", "three-of-a-kind", "two-pair", "one-pair", "high-card"])}

for part in (1, 2):
    symbols["J"] -= symbols["J"] if part == 2 else 0
    sorted_hands = sorted(hands, key=cmp_to_key(lambda x, y: compare(lambda z: kind(z, part), x, y)))
    print(sum((sorted_hands.index(hand) + 1) * bid for hand, bid in zip(hands, bids)))
