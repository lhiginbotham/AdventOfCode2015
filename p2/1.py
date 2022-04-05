inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

total_surface_area = 0
for line in inp:
    (length, width, height) = line.split('x')
    length = int(length)
    width = int(width)
    height = int(height)

    lw = length * width
    lh = length * height
    wh = width * height

    surface_area = 2 * (lw + lh + wh)
    slack = min(lw, lh, wh)

    total_surface_area += surface_area + slack

print(total_surface_area)
