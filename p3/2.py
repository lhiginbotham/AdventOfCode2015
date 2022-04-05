from collections import defaultdict

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

presents_dropped_map = defaultdict(lambda: defaultdict(lambda: 0))
presents_dropped_map[0][0] += 2
santa_pos = [0, 0]
robo_santa_pos = [0, 0]
pos = santa_pos
for direction in inp[0]:
    next_pos = None
    old_pos = pos
    if pos is santa_pos:
        next_pos = robo_santa_pos
    else:
        next_pos = santa_pos

    if direction == '^':
        pos[1] += 1 
    elif direction == '>':
        pos[0] += 1
    elif direction == 'v':
        pos[1] -= 1
    elif direction == '<':
        pos[0] -= 1

    presents_dropped_map[pos[0]][pos[1]] += 1
    old_pos = pos
    pos = next_pos

print(f'houses that had presents dropped at it: {sum([len(x.values()) for x in presents_dropped_map.values()])}')
