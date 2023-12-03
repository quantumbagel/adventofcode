x = open('inputs/quantumbagelinput.txt')
lines = [i.replace('\n', '') for i in x.readlines()]
numbers = "0123456789"


def check_surrounding(row, col):
    transform = [[0, -1], [0, 1], [1, 0], [-1, 0], [-1, 1], [1, -1], [1, 1], [-1, -1]]
    for transformation in transform:
        new_col = col + transformation[1]
        new_row = row + transformation[0]
        if not (new_col < 0 or new_row < 0 or new_row >= len(lines[0]) or new_col >= len(lines)):
            if lines[new_col][new_row] not in numbers and lines[new_col][new_row] != ".":
                return True
    return False


sum_of_numbers = 0
for c, line in enumerate(lines):
    current_number = ""
    current_pos = []
    for r, string_char in enumerate(line):
        if string_char in numbers:
            current_number += string_char
            current_pos.append([c, r])
        if (not (string_char in numbers) and current_number) or r == len(line) - 1:
            for pos in current_pos:
                if check_surrounding(pos[1], pos[0]):
                    sum_of_numbers += int(current_number)
                    break
            current_number = ""
            current_pos = []
print(sum_of_numbers)
