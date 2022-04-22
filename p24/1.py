from functools import reduce
import itertools

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = int(inp[i].rstrip())

best_quantum_entanglement = None

# number of packages to fit into Santa's compartment
for i in range(1, len(inp) - 1):
    # since we are starting with the smallest amount of packages to fit into Santa's compartment,
    # we can stop adding packages to Santa's compartment if we find an acceptable answer and stay within
    # this "number of packages" realm in order to find the lowest quantum entanglement
    print(i)
    for pick_i_packages in itertools.combinations(inp, i):
        weight_to_balance = sum(pick_i_packages)
        remaining_packages = inp[:]
        for package in pick_i_packages:
            remaining_packages.remove(package)

        remaining_packages_weight = sum(remaining_packages)
        if 2 * weight_to_balance != remaining_packages_weight:
            continue

        for j in range(1, len(remaining_packages) - 1):
            for pick_j_packages in itertools.combinations(remaining_packages, j):
                if sum(pick_j_packages) != weight_to_balance:
                    continue

                third_group = remaining_packages[:]
                for package in pick_j_packages:
                    third_group.remove(package)

                if sum(third_group) != weight_to_balance:
                    continue

                # we found an answer!
                quantum_entanglement = reduce(lambda x, y: x * y, pick_i_packages, 1)
                if best_quantum_entanglement is None or quantum_entanglement < best_quantum_entanglement:
                    best_quantum_entanglement = quantum_entanglement
                    print('best seen updated to (and honestly, this is the answer since the data is sorted):\n' + str(best_quantum_entanglement))
                    exit()

#     if best_quantum_entanglement is not None:
#         break

# print(best_quantum_entanglement)

