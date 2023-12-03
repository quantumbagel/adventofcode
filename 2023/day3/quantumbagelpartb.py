x = open('inputs/quantumbagelinput.txt')
lines = [i.replace('\n', '') for i in x.readlines()]
numbers = "0123456789"


def check_surrounding(row, col):
    transform = [[0, -1], [0, 1], [1, 0], [-1, 0], [-1, 1], [1, -1], [1, 1], [-1, -1]]
    for transformation in transform:
        new_col = col + transformation[1]
        new_row = row + transformation[0]
        if not (new_col < 0 or new_row < 0 or new_row >= len(lines[0]) or new_col >= len(lines)):
            if lines[new_col][new_row] == "*":
                return new_col, new_row
    return -1, -1


pos_dict = {}
gear_tracker = {}
gear_nums = {}
for c, line in enumerate(lines):
    current_number = ""
    current_pos = []
    for r, string_char in enumerate(line):
        if string_char in numbers:
            current_number += string_char
            current_pos.append([c, r])
        if (not (string_char in numbers) and current_number) or r == len(line) - 1:
            for pos in current_pos:
                out = check_surrounding(pos[1], pos[0])
                if out[0] != -1 and out[1] != -1:
                    if [out[0], out[1]] in pos_dict.values():
                        key_val = list(pos_dict.keys())[list(pos_dict.values()).index([out[0], out[1]])]
                        gear_tracker[key_val] += 1
                        gear_nums[key_val].append(int(current_number))
                    else:
                         key_val = len(pos_dict.keys())
                         pos_dict.update({key_val: [out[0], out[1]]})
                         gear_tracker.update({key_val: 1})
                         gear_nums.update({key_val: [int(current_number)]})
                    break
            current_number = ""
            current_pos = []
total_gear_sum = 0
for gear in gear_tracker.keys():
    if gear_tracker[gear] == 2:
        total_gear_sum += gear_nums[gear][0] * gear_nums[gear][1]
print(total_gear_sum)
