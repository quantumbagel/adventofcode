import string

file = open("input.txt")
raw_lines = file.readlines()
lines = []

# remove the new line characters
for line in raw_lines:
    lines.append(line.removesuffix("\n"))

# remove characters from the lines
lines_with_no_letters = []
for line in lines:
    # do stuff with the lines here
    # please
    # im begging u
    for letter in string.ascii_letters:
        line = line.replace(letter, "")
    lines_with_no_letters.append(line)

final = 0
for line in lines_with_no_letters:
    # Get the first and last numbers from the line
    first = line[0]
    last = line[-1]
    first_and_last_number = int(first + last)  # Add them
    final += first_and_last_number  # Add the total to the answer


print(final)