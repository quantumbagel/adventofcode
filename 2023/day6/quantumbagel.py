def part_1():
    raw_lines = [[int(j) for j in i.split()[1:]] for i in open('inputs/quantumbagelinput.txt').readlines()]
    races = [[raw_lines[0][i], raw_lines[1][i]] for i in range(len(raw_lines[0]))]
    total_mult = 1
    for race in races:
        beat_times = 0
        for hold_time in range(race[0]):
            distance = hold_time * (race[0] - hold_time)
            if distance > race[1]:
                beat_times += 1
        total_mult *= beat_times
    print(total_mult)


def part_2():
    raw_lines = [int(''.join(i.split()[1:])) for i in open('inputs/quantumbagelinput.txt').readlines()]
    total_mult = 1
    beat_times = 0
    for hold_time in range(raw_lines[0]):
        distance = hold_time * (raw_lines[0] - hold_time)
        if distance > raw_lines[1]:
            beat_times += 1
        else:
            if beat_times:
                break
    total_mult *= beat_times
    print(total_mult)


part_2()