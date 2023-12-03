neighbors = [(1, 1), (0, 1), (-1, 1), (1, 0), (-1, 0), (1, -1), (0, -1), (-1, -1)]

def process_number_forward(lines: list[str], row: int, column: int) -> (int, int):
    """
    Looks at the list of lines starting at the given coordinates and attempts
    to read the integer stored there. If a non-period non-digit symbol is
    found adjacent to any of the digits in the number, then we return that number.
    Otherwise, we return 0. The second component of the return is the length of the
    processed number, which is used to skip part it in the main loop.

    :param lines: the list of lines
    :param row: the starting row
    :param column: the starting column
    :return: the part number beginning at the coords, and the length of that number
    """
    x = column
    num = 0
    found_symbol = False
    while x < len(lines[row]) and lines[row][x].isdigit():
        # check for the symbol if we haven't found it yet
        if not found_symbol:
            for transformation in neighbors:
                # Use the transformation to shift where we check for the symbol.
                # Restrain the coordinates so that they don't go outside the bounds
                check_row = min(max(0, row + transformation[0]), len(lines) - 1)
                check_column = min(max(0, x + transformation[1]), len(lines[row]) - 1)
                check_char = lines[check_row][check_column]
                # If we find the symbol, record it and break out early
                if not (check_char.isdigit() or check_char == '.'):
                    found_symbol = True
                    break

        num = 10 * num + int(lines[row][x])
        x += 1

    # If we didn't find a symbol, just clear the number
    if not found_symbol:
        num = 0
    return num, x - column


def process_gear_part(lines: list[str], row: int, column: int) -> (int, int):
    """
    Looks for and returns an integer with one of its characters stored at
    the given coordinates. Looks both forwards and backwards in the line,
    stopping at either a non-digit or the end of a line.\n\n
    Also gives the column of the first digit in the number.

    :param lines: the list of lines
    :param row: the starting row
    :param column: the starting column
    :return: the number stored at given coordinates, and the column of the first digit
    """
    digits = lines[row][column]  # Use it as a string to help with flexible concatenation

    # start by moving to the left of the starting coords
    left = column - 1
    while left >= 0 and lines[row][left].isdigit():
        digits = lines[row][left] + digits  # Add new digits at front of number
        left -= 1

    # now we move to the right of the starting coords
    right = column + 1
    while right < len(lines[row]) and lines[row][right].isdigit():
        digits = digits + lines[row][right]  # Add new digits at back of number
        right += 1

    return int(digits), left + 1


def part_one():
    file = open("inputs/tylerinput.txt")
    file_lines = [i.removesuffix('\n') for i in file.readlines()]

    sum = 0
    # Loop over every line, keeping track of the row number
    for row, line in enumerate(file_lines):
        # Loop over every character in the line, keeping track of the column number
        column = 0
        while column < len(line):
            # If this character isn't a digit, move to next one
            if not line[column].isdigit():
                column += 1
                continue

            # Process the number starting at the current column
            num, skip = process_number_forward(file_lines, row, column)

            sum += num  # Add the sum to the final result
            column += skip  # skip ahead to the end of the number
    print(sum)


def part_two():
    file = open("inputs/tylerinput.txt")
    file_lines = [i.removesuffix('\n') for i in file.readlines()]

    sum = 0
    # Loop over every line, keeping track of the row number
    for row, line in enumerate(file_lines):
        for column, char in enumerate(line):
            # If this character isn't a gear, we skip through
            if char != '*':
                continue

            gear_ratio = 1  # Store the gear ratio
            used_parts = []  # Create a list to tell if we've already counted a part
            for transformation in neighbors:
                # Use the transformation to shift where we check for the digits.
                # Restrain the coordinates so that they don't go outside the bounds
                check_row = min(max(0, row + transformation[0]), len(file_lines) - 1)
                check_column = min(max(0, column + transformation[1]), len(file_lines[row]) - 1)
                if file_lines[check_row][check_column].isdigit():
                    num, first_column = process_gear_part(file_lines, check_row, check_column)
                    if (check_row, first_column) not in used_parts:
                        gear_ratio *= num
                        used_parts.append((check_row, first_column))

            if len(used_parts) == 2:  # If this is an actual gear
                sum += gear_ratio  # Add the sum to the final result
    print(sum)


if __name__ == "__main__":
    # part_one()
    part_two()
