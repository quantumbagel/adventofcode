import pprint


def part_1():
    lines = open('input.txt').readlines()
    the_map = []
    start_pos = ()
    for column, line in enumerate(lines):
        line = line.replace('\n', '')
        temp = [[character, 0] for character in line]
        for index, item in enumerate(temp):
            if item[0] == "S":
                start_pos = (index, column)
                break
        the_map.append(temp)

    transform_letters = {"J": [[-1, 0], [0, -1]],
                         "L": [[1, 0], [0, -1]],
                         "F": [[1, 0], [0, 1]],
                         "7": [[-1, 0], [0, 1]],
                         "|": [[0, 1], [0, -1]],
                         "-": [[-1, 0], [1, 0]],
                         ".": [],
                         "S": [[-1, 0], [1, 0], [0, 1], [0, -1]]}

    def get_valid_neighbors(check_map, row, column):
        neighbors = []
        for transformation in transform_letters[check_map[column][row][0]]:
            new_row = row + transformation[0]
            new_column = column + transformation[1]
            if new_column < 0 or new_column >= len(check_map) or new_row < 0 or new_row >= len(check_map[0]):
                continue
            if check_map[new_column][new_row][0] == '.':
                continue
            neighbors.append((new_row, new_column))
        return neighbors


    last_position = start_pos[:]
    current_position = get_valid_neighbors(the_map, start_pos[0], start_pos[1])[0]
    dist = 1
    while True:
        the_map[current_position[1]][current_position[0]][1] = dist
        neighbors = get_valid_neighbors(the_map, current_position[0], current_position[1])
        for item in neighbors:
            if item != last_position:
                last_position = current_position[:]
                current_position = item
                break
        if current_position == start_pos:
            break
        dist += 1
    print("Part 1 answer:")
    if dist % 2 == 1:
        print((dist+1)//2)
    else:
        print((dist+1)//2 + 1)
    return the_map
def part_2():
    the_map = part_1()
    import pprint
    pprint.pprint(the_map)
    for line in the_map:
        inside = False
        l_in = False
        for our_index, cell in enumerate(line):
            if cell[1] or cell[0] == "S":  # in thing
                if not l_in:
                    inside = not inside
                    l_in = True
            else:
                l_in = False
            if inside:
                for item in line:
                    de
            print(cell, inside)



part_2()