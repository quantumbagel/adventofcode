def part_one():
    file = open("inputs/tylerinput.txt")
    patterns = []
    working = []
    for line in file:
        line = line.removesuffix('\n')
        if line == '':
            patterns.append(working)
            working = []
            continue

        working.append(line)

    patterns.append(working)

    summary = 0
    for pattern in patterns:
        refl_idx = 0
        refl_dist = 0
        for i in range(1, len(pattern)):
            candidate_idx = i - refl_dist * 2 - 1
            if candidate_idx < 0:
                break
            if pattern[i] == pattern[candidate_idx]:
                refl_idx = i - refl_dist
                refl_dist += 1
            else:
                refl_dist = 0

        if refl_dist > 0:
            summary += 100 * refl_idx  # Vertical reflection

        refl_idx = 0
        refl_dist = 0
        for i in range(1, len(pattern[0])):
            candidate_idx = i - refl_dist * 2 - 1
            if candidate_idx < 0:
                break
            column = [row[i] for row in pattern]
            candidate = [row[candidate_idx] for row in pattern]
            if column == candidate:
                refl_idx = i - refl_dist
                refl_dist += 1
            else:
                refl_dist = 0

        if refl_dist > 0:
            summary += refl_idx  # Horizontal reflection

    print(summary)


def part_two():
    file = open("input.txt")


if __name__ == "__main__":
    part_one()
    # part_two()
