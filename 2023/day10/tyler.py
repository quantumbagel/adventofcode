# Turns are organized so that if you leave out the first connect,
# you're moving clockwise, and counter-clockwise otherwise
pipe_connections = {
    '|': [(0, -1), (0, 1)],
    '-': [(-1, 0), (1, 0)],
    'L': [(0, -1), (1, 0)],
    'J': [(-1, 0), (0, -1)],
    '7': [(0, 1), (-1, 0)],
    'F': [(1, 0), (0, 1)],
    '.': [],
}

def part_one():
    file = open("inputs/tylerinput.txt")
    file_lines = [line.removesuffix('\n') for line in file]

    # Find starting tile
    start_x, start_y = 0, 0
    for i, line in enumerate(file_lines):
        if 'S' in line:
            start_x = line.index('S')
            start_y = i
            break

    # Find left and right exits from the starting tile.
    # They don't have to be true left and right; the point
    # is that they go in opposite directions around the loop
    left = []
    right = []
    for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        check_x = start_x + i
        check_y = start_y + j
        if check_x < 0 or check_y < 0 or check_x >= len(file_lines[0]) or check_y >= len(file_lines):
            continue
        char = file_lines[check_y][check_x]
        if (-i, -j) in pipe_connections[char]:
            if len(left) == 0:
                left = [check_x, check_y]
            else:
                right = [check_x, check_y]
                break

    # Move the left and right sentries around the loop until they meet.
    # Record the distance they travel.
    dist = 1

    # Use these variables to tell which direction the sentries came from
    left_coming = [start_x - left[0], start_y - left[1]]
    right_coming = [start_x - right[0], start_y - right[1]]

    while left[0] != right[0] or left[1] != right[1]:
        left_char = file_lines[left[1]][left[0]]
        right_char = file_lines[right[1]][right[0]]

        # Find the outgoing connection and move the left sentry
        for connection in pipe_connections[left_char]:
            if connection[0] != left_coming[0] or connection[1] != left_coming[1]:
                left[0] += connection[0]
                left[1] += connection[1]
                left_coming[0] = -connection[0]
                left_coming[1] = -connection[1]
                break

        # If the left has found the right, we're done, no more need to increase distance.
        # Loop must have odd length.
        if left[0] == right[0] and left[1] == right[1]:
            break

        # Find the outgoing connection and move the right sentry
        for connection in pipe_connections[right_char]:
            if connection[0] != right_coming[0] or connection[1] != right_coming[1]:
                right[0] += connection[0]
                right[1] += connection[1]
                right_coming[0] = -connection[0]
                right_coming[1] = -connection[1]
                break

        dist += 1  # Increment distance counter

    print(dist)


# Helper function for part two
def get_sides(path, clockwise_default):
    """
    Returns two offsets, one to the left/right of the path, and
    another directly in front of that.

    :param path: the path
    :param clockwise_default: whether this loop has a clockwise default
    :return: list of side offsets from the path
    """
    if clockwise_default:
        return [(-path[1], path[0]), (-path[1] + path[0], path[0] + path[1])]
    return [(path[1], -path[0]), (path[1] + path[0], -path[0] + path[1])]


def part_two():
    file = open("inputs/tylerinput.txt")
    file_lines = [line.removesuffix('\n') for line in file]

    # STEP 1: Find the start tile
    start_x, start_y = 0, 0
    for i, line in enumerate(file_lines):
        if 'S' in line:
            start_x = line.index('S')
            start_y = i
            break

    # STEP 2: Find a pipe leading out of the start
    current = []
    for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        check_x = start_x + i
        check_y = start_y + j
        if check_x < 0 or check_y < 0 or check_x >= len(file_lines[0]) or check_y >= len(file_lines):
            continue
        char = file_lines[check_y][check_x]
        if (-i, -j) in pipe_connections[char]:
            current = [check_x, check_y]
            break

    # Create a simplified grid that removes everything but the main loop
    simplified_grid = [['.' for _ in line] for line in file_lines]
    simplified_grid[start_y][start_x] = 'S'

    # STEP 3: Find the main loop
    # Create a variable to check against so we know which way we came from
    coming_from = [start_x - current[0], start_y - current[1]]

    # Use this variable to determine if our path through the loop has a
    # clockwise or counter-clockwise default. This will then be used
    # to determine which side of the loop (left or right) is the inside.
    turn_default = 0

    # Keep track of a simplified path for the next time we traverse the loop
    path = [(-coming_from[0], -coming_from[1])]
    while current[0] != start_x or current[1] != start_y:
        char = file_lines[current[1]][current[0]]

        # Add character to simplified grid
        simplified_grid[current[1]][current[0]] = char

        # Check the sentry connections
        for con_num, connection in enumerate(pipe_connections[char]):
            if connection[0] != coming_from[0] or connection[1] != coming_from[1]:
                # If this is a turn
                if char not in "|-":
                    if con_num == 0:
                        turn_default -= 1  # clockwise turn
                    else:
                        turn_default += 1  # counter-clockwise turn

                # Move the sentry
                current[0] += connection[0]
                current[1] += connection[1]
                # Update where we came from
                coming_from[0] = -connection[0]
                coming_from[1] = -connection[1]
                # Add connection to the path
                path.append((connection[0], connection[1]))
                break

    # STEP 4: Move along the loop, adding flagging any
    # empty spaces inside the loop
    flagged = []
    current = [start_x, start_y]
    clockwise_default = turn_default < 0
    for p in path:
        # This function gets the inside parts of the loop to flag
        sides = get_sides(p, clockwise_default)

        for offset in sides:
            to_check = current[0] + offset[0], current[1] + offset[1]

            # Ensure that the candidate is inside the bounds of the grid
            if to_check[0] < 0 or to_check[1] < 0 or\
                    to_check[0] >= len(simplified_grid[0]) or to_check[1] >= len(simplified_grid):
                continue

            char = simplified_grid[to_check[1]][to_check[0]]
            if char == '.' and to_check not in flagged:
                flagged.append(to_check)

        # Move the sentry along the path
        current[0] += p[0]
        current[1] += p[1]

    # STEP 5: Flood-fill algorithm to find all other enclosed areas.
    enclosed = []
    while len(flagged) != 0:
        to_check = flagged.pop(0)

        if to_check[0] < 0 or to_check[1] < 0 or\
                to_check[0] >= len(simplified_grid[0]) or to_check[1] >= len(simplified_grid):
            continue
        char = simplified_grid[to_check[1]][to_check[0]]
        if char != '.':
            continue
        if to_check in enclosed:
            continue

        enclosed.append(to_check)
        simplified_grid[to_check[1]][to_check[0]] = 'A'  # Visual/Debugging purposes only ('I' was hard to see)
        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            flagged.append((to_check[0] + i, to_check[1] + j))

    area = len(enclosed)
    print(area)


if __name__ == "__main__":
    # part_one()
    part_two()
