import time
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


# This is shamelessly stolen from Julian, all credit to him.
# All I did was comment it so you could have a fraction of an idea
# of what the heck is going on here.
def num_valid_arrangements_optimized(segments: list[str], counts: list[int], cache={}):
    # Use a caching system to save time
    key = "|".join(map(str, counts))
    key += "-" + ":".join(segments)
    if key in cache:
        # print("Used cache on key " + key)
        return cache[key]

    if len(segments) <= 0:
        if len(counts) > 0:
            return 0
        return 1

    if len(counts) <= 0:
        # No more damaged springs should exist. If we find one, this is an invalid arrangement
        for segment in segments:
            if '#' in segment:
                return 0
        # Otherwise, we're all good
        return 1

    segment = segments[0]
    count = counts[0]

    if count > len(segment) and "#" in segment:
        return 0

    # Recursion time
    num_arr = 0

    # Simulate cases where the required count is in this segment
    for i in range(len(segment) - count + 1):
        left = segment[:i]  # Everything to the left of the possibly damaged cluster

        if '#' in left:  # We've passed the first guaranteed damaged spring, no more to check for this segment
            break

        right = segment[i + count:]  # Everything to the right of the possibly damaged cluster

        if right.startswith('#'):  # A damaged cluster must be followed by a '.' to be its own cluster
            continue

        new_segments = segments[1:]  # Splitting the segments
        if len(right) > 1:  # Segments less than length 2 aren't worth checking
            new_segments.insert(0, right[1:])  # First char of right has to be a '.', don't include it
        num_arr += num_valid_arrangements_optimized(new_segments, counts[1:])

    # Account for case where this segment is all functional springs.
    # Only possible if there are no guaranteed damaged springs.
    if '#' not in segment:
        num_arr += num_valid_arrangements_optimized(segments[1:], counts)

    cache[key] = num_arr
    return num_arr


def part_one():
    file = open("input.txt")

    total = 0
    for line in file:
        line = line.removesuffix('\n')
        template = line.split()[0]
        counts = [int(s) for s in line.split()[1].split(',')]

        total += num_valid_arrangements(template, counts)
    print(total)


def part_two():
    file = open("inputs/tylerinput.txt")

    total = 0
    for line in file:
        line = line.removesuffix('\n')
        spring_list = ((line.split()[0] + '?') * 5)[:-1]
        segments = [_ for _ in spring_list.split('.') if _]
        counts = [int(s) for s in line.split()[1].split(',')] * 5
        total += num_valid_arrangements_optimized(segments, counts)

    print(total)


if __name__ == "__main__":
    start_time = time.time()
    # part_one()
    part_two()
    print(str(time.time() - start_time) + " s")
