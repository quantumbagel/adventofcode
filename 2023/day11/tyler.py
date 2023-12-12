def part_one():
    file = open("inputs/tylerinput.txt")

    expanded_universe = []
    for line in file:
        line = [_ for _ in line.removesuffix('\n')]
        expanded_universe.append(line)
        if '#' not in line:
            expanded_universe.append(line.copy())

    # Check columns
    i = 0
    while i < len(expanded_universe[0]):
        column = [line[i] for line in expanded_universe]
        if '#' not in column:
            for line in expanded_universe:
                line.insert(i, '.')
            i += 1
        i += 1

    galaxies = []
    for y, line in enumerate(expanded_universe):
        for x, char in enumerate(line):
            if char == '#':
                galaxies.append((x, y))

    total = 0
    for i, g1 in enumerate(galaxies):
        for j in range(i, len(galaxies)):
            g2 = galaxies[j]
            total += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])  # Taxicab distance
    print(total)


def part_two():
    file = open("inputs/tylerinput.txt")
    basic_universe = [[_ for _ in line.removesuffix('\n')] for line in file]

    expansion_const = 1000000

    # Use a distance maps to expand the space between galaxies
    # without expanding the universe array.
    distance_x = []
    distance_y = []
    for y, row in enumerate(basic_universe):
        if '#' not in row:
            distance_y.append(expansion_const)
        else:
            distance_y.append(1)

    for x in range(len(basic_universe[0])):
        column = [row[x] for row in basic_universe]
        if '#' not in column:
            distance_x.append(expansion_const)
        else:
            distance_x.append(1)

    # Find all galaxies. Search through the basic universe
    # to find the index pos of the galaxies, but use the distance map to
    # find where they are actually located in space.
    galaxies = []
    y = 0
    for j, row in enumerate(basic_universe):
        x = 0
        for i, char in enumerate(row):
            if char == '#':
                galaxies.append((x, y))
            x += distance_x[i]
        y += distance_y[j]

    total = 0
    for i, g1 in enumerate(galaxies):
        for j in range(i, len(galaxies)):
            g2 = galaxies[j]
            total += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])  # Taxicab distance
    print(total)


if __name__ == "__main__":
    # part_one()
    part_two()
