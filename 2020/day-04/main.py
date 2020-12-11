import re

""" --> Part 1 <--"""

filepath = 'input'
passports = []
current_passport = ''

with open(filepath) as fp:
    for line in (fp):
        if line == '\n':
            passports.append(current_passport)
            current_passport = ''
        else:
            current_passport += ' ' + line.rstrip('\n')

correct_passports = 0
expected_fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
regex = re.compile('([a-z]+:)')
for passport in passports:
    current_passport_fields = list(regex.findall(passport))
    valid = True
    for field in expected_fields: 
        valid &= field in current_passport_fields
    if valid: correct_passports +=1
answer = correct_passports
print(f'part-1 answer: {answer}')

""" --> Part 2 <--"""

filepath = 'input'
passports = []
current_passport = ''

with open(filepath) as fp:
    for line in (fp):
        if line == '\n':
            passports.append(current_passport)
            current_passport = ''
        else:
            current_passport += ' ' + line.rstrip('\n')

correct_passports = 0
fields_regex = {
    'byr' : r'(byr:)(\d{4})', 
    'iyr' : r'(iyr:)(\d{4})', 
    'eyr' : r'(eyr:)(\d{4})', 
    'hgt' : r'(hgt:)(\d+)(cm|in)', 
    'hcl' : r'(hcl:)(#[0-9a-f]{6})', 
    'ecl' : r'(ecl:)(amb|blu|brn|gry|grn|hzl|oth)', 
    'pid' : r'(pid:)(\d{9})'}

for passport in passports:
    valid = True
    for field in fields_regex:
        regex = re.compile(fields_regex[field])
        match_result = regex.search(passport)
        if match_result is not None:      
            groups = match_result.groups()
            if field == 'byr':
                year = int(groups[1])
                valid &= 1920 <= year <= 2002
            if field == 'iyr':
                year = int(groups[1])
                valid &= 2010 <= year <= 2020
            if field == 'eyr':
                year = int(groups[1])
                valid &= 2020 <= year <= 2030
            if field == 'hgt':
                height = int(groups[1])
                unit = groups[2]
                if unit == 'cm':
                    valid &= 150 <= height <= 193
                else:
                    valid &= 59 <= height <= 76 
            pass
        else:
            valid = False
    if valid: correct_passports +=1
        
answer = correct_passports
print(f'part-2 answer: {answer}')