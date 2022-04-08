inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

total_file_characters = 0
total_double_encoded_characters = 0
for line in inp:
    len_orig = len(line)
    total_file_characters += len_orig

    total_double_encoded_characters += (
        len_orig +
        2 + # new encapsulating quotes
        line.count('"') +
        line.count('\\')
    )

print(total_double_encoded_characters - total_file_characters)
