inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

total_file_characters = 0
total_characters = 0
for line in inp:
    total_file_characters += len(line)
    string = line[1:-1]

    i = 0
    len_str = len(string)
    while i < len_str:
        if string[i] == '\\':
            if string[i + 1] == 'x':
                i += 3
            else:
                i += 1

        total_characters += 1
        i += 1

print(total_file_characters - total_characters)
