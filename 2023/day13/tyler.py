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
        i = 1
        while i < len(pattern):
            candidate_idx = i - refl_dist * 2 - 1
            if candidate_idx < 0:
                break
            if pattern[i] == pattern[candidate_idx]:
                refl_idx = i - refl_dist
                refl_dist += 1
            elif refl_dist != 0:
                refl_dist = 0
                i = refl_idx
            i += 1

        if refl_dist > 0:
            summary += 100 * refl_idx  # Vertical reflection

        refl_idx = 0
        refl_dist = 0
        columns = [''.join([row[i] for row in pattern]) for i in range(len(pattern[0]))]
        i = 1
        while i < len(pattern[0]):
            candidate_idx = i - refl_dist * 2 - 1
            if candidate_idx < 0:
                break
            if columns[i] == columns[candidate_idx]:
                refl_idx = i - refl_dist
                refl_dist += 1
            elif refl_dist != 0:
                refl_dist = 0
                i = refl_idx
            i += 1

        if refl_dist > 0:
            summary += refl_idx  # Horizontal reflection

    print(summary)


def line_diff(line1: str, line2: str):
    diff = 0
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            diff += 1
    return diff


def part_two():
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
        i = 1
        used_smudge = False
        while i < len(pattern):
            candidate_idx = i - refl_dist * 2 - 1
            if candidate_idx < 0:
                break

            diff = line_diff(pattern[i], pattern[candidate_idx])
            if diff == 0 or (diff == 1 and not used_smudge):
                refl_idx = i - refl_dist
                refl_dist += 1
                if diff == 1:
                    used_smudge = True
            elif refl_dist != 0:
                refl_dist = 0
                i = refl_idx
                used_smudge = False
            i += 1

        if refl_dist > 0:
            summary += 100 * refl_idx  # Vertical reflection
            continue  # No need to look for horizontal reflections

        refl_idx = 0
        refl_dist = 0
        columns = [''.join([row[i] for row in pattern]) for i in range(len(pattern[0]))]
        i = 1
        used_smudge = False
        while i < len(pattern[0]):
            candidate_idx = i - refl_dist * 2 - 1
            if candidate_idx < 0:
                break

            diff = line_diff(columns[i], columns[candidate_idx])
            if diff == 0 or (diff == 1 and not used_smudge):
                refl_idx = i - refl_dist
                refl_dist += 1
                if diff == 1:
                    used_smudge = True
            elif refl_dist != 0:
                refl_dist = 0
                i = refl_idx
                used_smudge = False
            i += 1

        if refl_dist > 0:
            summary += refl_idx  # Horizontal reflection

    print(summary)


if __name__ == "__main__":
    # part_one()
    part_two()
