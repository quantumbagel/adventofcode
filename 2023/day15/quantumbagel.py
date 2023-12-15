def score_string(calibration_value):
    current_value = 0
    for char in calibration_value:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def part_1():
    # Parse input
    calibration_values = open("inputs/quantumbagelinput.txt").readlines()[0].replace('\n', '').split(",")
    # Score input
    print(sum([score_string(c_value) for c_value in calibration_values]))


def part_2():
    boxes = {}
    # Parse input
    instructions = open("inputs/quantumbagelinput.txt").readlines()[0].replace('\n', '').split(",")
    # Filling boxes
    for instruction in instructions:
        if instruction[-1] == '-':  # This is a "subtract" op
            remove_me = -1
            box = score_string(instruction.split('-')[0])
            try:
                for index, valid_box in enumerate(boxes[box]):  # For every box in the box that this lens *should* be in
                    if valid_box[0] == instruction.removesuffix('-'):  # If it's there
                        remove_me = index  # Mark for removal
                        break
            except KeyError:
                continue
            if remove_me != -1:  # If we need to remove something
                boxes[box].pop(remove_me)  # Do so
                if not boxes[box]:
                    del boxes[box]  # Clean up
        else:  # This is a "set" op
            box = score_string(instruction.split('=')[0])
            number = int(instruction.split('=')[1])
            identification = instruction.split('=')[0]
            valid_id = -1
            try:
                for index, lens in enumerate(boxes[box]):  # For every lens
                    if lens[0] == identification:  # If it exists, save the index
                        valid_id = index
                        break
            except KeyError:
                pass  # We want the code to continue here
            if valid_id == -1:  # If we don't know the index
                try:
                    boxes[box].append([identification, number])  # Just add to the end
                except KeyError:
                    boxes[box] = [[identification, number]]  # Update existing entry
            else:
                boxes[box][valid_id][1] = number  # Update the focal length (we know)

    # Scoring
    score = 0
    for box in boxes:
        for slot, lens in enumerate(boxes[box]):
            score += (box + 1) * (slot + 1) * lens[1]
    print(score)


part_2()

