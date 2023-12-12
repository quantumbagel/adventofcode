from itertools import combinations


def num_valid_arrangements(template, counts):
    already_damaged = len([_ for _ in template if _ == '#'])
    left_to_damage = sum(counts) - already_damaged
    unknown_indices = [i for i, char in enumerate(template) if char == '?']

    total = 0
    for combo in combinations(unknown_indices, left_to_damage):
        is_valid = True
        current_count = 0
        segment = 0
        for idx, char in enumerate(template):
            if idx in combo or char == '#':
                current_count += 1
                continue

            if current_count != 0:
                if segment >= len(counts) or current_count != counts[segment]:
                    is_valid = False  # Either too many segments or the counts don't match
                    break
                current_count = 0
                segment += 1

        if not is_valid:
            continue

        if segment < len(counts) and current_count != counts[segment]:
            is_valid = False

        if is_valid:
            total += 1

    return total


def num_valid_arrangements_optimized(template: str, counts: list[int]):
    simplified = [_ for _ in template.split('.') if _ != '']
    segment_diff = len(counts) - len(simplified)

    print("----")
    print(simplified)

    if segment_diff == 0:
        edge_space = [len(seg) - counts[i] for i, seg in enumerate(simplified)]
        num_arr = 1
        for space in edge_space:
            num_arr *= space + 1
        print(num_arr)
        return num_arr


def part_one():
    file = open("input.txt")

    total = 0
    for line in file:
        line = line.removesuffix('\n')
        template = line.split()[0]
        counts = [int(s) for s in line.split()[1].split(',')]

        total += num_valid_arrangements(template, counts)
        num_valid_arrangements_optimized(template, counts)
    print(total)


def part_two():
    file = open("inputs/tylerinput.txt")

    total = 0
    for line in file:
        line = line.removesuffix('\n')
        template = line.split()[0]
        counts = [int(s) for s in line.split()[1].split(',')]

        # THIS METHOD DOESN'T WORK.
        # IT RELIES ON A SHORTCUT THAT ISN'T ALWAYS TRUE.
        # TRY TO THINK OF A WAY TO ACTUALLY OPTIMIZE THIS PROCESS.
        template_front = "?" + template
        counts_front = counts.copy()
        counts_front.insert(0, counts_front.pop())
        template_back = template + "?"
        counts_back = counts.copy()
        counts_back.append(counts_back.pop(0))

        num_normal_arr = num_valid_arrangements(template, counts)
        max_from_front = max(num_valid_arrangements(template_front, counts),
                             num_valid_arrangements(template_front, counts_front))
        max_from_back = max(num_valid_arrangements(template_back, counts),
                            num_valid_arrangements(template_back, counts_back))

        if template[0] == template[-1]:
            num_extra = max(max_from_front, max_from_back)
        elif template[-1] != '.':
            num_extra = max_from_back
        elif template[0] != '.':
            num_extra = max_from_front
        else:
            num_extra = max_from_front

        total += num_normal_arr * (num_extra ** 4)
    print(total)


if __name__ == "__main__":
    part_one()
    # part_two()
