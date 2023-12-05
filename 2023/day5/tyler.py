import math


def access_map(maps: dict[str, list[tuple[int, int, int]]], map_name: str, src: int) -> int:
    the_map = maps[map_name]
    for i in range(len(the_map)):  # Check entries in reverse
        entry_src = the_map[i][0]
        entry_length = the_map[i][1]
        entry_dest = the_map[i][2]

        # if our source falls between this entry's range, remap it using this entry
        if entry_src <= src < entry_src + entry_length:
            return src - entry_src + entry_dest
        # If our source is less than entry src, since we already checked all the ones
        # before it, our source must not be in an entry, so return the original source.
        if src < entry_src:
            return src
    return src  # If we haven't already returned, return the original source


def map_ranges(the_map: list[tuple[int, int, int]], src_ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    rngs_to_check = src_ranges.copy()
    new_ranges = []
    map_ranges_checked = 0  # This was meant to save time when checking maps that are definitely lower than our ranges
    # ^ this breaks the code for some reason, not sure why yet
    while len(rngs_to_check) > 0:
        rng = rngs_to_check.pop(0)
        src_start = rng[0]
        src_length = rng[1]
        # Loop over all map ranges
        for i in range(map_ranges_checked, len(the_map)):
            map_start = the_map[i][0]
            map_length = the_map[i][1]
            map_dest = the_map[i][2]

            # Src range is after this range, skip it and move on
            if src_start >= map_start + map_length:
                map_ranges_checked += 1  # Update this counter so we don't count this range for other src ranges
                continue

            # Src range starts before map range
            if src_start < map_start:
                # Src range ends before map rng starts, no need for fancy shenanigans
                if src_start + src_length < map_start:
                    new_ranges.append(rng)
                    break

                new_ranges.append((src_start, map_start - src_start))
                src_length -= map_start - src_start
                src_start = map_start

            # Src range overflows this map range
            if src_start + src_length > map_start + map_length:
                rngs_to_check.insert(0, (map_start + map_length, src_length + src_start - (map_start + map_length)))
                src_length = map_start + map_length - src_start
                # maps_ranges_checked += 1  # This would work if we could guarantee that source ranges don't overlap.
                # Sadly, we can't.

            # Src range fits inside the map range
            skip = src_start - map_start
            new_ranges.append((map_dest + skip, src_length))
            break  # If we made it here, then we've successfully mapped the src range

        # Src range didn't fit in any of the map ranges, just add the src range
        if src_start >= the_map[-1][0] + the_map[-1][1]:
            new_ranges.append(rng)
    return sorted(new_ranges)


def part_one():
    file = open("inputs/tylerinput.txt")
    file_lines = [line.removesuffix('\n') for line in file]

    seeds = [int(s) for s in file_lines[0].split(': ')[1].split()]

    maps = {}
    working_name = ""
    working_map = []
    for i in range(2, len(file_lines)):
        line = file_lines[i]

        if line == '':
            maps[working_name] = sorted(working_map)
            working_name = ""
            working_map = []
            continue

        if not line[0].isdigit():
            working_name = line.split(' map:')[0]
            continue

        destination = int(line.split()[0])
        source = int(line.split()[1])
        length = int(line.split()[2])
        working_map.append((source, length, destination))
        print("Line " + str(i+1) + " processed")

    # finish any working map
    if working_name != '':
        maps[working_name] = sorted(working_map)

    min_loc = math.inf
    for seed in seeds:
        soil = access_map(maps, "seed-to-soil", seed)
        fertilizer = access_map(maps, "soil-to-fertilizer", soil)
        water = access_map(maps, "fertilizer-to-water", fertilizer)
        light = access_map(maps, "water-to-light", water)
        temperature = access_map(maps, "light-to-temperature", light)
        humidity = access_map(maps, "temperature-to-humidity", temperature)
        location = access_map(maps, "humidity-to-location", humidity)

        min_loc = min(min_loc, location)

    print(min_loc)


def part_two():
    file = open("inputs/tylerinput.txt")
    file_lines = [line.removesuffix('\n') for line in file]

    seed_nums = [int(s) for s in file_lines[0].split(': ')[1].split()]
    seed_ranges = sorted([(seed_nums[2 * i], seed_nums[2 * i + 1]) for i in range(len(seed_nums) // 2)])

    maps = {}
    working_name = ""
    working_map = []
    for i in range(2, len(file_lines)):
        line = file_lines[i]

        if line == '':
            maps[working_name] = sorted(working_map)
            working_name = ""
            working_map = []
            continue

        if not line[0].isdigit():
            working_name = line.split(' map:')[0]
            continue

        destination = int(line.split()[0])
        source = int(line.split()[1])
        length = int(line.split()[2])
        working_map.append((source, length, destination))
        print("Line " + str(i + 1) + " processed")

    # finish any working map
    if working_name != '':
        maps[working_name] = sorted(working_map)

    soil_ranges = map_ranges(maps["seed-to-soil"], seed_ranges)
    print("mapped soil ranges: " + str(soil_ranges) + " Length " + str(len(soil_ranges)))
    fertilizer_ranges = map_ranges(maps["soil-to-fertilizer"], soil_ranges)
    print("mapped fertilizer ranges: " + str(fertilizer_ranges))
    water_ranges = map_ranges(maps["fertilizer-to-water"], fertilizer_ranges)
    print("mapped water ranges: " + str(water_ranges))
    light_ranges = map_ranges(maps["water-to-light"], water_ranges)
    print("mapped light ranges: " + str(light_ranges))
    temperature_ranges = map_ranges(maps["light-to-temperature"], light_ranges)
    print("mapped temperature ranges: " + str(temperature_ranges))
    humidity_ranges = map_ranges(maps["temperature-to-humidity"], temperature_ranges)
    print("mapped humidity ranges: " + str(humidity_ranges))
    location_ranges = map_ranges(maps["humidity-to-location"], humidity_ranges)

    print(location_ranges[0][0])


if __name__ == "__main__":
    # part_one()
    part_two()
    """
    soil_map = sorted([(98, 2, 50), (50, 48, 52)])
    fertilizer_map = sorted([(15, 37, 0), (52, 2, 37), (0, 15, 39)])
    seed_ranges = sorted([(79, 14), (55, 13)])
    print(seed_ranges)
    soil_ranges = map_ranges(soil_map, seed_ranges)
    print(soil_ranges)
    fertilizer_ranges = map_ranges(fertilizer_map, soil_ranges)
    print(fertilizer_ranges)
    """
