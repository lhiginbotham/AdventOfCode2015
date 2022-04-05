import itertools

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

LightMap = list[list[bool]]

lights = [[False] * 1000 for x in range(1000)]

def toggle(lights: LightMap, x: int, y: int) -> None:
    lights[x][y] = (lights[x][y] == False)

def set_to(lights: LightMap, x: int, y: int, on_off: bool) -> None:
    lights[x][y] = on_off

for instruction in inp:
    components = instruction.split()
    if components[0] == 'toggle':
        (startX, startY) = [ int(x) for x in components[1].split(',') ]
        (endX, endY)     = [ int(x) for x in components[3].split(',') ]

        for coord in itertools.product(
            range(min(startX, endX), max(startX, endX) + 1),
            range(min(startY, endY), max(startY, endY) + 1)
        ):
            toggle(lights, coord[0], coord[1])
    else:
        on_off_val = components[1] == 'on'

        (startX, startY) = [ int(x) for x in components[2].split(',') ]
        (endX, endY)     = [ int(x) for x in components[4].split(',') ]

        for coord in itertools.product(
            range(min(startX, endX), max(startX, endX) + 1),
            range(min(startY, endY), max(startY, endY) + 1)
        ):
            set_to(lights, coord[0], coord[1], on_off_val)

lit_lights_count = 0
for row in lights:
    for light in row:
        if light:
            lit_lights_count += 1

print(lit_lights_count)
