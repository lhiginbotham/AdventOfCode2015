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
least_amount_of_containers_needed = None
number_of_ways_to_fill_least_amount_of_containers = 1
for i in range(2 ** len(inp)):
    sum = 0
    number_used = 0
    for bit in range(len(inp)):
        if i & (1 << bit) == 0:
            continue

        sum += inp[len(inp) - 1 - bit]
        number_used += 1
        if sum > 150:
            break

    if sum == 150:
        ways_to_hold += 1
        if least_amount_of_containers_needed is None or number_used < least_amount_of_containers_needed:
            least_amount_of_containers_needed = number_used
            number_of_ways_to_fill_least_amount_of_containers = 1
        elif number_used == least_amount_of_containers_needed:
            number_of_ways_to_fill_least_amount_of_containers += 1

print(f'ways_to_hold = {ways_to_hold}, least_amount_of_containers_needed = {least_amount_of_containers_needed}, number_of_ways_to_fill_least_amount_of_containers = {number_of_ways_to_fill_least_amount_of_containers}')
