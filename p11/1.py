inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

def password_matches_rules(password):
    for c in 'iol':
        if c in password:
            return False

    containsSequence = False
    for i in range(len(password) - 2):
        one = password[i]
        two = password[i + 1]
        three = password[i + 2]
        if one == chr(ord(two) - 1) and two == chr(ord(three) - 1):
            containsSequence = True

    numDoubledPairs = 0
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            numDoubledPairs += 1
            i += 1
        i += 1

    return containsSequence and numDoubledPairs >= 2

def increment_password(password):
    password = [ x for x in password ]
    curr_c_index = len(password) - 1

    while True:
        if password[curr_c_index] == 'z':
            password[curr_c_index] = 'a'
            curr_c_index -= 1
            continue
        else:
            curr_c = password[curr_c_index]
            password[curr_c_index] = chr(ord(curr_c) + 1)
            break

    return ''.join(password)

old_password = inp[0]
new_password = old_password
while not password_matches_rules(new_password):
    new_password = increment_password(new_password)

print(new_password)
