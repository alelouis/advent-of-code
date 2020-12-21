d = dict()
for l in open('input'):
    recipe = l.split(' (contains ')
    ingredients, allergens = recipe[0].split(' '), set(recipe[1].strip()[:-1].split(', '))
    for allergen in allergens:
        if allergen in d: d[allergen] = [v for v in ingredients if v in d[allergen]] 
        else: d[allergen] = ingredients

def delete_lonely(d):
    for key_1 in d:
        if len(d[key_1]) == 1:
            for key_2 in d:
                if key_1 != key_2 and d[key_1][0] in d[key_2]:
                    d[key_2].remove(d[key_1][0])

while not all([len(d[k])==1 for k in d]):
    delete_lonely(d)

recipes =  [l.split(' (contains ')[0].split(' ') for l in open('input')]
answer = sum([i not in [v[0] for k,v in d.items()] for r in recipes for i in r])
print(f'part-1 answer: {answer}')

answer = ','.join([d[k][0] for k in sorted([k for k in d.keys()])])
print(f'part-2 answer: {answer}')