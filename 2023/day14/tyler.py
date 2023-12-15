import time


def part_one():
    file = open("inputs/tylerinput.txt")
    file_lines = [row.removesuffix('\n') for row in file]

    load = 0
    for c in range(len(file_lines[0])):
        rounds = 0
        recent_square_idx = -1
        for r, line in enumerate(file_lines):
            char = line[c]
            if char == '#':
                load_offset = len(file_lines) - recent_square_idx - rounds
                load += (rounds * (rounds - 1)) // 2 + rounds * load_offset
                recent_square_idx = r
                rounds = 0
                continue
            if char == 'O':
                rounds += 1
                continue

        if rounds != 0:
            load_offset = len(file_lines) - recent_square_idx - rounds
            load += (rounds * (rounds - 1)) // 2 + rounds * load_offset

    print(load)


def north(rows: list[str]) -> list[str]:
    for c in range(len(rows[0])):
        rounds = 0
        recent_square_idx = -1
        for r, row in enumerate(rows):
            char = row[c]
            if char == '#':
                # Move rocks
                for i in range(rounds):
                    target = rows[recent_square_idx + i + 1]
                    rows[recent_square_idx + i + 1] = target[:c] + 'O' + target[c + 1:]
                recent_square_idx = r
                rounds = 0
                continue
            if char == 'O':
                rows[r] = row[:c] + '.' + row[c + 1:]
                rounds += 1
                continue

        if rounds != 0:
            # Move rocks
            for i in range(rounds):
                target = rows[i + recent_square_idx + 1]
                rows[i + recent_square_idx + 1] = target[:c] + 'O' + target[c + 1:]
    return rows


def south(rows: list[str]) -> list[str]:
    rows.reverse()
    rows = north(rows)
    rows.reverse()
    return rows


def west(rows: list[str]) -> list[str]:
    columns = [''.join([row[i] for row in rows]) for i in range(len(rows[0]))]
    columns = north(columns)
    return [''.join([column[i] for column in columns]) for i in range(len(columns[0]))]


def east(rows: list[str]) -> list[str]:
    columns = [''.join([row[i] for row in rows]) for i in reversed(range(len(rows[0])))]
    columns = north(columns)
    return [''.join([column[i] for column in reversed(columns)]) for i in range(len(columns[0]))]


def cycle(rows: list[str], num_cycles: int, cache={}) -> list[str]:
    cycled = rows.copy()
    i = 0
    while i < num_cycles:
        key = ''.join(cycled)
        if key in cache:
            # We've found a loop, skip until we can't fit the loop anymore
            i = num_cycles - (num_cycles - i) % (i - cache[key])
            cache = {}  # clear the cache
            continue
        cache[key] = i

        cycled = north(cycled)
        cycled = west(cycled)
        cycled = south(cycled)
        cycled = east(cycled)
        i += 1
    return cycled


def part_two():
    file = open("inputs/tylerinput.txt")
    file_lines = [row.removesuffix('\n') for row in file]
    cycled = cycle(file_lines, 1000000000)

    # Calculate load
    load = 0
    for r, row in enumerate(cycled):
        for char in row:
            if char == 'O':
                load += len(cycled) - r
    print(load)


if __name__ == "__main__":
    start_time = time.time()
    # part_one()
    part_two()
    print(str(time.time() - start_time) + " s")
