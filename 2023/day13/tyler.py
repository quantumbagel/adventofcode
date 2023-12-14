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


def find_mirror_idx(l: list[str], allow_smudge=False) -> int:
    refl_idx = 0
    refl_dist = 0
    i = 1
    used_smudge = not allow_smudge
    while i < len(l):
        candidate_idx = i - refl_dist * 2 - 1  # This is the line we're supposedly mirroring

        # If if we've already compared all existing lines to the left of the mirror,
        # then we might be done.
        if candidate_idx < 0:
            # If we didn't use a smudge when we were supposed to,
            # go back and find another reflection line.
            if allow_smudge and not used_smudge:
                refl_dist = 0
                i = refl_idx + 1
                continue
            break

        # Compare the current and candidate lines.
        # If we're using smudges, allow for one non-match.
        is_mirror = True
        for j in range(len(l[0])):
            if l[i][j] != l[candidate_idx][j]:
                if used_smudge:
                    used_smudge = not allow_smudge
                    is_mirror = False
                    break
                used_smudge = True

        # If the mirror was successful, increase the refl_distance
        if is_mirror:
            refl_idx = i - refl_dist
            refl_dist += 1
        elif refl_dist != 0:  # If we were working on a reflection
            refl_dist = 0  # Clear the reflection
            i = refl_idx  # Go back to where the reflection started so we can check for different ones
            used_smudge = not allow_smudge  # reset smudge flag
        i += 1

        # If we didn't use a smudge when we were supposed to,
        # go back and find another reflection line.
        if i >= len(l) and refl_dist != 0 and allow_smudge and not used_smudge:
            refl_dist = 0
            i = refl_idx + 1

    if refl_dist > 0:  # if we found a reflection
        return refl_idx
    return 0


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
        vertical_refl = find_mirror_idx(pattern, True)
        if vertical_refl > 0:
            summary += 100 * vertical_refl  # Vertical reflection
            continue  # No need to look for horizontal reflections

        columns = [''.join([row[i] for row in pattern]) for i in range(len(pattern[0]))]
        horizontal_refl = find_mirror_idx(columns, True)
        if horizontal_refl > 0:
            summary += horizontal_refl  # Horizontal reflection
            continue

    print(summary)


if __name__ == "__main__":
    # part_one()
    part_two()
