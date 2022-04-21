# Each elf 1 to N delivers 10*elf_number to the houses they visit
# and each elf visits elf_number*k for k = 1 to infinity.
# What house is the lowest house number to get *at least* goal_num_presents?

goal_num_presents = 34000000

# elf numbered (goal_num_presents/10) will visit their first house and
# drop off exactly goal_num_presents in addition to all that was
# delivered by other elves. Good end point to limit the amount of computation needed
max_house = goal_num_presents // 10 
houses_visited = [ 0 for i in range(max_house) ]

for i in range(1, max_house + 1):
    index = i - 1
    while index < max_house:
        houses_visited[index] += 10 * i
        index += i

for i in range(len(houses_visited)):
    if houses_visited[i] >= goal_num_presents:
        print("answer = " + str(i + 1))
        break
