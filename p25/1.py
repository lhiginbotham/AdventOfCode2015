# Puzzle Input:
#     To continue, please consult the code grid in the manual.  Enter the code at row 3010, column 3019.

from collections import defaultdict

answer_code_loc = (3010, 3019)

codes = defaultdict(lambda: None)
codes[0] = 20151125

def get_linearized_index(row, col):
    orig_col = col

    # get diagonal number that this belongs to
    while col > 1:
        col -= 1
        row += 1
    diagonal_number = row

    # base index is the sum of the numbers up to the diagonal number, as the diagonal contains diagonal_number elements
    base_index = (row * (row - 1)) // 2
    return base_index + orig_col - 1

def calc_code(prev_val):
    return (prev_val * 252533) % 33554393

def get_code_for(codes, row, col):
    idx = get_linearized_index(row, col)
    for i in range(1, idx + 1):
        if codes[i] is None:
            codes[i] = calc_code(codes[i - 1])
    return codes[idx]

print(get_code_for(codes, answer_code_loc[0], answer_code_loc[1]))
