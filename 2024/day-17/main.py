from copy import copy


def literal(operand):
    return operand


def combo(operand):
    if 0 <= operand <= 3: return operand
    else:
        match operand:
            case 4: return registers['A']
            case 5: return registers['B']
            case 6: return registers['C']
            case 7: raise Exception('7 Should not appear')


def process_instruction(opcode, operand, instruction_pointer):
    out = None
    match opcode:
        case 0:  # adv
            num = registers['A']
            den = 2 ** combo(operand)
            result = num // den
            registers['A'] = result
            instruction_pointer += 2
        case 1:  # bxl
            res = registers['B'] ^ literal(operand)
            registers['B'] = res
            instruction_pointer += 2
        case 2:  # bst
            res = combo(operand) % 8
            registers['B'] = res
            instruction_pointer += 2
        case 3:  # jnz
            if registers['A'] != 0:
                instruction_pointer = literal(operand)
            else:
                instruction_pointer += 2
        case 4:  # bxc
            res = registers['B'] ^ registers['C']
            registers['B'] = res
            instruction_pointer += 2
        case 5:  # out
            res = combo(operand) % 8
            out = res
            instruction_pointer += 2
        case 6:  # bdv
            num = registers['A']
            den = 2 ** combo(operand)
            result = num // den
            registers['B'] = result
            instruction_pointer += 2
        case 7:  # cdv
            num = registers['A']
            den = 2 ** combo(operand)
            result = num // den
            registers['C'] = result
            instruction_pointer += 2

    return out, instruction_pointer


def run_program(a_value):
    registers['A'] = a_value
    ip, out = 0, []
    while ip < len(program):
        instruction, operand = program[ip], program[ip + 1]
        o, ip = process_instruction(instruction, operand, ip)
        out.append(o)
    return [o for o in out if o is not None]


def flatten(S):
    if not S: return S
    if isinstance(S[0], list): return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])


def find_index(register, idx):
    """
    Iteratively change register digit by digit (in base 8) until output program is original program.
    Many digits may be possible for a given index, this function has to branch.

    This comes from the observation that the output program changes every 8 (decimal) increments in register A.
    """
    if idx == 16: return int(''.join(map(str, register)))
    potential_register = []
    for value in range(8):  # Iterating in base 8
        register[idx] = value
        a_value = int("".join(map(str, register)), 8)  # Convert to decimal A register
        out = run_program(a_value)
        out = [0] * (len(program) - len(out)) + out  # Prepend 0 for low A values
        if out[-(idx + 1)] == program[-(idx + 1)]:
            potential_register.append(copy(register))
    return [find_index(r, idx + 1) for r in potential_register]  # Branch


data = open('input').readlines()
registers = {r: int(data[i].strip().split(': ')[1]) for r, i in zip("ABC", range(3))}
program = [int(d) for d in data[-1].split(': ')[1].split(',')]
part1 = ",".join(map(str, run_program(registers['A'])))
print(part1)

min_reg = min(flatten(find_index([0] * 16, 0)))
part2 = int(str(min_reg), 8)
print(part2)
