# quantumsoldship's Horribly Inefficient Code that Gets the Job Done

# I hope I commented well.
# Also, thanks to quantumbagel for the help

# Determining variables
predetermined = []  # The predetermined "winning" numbers
yours = []  # The scratch card's numbers that you uncovered


counter = 0
sum = 0
lines = []

with open("input.txt") as file:
    raw_lines = file.readlines()
for line in raw_lines:
    removed = line.removesuffix('\n')
    reremoved = removed.removesuffix('\'')
    lines.append(reremoved)

print(lines)

for thing in lines:
    points = 0
    splitted = thing.split('|')
    winning_numbers = []  # move reset to here
    your_numbers = []
    # Section Start
    for k in range(2):  # increased range
        segmented = splitted[k]
        resegmented = segmented.split(" ")
        for i in resegmented:
            if i.isdigit():
                if k == 0:
                    winning_numbers.append(i)
                else:
                    your_numbers.append(i)
    for j in your_numbers:
        if j in winning_numbers:
            points += 1

    if points != 0:
        sum += 2 ** (points-1)  # +=


