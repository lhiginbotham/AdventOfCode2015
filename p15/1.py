from collections import defaultdict
import itertools

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

ingredients = []

for line in inp:
    arr = line.split()
    ingredients.append([ int(x if x[-1] != ',' else x[:-1] ) for x in [arr[2], arr[4], arr[6], arr[8], arr[10]] ])

best_score = -1
for recipe in itertools.combinations_with_replacement(range(len(ingredients)), 100):
    ingredient_quantities = defaultdict(lambda: 0)
    for teaspoon_of_ingredient in recipe:
        ingredient_quantities[teaspoon_of_ingredient] += 1

    recipe_attributes = defaultdict(lambda: 0)
    for ingredient_index in ingredient_quantities.keys():
        teaspoons_of_ingredient = ingredient_quantities[ingredient_index]
        for i in range(len(ingredients[ingredient_index]) - 1):
            attribute_val = ingredients[ingredient_index][i]
            recipe_attributes[i] += attribute_val * teaspoons_of_ingredient

    attributes = list(recipe_attributes.values())
    tasty_score = 0
    if all(x > 0 for x in attributes):
        tasty_score = 1
        for x in attributes:
            tasty_score *= x

    if best_score < tasty_score:
        best_score = tasty_score

print(best_score)
