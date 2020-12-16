def parse():
    ls = [l.split(':') for l in open('input') if l != '\n']
    na = [l[0] for l in ls if len(l) == 2 and l[1] != '\n']
    co = [l[1].strip().split(' or ') for l in ls if len(l) == 2 and l[1] != '\n']
    co = [c[0].split('-') + c[1].split('-') for c in co]
    tick = [l[0].strip().split(',') for l in ls if len(l)==1]
    return tick[0], tick[1:], na, co

my_ticket, nearby_tickets, names, conditions = parse()

def apply_condition(value, cond):
    return int(cond[0]) <= int(value) <= int(cond[1]) or int(cond[2]) <= int(value) <= int(cond[3])

invalid_sum, valid_tickets = 0, []
for ticket in nearby_tickets:
    valid_ticket = True
    for value in ticket:
        valid_value = sum([apply_condition(value, cond) for cond in conditions])
        valid_ticket &= bool(valid_value)
        if not valid_value: invalid_sum += int(value)
    if valid_ticket: valid_tickets.append(ticket)

print(f'part-1 answer: {invalid_sum}')

def possible_fields(names, conditions, ticket):
    possible_fields_ticket = []
    for value in ticket:
        fields = []
        for i, cond in enumerate(conditions):
            if apply_condition(value, cond): fields.append(names[i])
        possible_fields_ticket.append(fields)
    return possible_fields_ticket

def delete_lonely(t_glob):
    uniques, cleaned = [p[0] for p in t_glob if len(p)==1], []
    for p in t_glob:
        for u in uniques:
            if len(p) != 1 and u in p: p.remove(u)
        cleaned.append(p)
    return cleaned

def isolate_lonely(t_glob):
    iso = {name:i for i, p in enumerate(t_glob) for name in p if sum([name in pp for pp in t_glob]) == 1 and len(p) != 1}
    for k, v in iso.items():
        t_glob[v] = [k]
    return t_glob

t_glob, answer = [names]*len(ticket), 1
for ticket in valid_tickets:
    t_loca = possible_fields(names, conditions, ticket)
    t_glob = [list(set(a) & set(b)) for a, b in zip(t_glob, t_loca)]

while not all([len(p)==1 for p in t_glob]):
    t_glob = delete_lonely(t_glob)
    t_glob = isolate_lonely(t_glob)

for i, field in enumerate(t_glob):
    if field[0].split(' ')[0]=='departure':
        answer *= int(my_ticket[i])

print(f'part-2 answer: {answer}')
