import copy
import sys
transformation = {"|": {"R": ["U", "D"], "L": ["U", "D"], "U": ["U"], "D": ["D"]},
                  "-": {"R": ["R"], "L": ["L"], "U": ["L", "R"], "D": ["L", "R"]},
                  ".": {"R": ["R"], "L": ["L"], "U": ["U"], "D": ["D"]},
                  "/": {"R": ["U"], "L": ["D"], "U": ["R"], "D": ["L"]},
                  "\\": {"R": ["D"], "L": ["U"], "U": ["L"], "D": ["R"]}}

direction_to_movement = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}


board = [[{i: False} for i in line if i != '\n'] for line in open('inputs/quantumbagelinput.txt')]



def print_map(m):
    string_to_print = ""
    for line in m:
        for dic in line:
            if list(dic.values())[0]:
                string_to_print += "#"
            else:
                string_to_print += list(dic.keys())[0]
        string_to_print += '\n'
    print(string_to_print)


def score_map(m):
    energized = 0
    for line in m:
        for dic in line:
            if list(dic.values())[0]:
                energized += 1
    return energized


def part_1(b, start_track):
    b = copy.deepcopy(b)  # Ensure copy
    tracking = start_track[:]  # The current positions and directions of the beam of light
    tracking_cache = []  # Cache of past positions
    while True:
        next_iteration_tracker = []
        should_continue = False
        for coord in tracking:
            if coord not in tracking_cache:  # If we haven't been here
                tracking_cache.append(coord)  # Now we have
                should_continue = True
            else:  # just keep on fruiting
                continue
            direction = coord[-1]
            coord = (int(coord[:-1].split(',')[0]), int(coord[:-1].split(',')[1]))
            character = list(b[coord[1]][coord[0]].keys())[0]  # Get the character of the current position
            b[coord[1]][coord[0]][character] = True  # "Energize" the square
            new_directions = transformation[character][direction]  # The direction (or directions) the beam goes from here
            for new_direction in new_directions:

                # Retrieve the transformation
                direction_transform = direction_to_movement[new_direction]

                # Get the updated x and y coordinates
                new_x = coord[0] + direction_transform[0]
                new_y = coord[1] + direction_transform[1]

                # If this position would be invalid
                if new_x < 0 or new_y < 0 or new_x >= len(b[0]) or new_y >= len(b):
                    continue  # Just go to the next one
                next_iteration_tracker.append(str(new_x) + "," + str(new_y) + new_direction)
        if not should_continue:
            break
        tracking = next_iteration_tracker  # Prepare for next iteration
    return score_map(b)


def part_2():
    max_score = 0
    for index, bottom in enumerate(range(len(board[0]))):
        print(index+1, len(board[0])-1, "B")
        score = part_1(board, [f"{bottom},{len(board[0])-1}U"])
        if score > max_score:
            print("PR", score)
            max_score = score
    for index, top in enumerate(range(len(board[0]))):
        print(index+1, len(board[0])-1, "T")
        score = part_1(board, [f"{top},0D"])
        if score > max_score:
            print("PR", score)
            max_score = score
    for index, left in enumerate(range(len(board))):
        print(index+1, len(board[0])-1, "L")
        score = part_1(board, [f"0,{left}R"])
        if score > max_score:
            print("PR", score)
            max_score = score
    for index, right in enumerate(range(len(board))):
        print(index+1, len(board[0])-1, "R")
        score = part_1(board, [f"{len(board)-1},{right}L"])
        if score > max_score:
            print("PR", score)
            max_score = score
    return max_score

print(part_2())
