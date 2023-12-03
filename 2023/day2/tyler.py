def part_one():
    file = open("inputs/tylerinput.txt")

    sum = 0
    for id, line in enumerate(file.readlines()):
        line = line.removesuffix('\n')
        where_is_colon = line.index(':')
        line = line[where_is_colon + 2:]

        color_limits = {"red": 12, "green": 13, "blue": 14}  # from the problem
        valid_game = True
        for round in line.split(';'):
            for sample in round.split(','):
                color = sample.split()[1]
                count = int(sample.split()[0])

                # If one of the counts is too high for that color, invalidate the game
                if count > color_limits[color]:
                    valid_game = False
                    break

            # No need to look at the other rounds if we already found an invalid one
            if not valid_game:
                break

        # Skip this line if the game isn't valid
        if not valid_game:
            continue
        sum += id + 1
    print(sum)

def part_two():
    file = open("inputs/tylerinput.txt")

    sum = 0
    for id, line in enumerate(file.readlines()):
        line = line.removesuffix('\n')
        where_is_colon = line.index(':')
        line = line[where_is_colon + 2:]

        highest_count = {"red": 0, "green": 0, "blue": 0}
        for round in line.split(';'):
            for sample in round.split(','):
                color = sample.split()[1]
                count = int(sample.split()[0])

                # If the count is higher than the highest so far, update the highest
                if count > highest_count[color]:
                    highest_count[color] = count

        # Multiply all the colors together
        power = 1
        for color in highest_count:
            power *= highest_count[color]

        # Add power to final sum
        sum += power
    print(sum)


if __name__ == "__main__":
    # part_one()
    part_two()
