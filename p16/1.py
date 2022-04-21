inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

what_i_know = dict([
    ('children', 3),
    ('cats', 7),
    ('samoyeds', 2),
    ('pomeranians', 3),
    ('akitas', 0),
    ('vizslas', 0),
    ('goldfish', 5),
    ('trees', 3),
    ('cars', 2),
    ('perfumes', 1)
])

possible_sues = []

number_sue = 0
for line in inp:
    number_sue += 1

    not_the_sue = False
    possible_sue_items = dict()
    items = line.split(": ", 1)[1].split(', ')
    for item in items:
        item_name, item_quantity = item.split(': ')
        item_quantity = int(item_quantity)
        if item_quantity != 0:
            if what_i_know[item_name] != item_quantity:
                not_the_sue = True
                break

        possible_sue_items[item_name] = item_quantity

    if not_the_sue:
        continue

    possible_sues.append((number_sue, possible_sue_items))

print('Multiple Sues, pick the one you know the most about')
print(possible_sues)