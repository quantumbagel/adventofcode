import math


def part_1():
    input_transform = {}
    pattern = ''
    for i, line in enumerate(open('inputs/quantumbagelinput.txt')):
        line = line.removesuffix('\n')
        if i == 0:  # Get the pattern on the first line
            pattern = line
            continue
        if i == 1:  # Second line is newline, ignore
            continue
        l = line.split("= ")[1].split(", ")[0].replace('(', '')  # Get the "left" number
        r = line.split("= ")[1].split(", ")[1].replace(")", '')  # Get the "right" number
        input_transform.update({line.split(" =")[0]: [l, r]})  # Add to the dictionary
    current = "AAA"
    pattern_index = 0
    left_right = "LR"
    steps = 0
    while current != "ZZZ":
        current = input_transform[current][left_right.index(pattern[pattern_index])]  # Find the next ID
        pattern_index += 1  # Update the pattern index
        pattern_index %= len(pattern)
        steps += 1  # Increment steps

    print(steps)


def part_2():
    # This code (thru line 49) is the same file parsing from part 1
    input_transform = {}
    pattern = ''
    for i, line in enumerate(open('inputs/quantumbagelinput.txt')):
        line = line.removesuffix('\n')
        if i == 0:
            pattern = line
            continue
        if i == 1:
            continue
        l = line.split("= ")[1].split(", ")[0].replace('(', '')
        r = line.split("= ")[1].split(", ")[1].replace(")", '')
        input_transform.update({line.split(" =")[0]: [l, r]})
    current = []
    start = []
    for item in input_transform.keys():
        if item.endswith("A"):
            current.append(item)
            start.append(item)

    pattern_index = 0
    left_right = "LR"  # So we can use .index() on line 59
    steps = 0
    z_appear = {}  # z_appear tracks the index when the Z number appears and where it appears
    zapp_found = False
    while True:
        n_current = []
        for ind, item in enumerate(current):
            n_current.append(input_transform[item][left_right.index(pattern[pattern_index])])
            if item.endswith("Z") and item not in z_appear:
                # Add the new item to z_appear. NOTE: The puzzle has a quirk -
                # the first discovered step of a Z value is the variance in-between loops
                z_appear.update({item: [steps, ind]})
                continue
            if len(z_appear) == 6:  # There are 6 starting values in the input
                zapp_found = True
                break
        pattern_index += 1  # Go to the next pattern
        pattern_index %= len(pattern)
        steps += 1  # Increment steps
        if zapp_found:  # Help i'm stuck in a while loop factory
            break
        current = n_current[:]  # Update list for next iteration

    # Calculate LCM of the numbers
    numbers = [i[0] for i in z_appear.values()]
    lcm = 1
    for i in numbers:
        lcm = lcm * i // math.gcd(lcm, i)
    print(lcm)


part_2()
