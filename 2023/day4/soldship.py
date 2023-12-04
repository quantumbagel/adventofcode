# quantumsoldship's Horribly Inefficient Code that Gets the Job Done

# I hope I commented well.

# Determining variables
predetermined = []  # The predetermined "winning" numbers
yours = []  # The scratch card's numbers that you uncovered

winning_numbers = []
your_numbers = []
counter = 0
sum = 0
lines = []

with open("/Users/isaacschool/Desktop/aocd4input.txt") as file:
    raw_lines = file.readlines()
for line in raw_lines:
    removed = line.removesuffix('\n')
    reremoved = removed.removesuffix('\'')
    lines.append(reremoved)

print(lines)

for thing in lines:
    print(thing)


# Here is where I split out the string into sections
    points = 0
    splitted = thing.split('|')

    # Section Start

    for k in range(1):
        segmented = splitted[k]
        resegmented = segmented.split(" ")
        for i in resegmented:
            if i.isdigit():
                if k == 0:
                    winning_numbers.append(i)
                else:
                    your_numbers.append(i)
    print(your_numbers)
    print(winning_numbers)
                
    for j in your_numbers:
        if j in winning_numbers:
            points += 1

    if points != 0:
        sum = 2 ** (points-1)
    break
    

print(sum)
