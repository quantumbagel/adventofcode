def part_one():
    file = open("inputs/tylerinput.txt")

    total = 0
    for line in file:
        line = line.removesuffix('\n')
        where_is_colon = line.index(':')
        line = line[where_is_colon+2:]  # Trim away colon

        winning_numbers = line.split('|')[0]
        our_numbers = line.split('|')[1]

        # Split each string into a list of digit strings
        winning_numbers = winning_numbers.split()
        our_numbers = our_numbers.split()

        # Count the number of matching numbers
        matches = 0
        for num in our_numbers:
            if num in winning_numbers:
                matches += 1

        # Add the point value using exponential math
        if matches > 0:
            total += 2 ** (matches - 1)
    print(total)


def part_two():
    file = open("inputs/tylerinput.txt")
    file_lines = [line.removesuffix('\n') for line in file]

    num_copies_by_id = [1 for line in file_lines]  # Initialize list with 1 copy of each card

    for i, line in enumerate(file_lines):
        line = line.removesuffix('\n')
        where_is_colon = line.index(':')
        line = line[where_is_colon + 2:]  # Trim away colon

        winning_numbers = line.split('|')[0]
        our_numbers = line.split('|')[1]

        # Split each string into a list of digit strings
        winning_numbers = winning_numbers.split()
        our_numbers = our_numbers.split()

        # Count the number of matching numbers
        matches = 0
        for num in our_numbers:
            if num in winning_numbers:
                matches += 1

        for j in range(i + 1, i + 1 + matches):
            if j < len(num_copies_by_id):  # Don't make copies of cards that don't exist
                # Each copy of the current card is gonna have the same matches,
                # so they will all create one copy of the next cards. We can
                # save on time by just adding the number of copies of this
                # card to the number of copies of the next cards.
                num_copies_by_id[j] += num_copies_by_id[i]

    print(sum(num_copies_by_id))


if __name__ == "__main__":
    # part_one()
    part_two()
