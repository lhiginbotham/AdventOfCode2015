inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

a = 1
b = 0

curr_instruction = 0
while curr_instruction < len(inp):
    instr, rest = inp[curr_instruction].split(' ', maxsplit=1)
    if instr == 'hlf':
        reg = rest
        if reg == 'a':
            a //= 2
        else:
            b //= 2
        curr_instruction += 1
    elif instr == 'tpl':
        reg = rest
        if reg == 'a':
            a *= 3
        else:
            b *= 3
        curr_instruction += 1
    elif instr == 'inc':
        reg = rest
        if reg == 'a':
            a += 1
        else:
            b += 1
        curr_instruction += 1
    elif instr == 'jmp':
        offset = rest
        curr_instruction += int(offset)
    elif instr == 'jie':
        reg, offset = rest.split(', ')
        reg_val = None

        if reg == 'a':
            reg_val = a
        else:
            reg_val = b

        if (reg_val % 2) == 0:
            curr_instruction += int(offset)
        else:
            curr_instruction += 1
    elif instr == 'jio':
        reg, offset = rest.split(', ')
        reg_val = None

        if reg == 'a':
            reg_val = a
        else:
            reg_val = b

        if reg_val == 1:
            curr_instruction += int(offset)
        else:
            curr_instruction += 1

print(b)
