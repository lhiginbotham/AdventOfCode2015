# how many ways to hold 150 liters in the containers you have (input)

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = int(inp[i].rstrip())

# sort to optimize (cutting out early if filling up big containers)
inp.sort()
ways_to_hold = 0

# iterate over bitfields representing usage/non-usage of the different containers
for i in range(2 ** len(inp)):
    sum = 0
    for bit in range(len(inp)):
        if i & (1 << bit) == 0:
            continue

        sum += inp[len(inp) - 1 - bit]
        if sum > 150:
            break

    if sum == 150:
        ways_to_hold += 1

print(ways_to_hold)
