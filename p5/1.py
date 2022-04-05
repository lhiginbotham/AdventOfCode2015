inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

banned_pairs = [ 'ab', 'cd', 'pq', 'xy' ]
banned_starts = [ x[0] for x in banned_pairs ]
banned_ends = [ x[1] for x in banned_pairs ]
vowels = 'aeiou'

def is_nice(name: str) -> bool:
    prevC = None
    containsDouble = False
    vowelCount = 0

    for c in name:
        if prevC is not None and prevC == c:
            containsDouble = True

        if prevC is not None and prevC in banned_starts and c == banned_ends[banned_starts.index(prevC)]:
            return False

        if c in vowels:
            vowelCount += 1

        prevC = c

    return vowelCount >= 3 and containsDouble

number_nice_strings = 0
for x in inp:
    if is_nice(x):
        number_nice_strings += 1

print(number_nice_strings)
