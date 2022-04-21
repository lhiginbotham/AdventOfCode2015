from collections import defaultdict
from dataclasses import replace
from enum import unique

replacements = defaultdict(lambda: list())
start_molecule = None
with open('input.txt') as f:
    done_with_replacements = False
    for line in f.readlines():
        line = line.rstrip()
        if len(line) < 1:
            done_with_replacements = True
            continue

        if not done_with_replacements:
            input, product = line.split(' => ')
            replacements[input].append(product)
        else:
            start_molecule = line

possible_replacements = defaultdict(lambda: set())
for replaceable in replacements:
    for i in range(len(start_molecule) - len(replaceable) + 1):
        if start_molecule[i:i + len(replaceable)] == replaceable:
            outputs = replacements[replaceable]
            for output in outputs:
                possible_replacements[(i, len(replaceable))].add(output)

unique_new_molecules = set()
for replacement in possible_replacements:
    split_molecule = [ c for c in start_molecule ]

    for i in range(replacement[1]):
        split_molecule.pop(replacement[0])

    for new_string in possible_replacements[replacement]:
        new_molecule = split_molecule[:]
        new_molecule.insert(replacement[0], new_string)
        unique_new_molecules.add(''.join(new_molecule))

print(len(unique_new_molecules))
