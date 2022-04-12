import itertools

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

person_to_people_happiness = dict() # { "name": { "name": happiness_sitting_next_to, ... }, ... }

for line in inp:
    person, _, modifier, amount, *_, other_person_dot = line.split()
    amount = int(amount) if modifier == 'gain' else -int(amount)
    other_person = other_person_dot[:-1]
    if person not in person_to_people_happiness:
        person_to_people_happiness[person] = dict()
    person_to_people_happiness[person][other_person] = amount

best_happiness = None
for p in itertools.permutations(person_to_people_happiness.keys()):
    happiness = sum([
        # happiness is a two-way street
        person_to_people_happiness[p[i]][p[(i + 1) % len(p)]] + person_to_people_happiness[p[(i + 1) % len(p)]][p[i]]
        for i in range(len(p))
    ])
    if best_happiness == None or best_happiness < happiness:
        best_happiness = happiness

print(best_happiness)
