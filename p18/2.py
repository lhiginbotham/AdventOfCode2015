import copy

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = [ c for c in inp[i].rstrip() ]

# grid is broken and instead the four corner lights are stuck on
def stick_the_lights(input):
    input[0][0] = '#'
    input[0][99] = '#'
    input[99][0] = '#'
    input[99][99] = '#'

stick_the_lights(inp)

def write_new_state(input, output, row, col):
    num_neighbors_lit = 0

    for inc_row in [-1, 0, 1]:
        for inc_col in [-1, 0, 1]:
            if (row == 0 and inc_row == -1) or (row == 99 and inc_row == 1) or \
                    (col == 0 and inc_col == -1) or (col == 99 and inc_col == 1) or \
                    (inc_row == 0 and inc_col == 0):
                continue

            if input[row + inc_row][col + inc_col] == '#':
                num_neighbors_lit += 1

    # A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
    # A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
    if input[row][col] == '#':
        output[row][col] = '#' if num_neighbors_lit in (2, 3) else '.'
    elif input[row][col] == '.':
        output[row][col] = '#' if num_neighbors_lit == 3 else '.'

for i in range(100):
    next_frame = copy.deepcopy(inp)
    for row in range(100):
        for col in range(100):
            write_new_state(inp, next_frame, row, col)
    inp = next_frame
    stick_the_lights(inp)

num_on = 0
for row in inp:
    for light in row:
        if light == '#':
            num_on += 1

print(num_on)
