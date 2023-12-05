
def part_1():
    lines = [i.removesuffix('\n') for i in open('input.txt').readlines()]
    seed_numbers = [int(j) for j in lines[0].split(': ')[1].split()]
    maps = []
    add_to = False
    temp = []
    for line in lines[2:]:  # ignore the first line and second line (newline)
        if 'map' in line:
            add_to = True
        elif add_to and line != '':
            temp.append(line.split())
        else:
            add_to = False
            maps.append(temp)
            temp = []
    maps.append(temp)  # catch the last category (hum-to-loc)
    lowest_loc = 10000000000000
    for seed in seed_numbers:
        for transform in maps:
            for index, m in enumerate(transform):
                if seed in range(int(m[1]), int(m[1])+int(m[2])):
                    seed -= int(m[1]) - int(m[0])
                    break
        if seed < lowest_loc:
            lowest_loc = seed
    print(lowest_loc)


def part_2():
    lines = [i.removesuffix('\n') for i in open('inputs/quantumbagelinput.txt').readlines()]

    def is_overlap(a, b):
        """
        Check if two ranges overlap
        :param a: The first range
        :param b: The second range
        :return: If the ranges overlap
        """
        return a[-1] > b[0] and a[0] < b[-1]

    seed_numbers = []
    last_start = -1
    for x in lines[0].split(": ")[1].split():
        if last_start == -1:
            last_start = int(x)
        else:
            seed_numbers.append(range(last_start, int(x)+last_start))  # Add the range of seeds, not all of them :P
            last_start = -1
    maps = []
    add_to = False
    temp = []
    for line in lines[2:]:  # ignore the first line and second line (newline)
        if 'map' in line:
            add_to = True
        elif add_to and line != '':
            temp.append(line.split())
        else:
            add_to = False
            maps.append(temp)
            temp = []
    maps.append(temp)  # catch the last category (hum-to-loc)

    for i in range(7):  # 7 categories
        n_seeds = []
        for seed_range in seed_numbers:
            acc = False
            for n in maps[i]:
                transform_range = range(int(n[1]), int(n[1]) + int(n[2]))  # Calculate the transformable numbers
                calc_range = range(max(transform_range[0], seed_range[0]) - int(n[1])+int(n[0]), min(transform_range[-1], seed_range[-1]) + 1 - int(n[1])+int(n[0]))  # Calculate where those numbers would go
                if max(transform_range[0], seed_range[0]) > min(transform_range[-1], seed_range[-1]) + 1 or not is_overlap(transform_range, seed_range):  # Is the range valid, and do the transform and seed ranges not overlap?
                    continue
                acc = True
                n_seeds.append(calc_range)  # Update the new seed list
            if not acc:
                n_seeds.append(seed_range)
                # If we didn't add the range, all the numbers are the same after this iteration,
                # so add it to the next one
        seed_numbers = n_seeds

    lowest_loc = 100000000000000000
    for rng in seed_numbers:
        if rng[0] < lowest_loc:  # It's a range, so get the lowest value
            lowest_loc = rng[0]
    print(lowest_loc)

# day_1()
day_2()
