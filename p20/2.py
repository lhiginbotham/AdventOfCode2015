import math

# Note: problem changed compared to 1.py,
# rather than the usual of "calculate some other
# statistic/knowledge in addition to what you already did"

# Each elf 1 to N delivers 11*elf_number to the houses they visit
# and each elf visits elf_number*k for k = 1 to 50.
# What house is the lowest house number to get *at least* goal_num_presents?

goal_num_presents = 34000000

# elf numbered roughly (goal_num_presents/11) will visit their first house and
# drop off guaranteed more than goal_num_presents in addition to all that was
# delivered by other elves. Good end point to limit amount of computation needed
max_house = math.ceil(goal_num_presents // 11)
houses_visited = [ 0 for i in range(max_house) ]

for i in range(1, max_house + 1):
    index = i - 1
    houses_elf_visited = 0
    while index < max_house and houses_elf_visited < 50:
        houses_visited[index] += 11 * i
        index += i
        houses_elf_visited += 1 # elves only visit 50 houses so they will quit once this is hit

for i in range(len(houses_visited)):
    if houses_visited[i] >= goal_num_presents:
        print("answer = " + str(i + 1))
        break
