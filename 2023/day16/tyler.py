def part_one():
    file = open("inputs/tylerinput.txt")
    layout = [[char for char in line.removesuffix('\n')] for line in file]

    energy_map = [[False for _ in row] for row in layout]
    dir_history: list[list[list[tuple[int, int]]]] = [[[] for _ in row] for row in layout]
    beam_headers = [(0, 0, 1, 0)]
    while len(beam_headers) != 0:
        header = beam_headers.pop(0)

        if not (0 <= header[0] < len(layout[0])) or not (0 <= header[1] < len(layout)):
            continue  # Beam has hit a wall

        if (header[2], header[3]) in dir_history[header[1]][header[0]]:
            continue

        energy_map[header[1]][header[0]] = True
        dir_history[header[1]][header[0]].append((header[2], header[3]))

        char = layout[header[1]][header[0]]

        if char == '\\':
            beam_headers.append((header[0] + header[3], header[1] + header[2], header[3], header[2]))
            continue
        if char == '/':
            beam_headers.append((header[0] - header[3], header[1] - header[2], -header[3], -header[2]))
            continue
        if char == '|' and header[2] != 0:
            beam_headers.append((header[0], header[1] + 1, 0, 1))
            beam_headers.append((header[0], header[1] - 1, 0, -1))
            continue
        if char == '-' and header[3] != 0:
            beam_headers.append((header[0] + 1, header[1], 1, 0))
            beam_headers.append((header[0] - 1, header[1], -1, 0))
            continue

        beam_headers.append((header[0] + header[2], header[1] + header[3], header[2], header[3]))

    total = 0
    for row in energy_map:
        for energized in row:
            if energized:
                total += 1
    print(total)


def calculate_energy(layout: list[list[str]], initial_header: tuple[int, int, int, int]):
    energy_map = [[False for _ in row] for row in layout]
    dir_history: list[list[list[tuple[int, int]]]] = [[[] for _ in row] for row in layout]
    beam_headers = [initial_header]
    total = 0
    while len(beam_headers) != 0:
        header = beam_headers.pop(0)

        if not (0 <= header[0] < len(layout[0])) or not (0 <= header[1] < len(layout)):
            continue  # Beam has hit a wall

        if (header[2], header[3]) in dir_history[header[1]][header[0]]:
            continue  # We've been to this tile in this direction already, no need to redo it

        if not energy_map[header[1]][header[0]]:
            energy_map[header[1]][header[0]] = True
            total += 1

        # Save direction for history check to avoid infinite loops
        dir_history[header[1]][header[0]].append((header[2], header[3]))

        char = layout[header[1]][header[0]]

        if char == '\\':
            beam_headers.append((header[0] + header[3], header[1] + header[2], header[3], header[2]))
            continue
        if char == '/':
            beam_headers.append((header[0] - header[3], header[1] - header[2], -header[3], -header[2]))
            continue
        if char == '|' and header[2] != 0:
            beam_headers.append((header[0], header[1] + 1, 0, 1))
            beam_headers.append((header[0], header[1] - 1, 0, -1))
            continue
        if char == '-' and header[3] != 0:
            beam_headers.append((header[0] + 1, header[1], 1, 0))
            beam_headers.append((header[0] - 1, header[1], -1, 0))
            continue

        beam_headers.append((header[0] + header[2], header[1] + header[3], header[2], header[3]))

    return total


def part_two():
    file = open("inputs/tylerinput.txt")
    layout = [[char for char in line.removesuffix('\n')] for line in file]

    max_energy = 0

    edge_x = len(layout[0]) - 1
    for y in range(len(layout)):
        max_energy = max(max_energy, calculate_energy(layout, (0, y, 1, 0)))
        max_energy = max(max_energy, calculate_energy(layout, (edge_x, y, -1, 0)))

    edge_y = len(layout) - 1
    for x in range(len(layout[0])):
        max_energy = max(max_energy, calculate_energy(layout, (x, 0, 0, 1)))
        max_energy = max(max_energy, calculate_energy(layout, (x, edge_y, 0, -1)))

    print(max_energy)


if __name__ == "__main__":
    part_one()
    #part_two()
