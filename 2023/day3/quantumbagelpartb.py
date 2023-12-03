x = open('inputs/quantumbagelinput.txt')
lines = [i.replace('\n', '') for i in x.readlines()]
numbers = "0123456789"


def check_surrounding(row, col):
    """
    Check if there is a gear around the position (col, row)
    :param row: the row
    :param col: the column
    :return: the position of the gear, or [-1, -1] otherwise
    """
    transform = [[0, -1], [0, 1], [1, 0], [-1, 0], [-1, 1], [1, -1], [1, 1], [-1, -1]]  # all possible transformations
    for transformation in transform:
        new_col = col + transformation[1]  # calculate prediction
        new_row = row + transformation[0]
        if not (new_col < 0 or new_row < 0 or new_row >= len(lines[0]) or new_col >= len(lines)):  # not out of bounds?
            if lines[new_col][new_row] == "*":  # is the symbol a gear?
                return new_col, new_row  # return the position of the gear
    return -1, -1  # no gear, return default


pos_dict = {}
gear_tracker = {}
gear_nums = {}
for c, line in enumerate(lines):
    current_number = ""  # tracker of current number and position
    current_pos = []
    for r, string_char in enumerate(line):
        if string_char in numbers:
            current_number += string_char  # add to current_number
            current_pos.append([c, r])  # add position of number
        if (not (string_char in numbers) and current_number) or r == len(line) - 1:  # is the number finished?
            for pos in current_pos:  # check every position
                out = check_surrounding(pos[1], pos[0])  # get position of gear
                if out[0] != -1 and out[1] != -1:  # if there IS a gear
                    if [out[0], out[1]] in pos_dict.values():  # we have observed this gear before
                        # Calculate what the ID of the gear is
                        key_val = list(pos_dict.keys())[list(pos_dict.values()).index([out[0], out[1]])]
                        # Update the amount of times this gear has been observed
                        gear_tracker[key_val] += 1
                        # Add the number to the numbers attached to the gear
                        gear_nums[key_val].append(int(current_number))
                    else:  # new gear!
                        # Get the new ID of the gear
                        key_val = len(pos_dict.keys())
                        # Create base variables
                        pos_dict.update({key_val: [out[0], out[1]]})
                        gear_tracker.update({key_val: 1})
                        gear_nums.update({key_val: [int(current_number)]})
                    break
            # Reset the number and position
            current_number = ""
            current_pos = []

total_gear_sum = 0
for gear in gear_tracker.keys():
    if gear_tracker[gear] == 2:  # If there are two numbers connected to this gear
        total_gear_sum += gear_nums[gear][0] * gear_nums[gear][1] # Add the multiplication of these two gears
print(total_gear_sum)
