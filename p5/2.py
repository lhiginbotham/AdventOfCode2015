inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

banned_pairs = [ 'ab', 'cd', 'pq', 'xy' ]
banned_starts = [ x[0] for x in banned_pairs ]
banned_ends = [ x[1] for x in banned_pairs ]
vowels = 'aeiou'

# returns true if you have some letter = S and anything else = A, 'SAS' in string
def _contains_sandwich(string: str) -> bool:
    if len(string) < 3:
        return False

    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True

    return False

def _contains_doubled_pair(string: str) -> bool:
    if len(string) < 4:
        return False

    for i in range(len(string) - 3):
        for j in range(i + 2, len(string) - 1):
            if string[i:i+2] == string[j:j+2]:
                return True

    return False

def is_nice(name: str) -> bool:
    return _contains_sandwich(name) and _contains_doubled_pair(name)

number_nice_strings = 0
for x in inp:
    if is_nice(x):
        number_nice_strings += 1

print(number_nice_strings)
