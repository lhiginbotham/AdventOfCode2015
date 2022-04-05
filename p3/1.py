from collections import defaultdict

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

presents_dropped_map = defaultdict(lambda: defaultdict(lambda: 0))
presents_dropped_map[0][0] += 1
pos = (0, 0)
for direction in inp[0]:
    if direction == '^':
        pos = (pos[0], pos[1] + 1)
    elif direction == '>':
        pos = (pos[0] + 1, pos[1])
    elif direction == 'v':
        pos = (pos[0], pos[1] - 1)
    elif direction == '<':
        pos = (pos[0] - 1, pos[1])

    presents_dropped_map[pos[0]][pos[1]] += 1

print(f'houses that had presents dropped at it: {sum([len(x.values()) for x in presents_dropped_map.values()])}')
