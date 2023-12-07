
# Part 1 in 8 lines (7 w/out print)
def part_1():
    total_mult = 1
    for race in [[[[int(j) for j in i.split()[1:]] for i in open('inputs/quantumbagelinput.txt').readlines()][0][i], [[int(j) for j in i.split()[1:]] for i in open('inputs/quantumbagelinput.txt').readlines()][1][i]] for i in range(len([[int(j) for j in i.split()[1:]] for i in open('inputs/quantumbagelinput.txt').readlines()][0]))]:
        beat_times = 0
        for hold_time in range(race[0]):
            if hold_time * (race[0] - hold_time) > race[1]:
                beat_times += 1
        total_mult *= beat_times
    print(total_mult)

# Part 2 in 5 lines (4 w/out print). Note, this will take *forever* because of the file IO, so look below

def part_2():
    beat_times = 0
    for hold_time in range([int(''.join(i.split()[1:])) for i in open('inputs/quantumbagelinput.txt').readlines()][0]):
        if hold_time * ([int(''.join(i.split()[1:])) for i in open('inputs/quantumbagelinput.txt').readlines()][0] - hold_time) > [int(''.join(i.split()[1:])) for i in open('inputs/quantumbagelinput.txt').readlines()][1]:
            beat_times += 1
    print(beat_times)

# Part 2 that *doesn't* take forever (6 lines) 5 w/out print

def part_2_fileIO():
    read_lines = open('inputs/quantumbagelinput.txt').readlines()
    beat_times = 0
    for hold_time in range([int(''.join(i.split()[1:])) for i in read_lines][0]):
        if hold_time * ([int(''.join(i.split()[1:])) for i in read_lines][0] - hold_time) > [int(''.join(i.split()[1:])) for i in read_lines][1]:
            beat_times += 1
    print(beat_times)



print(part_2_fileIO())
