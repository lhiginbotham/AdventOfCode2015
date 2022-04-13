inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

stats = dict()

for line in inp:
    components = line.split()
    reindeer = components[0]
    stats[reindeer] = dict()
    reindeer = components[0]
    stats[reindeer]['speed'] = int(components[3])
    stats[reindeer]['endurance'] = int(components[6])
    stats[reindeer]['rest'] = int(components[-2])
    stats[reindeer]['position'] = 0
    stats[reindeer]['points'] = 0

def is_running(current_time, endurance, rest):
    if current_time % (endurance + rest) < endurance:
        return True

len_of_race = 2504
for i in range(len_of_race):
    for reindeer in stats.values():
        speed = reindeer['speed']
        if is_running(i, reindeer['endurance'], reindeer['rest']):
            reindeer['position'] += speed

    best_position = 0
    for reindeer in stats.values():
        if best_position < reindeer['position']:
            best_position = reindeer['position']

    for reindeer in stats.values():
        if reindeer['position'] == best_position:
            reindeer['points'] += 1

best_points = 0
for reindeer in stats.values():
    reindeer_points = reindeer['points']
    if reindeer_points > best_points:
        best_points = reindeer_points

print(best_points)
