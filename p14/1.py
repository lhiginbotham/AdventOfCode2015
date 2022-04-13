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

def is_running(current_time, endurance, rest):
    if current_time % (endurance + rest) < endurance:
        return True

len_of_race = 2504
for i in range(len_of_race):
    for reindeer in stats.values():
        print(reindeer)
        speed = reindeer['speed']
        if is_running(i, reindeer['endurance'], reindeer['rest']):
            reindeer['position'] += speed

best_distance = 0
for reindeer in stats.values():
    reindeer_position = reindeer['position']
    if reindeer_position > best_distance:
        best_distance = reindeer_position

print(best_distance)
