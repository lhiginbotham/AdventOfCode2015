inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

current_looksay_string = inp[0]

def do_looksay(string):
    new_string = ""
    curr_c = None
    num = 0

    for c in string:
        if curr_c != c:
            if curr_c is not None:
                new_string += str(num) + curr_c
            curr_c = c
            num = 1
        else:
            num += 1

    new_string += str(num) + curr_c
    return new_string

for i in range(40):
    current_looksay_string = do_looksay(current_looksay_string)

print(len(current_looksay_string))
