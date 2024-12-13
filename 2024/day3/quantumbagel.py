import re; print(sum([int(item.replace("mul(", "").replace(")", "").split(",")[0]) * int(item.replace("mul(", "").replace(")", "").split(",")[1]) for item in re.findall("mul+\([\d,)]+,[\d,)]+\)", "".join(open("inputs/quantumbagel.txt").readlines()).replace("\n", ""))]))




def parse_and_compute(memory):
    # Regular expressions to identify valid instructions
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")

    # Start with mul instructions enabled
    mul_enabled = True
    total = 0

    # Scan through the memory to find instructions
    position = 0
    while position < len(memory):
        # Check for do()
        if match := do_pattern.match(memory, position):
            mul_enabled = True
            position = match.end()
        # Check for don't()
        elif match := dont_pattern.match(memory, position):
            mul_enabled = False
            position = match.end()
        # Check for mul(X, Y)
        elif match := mul_pattern.match(memory, position):
            if mul_enabled:
                x, y = map(int, match.groups())
                total += x * y
            position = match.end()
        else:
            # Move to the next character if no match is found
            position += 1

    return total

# Example corrupted memory


# Calculate the result
result = parse_and_compute("".join(open("inputs/quantumbagel.txt").readlines()))
print("part2:", result)
