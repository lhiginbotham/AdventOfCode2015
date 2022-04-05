inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

floor = 0
position = 0
traversal = inp[0]
for x in traversal:
    position += 1
    if x == '(':
        floor += 1
    else:
        floor -= 1

print(floor)
