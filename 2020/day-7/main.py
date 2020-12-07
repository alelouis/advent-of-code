def parse_line(line):
    s = line.split(' ')
    inside = [[w, ww  + www] for w, ww, www in zip(s, s[1:], s[2:]) if w.isnumeric()]
    return s[0] + s[1], inside
    
rules = {parse_line(line)[0]:parse_line(line)[1] for line in open('input')}

def go_shiny(rules, bag):
    return True if bag == 'shinygold' else sum([go_shiny(rules, b) for a, b in rules[bag]]) > 0

def go_deep(rules, bag):
    return sum([int(a) * (1 + go_deep(rules, b)) for a, b in rules[bag]]) if rules[bag] else 0

part_1 = sum([go_shiny(rules, parse_line(line)[0]) for line in open('input')]) - 1
print(f'part-1 answer: {part_1}')

part_2 = go_deep(rules, 'shinygold') 
print(f'part-2 answer: {part_2}')       