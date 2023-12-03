x = open('inputs/quantumbagelinput.txt')
lines = [i.replace('\n', '') for i in x.readlines()]

numbers = "0123456789"


def check_surrounding(col: int, row: int) -> bool:
    """
    Check if there is a symbol surrounding the position (row, col)
    :param col: the column
    :param row: the row
    :return: boolean
    """
    transform = [[0, -1], [0, 1], [1, 0], [-1, 0], [-1, 1], [1, -1], [1, 1], [-1, -1]]
    # all possible transformations that exist from a square
    for transformation in transform: # check each position around the square
        new_col = col + transformation[1]  # Create the position to check (row and col)
        new_row = row + transformation[0]
        if not (new_col < 0 or new_row < 0 or new_row >= len(lines[0]) or new_col >= len(lines)):
            # check if the position is off the edge
            if lines[new_col][new_row] not in numbers and lines[new_col][new_row] != ".":  # is the char a symbol?
                return True
    return False  # we haven't found a symbol, so return false


sum_of_numbers = 0
for c, line in enumerate(lines):
    current_number = ""
    current_pos = []  # the positions the number occupies
    for r, string_char in enumerate(line):
        if string_char in numbers:  # if the char is a number
            current_number += string_char  # add it
            current_pos.append([c, r])  # add its position
        if (not (string_char in numbers) and current_number) or r == len(line) - 1:
            # three things
            # 1. the char is not a number AND
            # 2. current_number is not empty
            # 3. OR we are at the end, so we should check the aggregated number anyway
            for pos in current_pos:  # go through each position
                if check_surrounding(pos[0], pos[1]):  # does it have a symbol?
                    sum_of_numbers += int(current_number)  # add the number to the sum
                    break  # don't double count, go to the next char
            current_number = ""  # don't forget, reset current_number and current_pos
            current_pos = []
print(sum_of_numbers)
