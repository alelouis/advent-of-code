import math

hex_str = open('input').readline()
bin = f'{int(hex_str, 16):0>{len(hex_str)*4}b}'

rules = {
    0:'sum',
    1:'math.prod',
    2:'min',
    3:'max',
    5:'>',
    6:'<',
    7:'==',
    }

def parse_packet(b):
    V, T = int(b[0:3], 2), int(b[3:6], 2)
    if T == 4:
        h, parts = 6, []
        while b[h] == '1':
            parts.append(b[h+1:h+5])
            h += 5
        parts.append(b[h+1:h+5])
        return [V, T, h+5, int(''.join(parts), 2)]  
    else:
        I, packets = b[6], []
        if I == '0': 
            L = b[7:22]
            p = parse_packet(b[22:22+int(L, 2)])
            packets.append(p)
            h = p[2]
            while h != int(L, 2):
                p = parse_packet(b[22+h:22+int(L, 2)])
                packets.append(p)
                h += p[2]
            return [V, T, h+22, packets]
        elif I == '1':
            L = b[7:18]
            h = 0
            for _ in range(int(L, 2)):
                p = parse_packet(b[18+h:])
                packets.append(p)
                h += p[2]
            return [V, T, h+18, packets]
                
def sum_v(pcks):
    if pcks[1] == 4: return pcks[0]
    else: return pcks[0] + sum(sum_v(p) for p in pcks[-1])

def unwrap(packet):
    if packet[1] == 4:
        return packet[-1]
    if packet[1] in [5, 6, 7]:
        pk1, pk2 = packet[-1]
        return f"{unwrap(pk1)}{rules[packet[1]]}{unwrap(pk2)}"
    else:
        s = f"{rules[int(packet[1])]}({[unwrap(p) for p in packet[-1]]})"
        s = s.replace("\"", '').replace("'", '').replace('\\', '')
        return s

packets = parse_packet(bin)
print(f'part-1 answer : {sum_v(packets)}')
print(f'part-2 answer : {eval(unwrap(packets))}')