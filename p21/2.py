# Puzzle Input (Boss's Stats)
#
# Hit Points: 104
# Damage: 8
# Armor: 1

# Shop Items
# Weapons:    Cost  Damage  Armor
# Dagger        8     4       0
# Shortsword   10     5       0
# Warhammer    25     6       0
# Longsword    40     7       0
# Greataxe     74     8       0

# Armor:      Cost  Damage  Armor
# Leather      13     0       1
# Chainmail    31     0       2
# Splintmail   53     0       3
# Bandedmail   75     0       4
# Platemail   102     0       5

# Rings:      Cost  Damage  Armor
# Damage +1    25     1       0
# Damage +2    50     2       0
# Damage +3   100     3       0
# Defense +1   20     0       1
# Defense +2   40     0       2
# Defense +3   80     0       3

# Player starts with the first attack in every battle.
# An attack does max(1, damage - armor) to the other character.
# A player must have a weapon, can have 0 or 1 armor, can have 0, 1, or 2 rings

import itertools

boss_start_health = 104
boss_damage = 8
boss_armor = 1

weapons = [
    (8, 4, 0), # Dagger
    (10, 5, 0), # Shortsword
    (25, 6, 0), # Warhammer
    (40, 7, 0), # Longsword
    (74, 8, 0), # Greataxe
]

armor = [
    (0, 0, 0), # None
    (13, 0, 1), # Leather
    (31, 0, 2), # Chainmail
    (53, 0, 3), # Splintmail
    (75, 0, 4), # Bandedmail
    (102, 0, 5), # Platemail
]

rings = [
    (0, 0, 0), # None
    (25, 1, 0), # Damage +1
    (50, 2, 0), # Damage +2
    (100, 3, 0), # Damage +3
    (20, 0, 1), # Defense +1
    (40, 0, 2), # Defense +2
    (80, 0, 3), # Defense +3
]

def does_player_win_fight(player_damage, player_armor):
    player_health = 100

    boss_health = boss_start_health

    turn = 0
    while player_health > 0 and boss_health > 0:
        if (turn % 2) == 0:
            # player attacks
            boss_health -= max(1, player_damage - boss_armor)
        else:
            # boss attacks
            player_health -= max(1, boss_damage - player_armor)
        turn += 1

    return player_health > 0

highest_cost_to_still_lose_against_boss = None

for equipment_selection in itertools.product(
    weapons,
    armor,
    itertools.combinations_with_replacement(rings, 2)
):
    # first off, technically combinations_with_replacement is only for the fact that you can select two "none"s for your rings
    # so let's just check that out the gate (cannot choose the same ring twice)
    weapon = equipment_selection[0]
    armor = equipment_selection[1]
    ring_one = equipment_selection[2][0]
    ring_two = equipment_selection[2][1]

    if ring_one == ring_two and ring_one[0] != 0:
        # shop only has one of each item, so this ring was selected twice, skip...
        continue

    equipment_cost = weapon[0] + armor[0] + ring_one[0] + ring_two[0]
    player_damage = weapon[1] + armor[1] + ring_one[1] + ring_two[1]
    player_armor = weapon[2] + armor[2] + ring_one[2] + ring_two[2]

    if highest_cost_to_still_lose_against_boss is None or \
        highest_cost_to_still_lose_against_boss < equipment_cost:
        if does_player_win_fight(player_damage, player_armor):
            continue
        highest_cost_to_still_lose_against_boss = equipment_cost

print(highest_cost_to_still_lose_against_boss)
