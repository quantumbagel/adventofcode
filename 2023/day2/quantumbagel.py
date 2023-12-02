# i've tried to comment this code well lol
file_to_read = "input.txt"  # which file are we going to read from?
file_object = open(file_to_read)

file_lines = [i.replace('\n', '') for i in file_object.readlines()]
# For a better understanding of the above line, read this excellent tutorial: https://www.w3schools.com/python/python_lists_comprehension.asp
color_limits = {"red": 12, "green": 13, "blue": 14}  # from the problem
id_sum = 0
for id, line in enumerate(file_lines):  # Iterate through each line in the file:
    where_is_the_colon = line.index(":")  # Returns the index of the colon (we don't need the Game 1: text)
    line = line[where_is_the_colon + 2:]  # this removes everything but the list of numbers and colors
    valid_game = True
    list_of_instructions = []
    tmp = []
    # the below section of code from 17 to 24 is kinda confusing, so I'll explain it over chat (just DM me)
    for marble_pick in line.split(", "):
        if ";" not in marble_pick:
            tmp.append(marble_pick)
        else:
            tmp.append(marble_pick.split('; ')[0])
            list_of_instructions.append(tmp)
            tmp = [marble_pick.split('; ')[1]]
    list_of_instructions.append(tmp)
    # List_of_instructions is now [["6 blue", "3 red"], ["2 green", "1 blue"]] with each sublist representing a sequence of draws w/out replacment
    valid_game = True  # a boolean to check if the game is still valid
    for instruction in list_of_instructions:
        current_stock_of_marbles = color_limits.copy()  # this is to prevent the original color_limits from being overwritten
        for marble_pick in instruction:
            number = int(marble_pick.split()[0])  # string.split()'s default argument is a space, so we have a list like ["6", "blue"]. This is why we apply the int cast
            color = marble_pick.split()[1]  # same thing here
            current_stock_of_marbles[color] -= number  # remove the marbles from the current stock
            if current_stock_of_marbles[color] < 0:  # if it is now negative, then the game must be invalid
                valid_game = False
                break
        if valid_game is False:  # this exits out of the second for loop
            break
    if valid_game:  # the game was valid!
        id_sum += id + 1  # Add id + 1 (the game ids start at 1 but the enumerate index starts at 0)
    print(f"Game {id+1}: {line} was {valid_game}")
print(id_sum)  # Print the answer!

