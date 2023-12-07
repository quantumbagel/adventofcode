import math


def quadratic_roots(a, b, c) -> (float, float):
    discriminant = (b ** 2) - 4 * a * c
    if discriminant < 0:
        return None, None
    if discriminant == 0:
        return -b / (2 * a), -b / (2 * a)
    return (-b + math.sqrt(discriminant)) / (2 * a), (-b - math.sqrt(discriminant)) / (2 * a)


def part_one():
    file = open("inputs/tylerinput.txt")
    max_times = [int(s) for s in file.readline().split(': ')[1].split()]
    records = [int(s) for s in file.readline().split(': ')[1].split()]

    product = 1
    for i in range(len(max_times)):
        max_time = max_times[i]
        record = records[i]
        record_accel_times = quadratic_roots(1, -max_time, record)
        if record_accel_times[0] is None:
            continue

        min_record_break_time = math.floor(record_accel_times[1] + 1)
        max_record_break_time = math.ceil(record_accel_times[0] - 1)

        num_ways_to_win = max_record_break_time - min_record_break_time + 1
        product *= num_ways_to_win
    print(product)


def part_two():
    file = open("inputs/tylerinput.txt")
    max_time = int(file.readline().split(': ')[1].replace(' ', ''))
    record = int(file.readline().split(': ')[1].replace(' ', ''))

    record_accel_times = quadratic_roots(1, -max_time, record)
    if record_accel_times[0] is None:
        return

    min_record_break_time = math.floor(record_accel_times[1] + 1)
    max_record_break_time = math.ceil(record_accel_times[0] - 1)

    num_ways_to_win = max_record_break_time - min_record_break_time + 1
    print(num_ways_to_win)


if __name__ == "__main__":
    # part_one()
    part_two()