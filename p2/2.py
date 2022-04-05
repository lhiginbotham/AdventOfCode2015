import itertools

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

total_wrapping_paper = 0
total_ribbon_needed = 0
for line in inp:
    (length, width, height) = line.split('x')
    length = int(length)
    width = int(width)
    height = int(height)

    combos = [combo for combo in itertools.combinations([length, width, height], 2)]
    smallest_side = min(combos, key=lambda combo: combo[0] * combo[1])

    surface_area = 2 * (combos[0][0]*combos[0][1] + combos[1][0]*combos[1][1] + combos[2][0]*combos[2][1])
    slack = smallest_side[0] * smallest_side[1]
    volume = length * width * height

    total_wrapping_paper += surface_area + slack
    total_ribbon_needed += 2 * (smallest_side[0] + smallest_side[1]) + volume

print(f'total_surface_area: {total_wrapping_paper}')
print(f'total_ribbon_needed: {total_ribbon_needed}')
