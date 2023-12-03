# i've tried to comment this code well lol
file_to_read = "inputs/quantumbagelinput.txt"  # which file are we going to read from?
file_object = open(file_to_read)

file_lines = [i.replace('\n', '') for i in file_object.readlines()]
# For a better understanding of the above line, read this excellent tutorial:
# https://www.w3schools.com/python/python_lists_comprehension.asp
color_limits = {"red": 12, "green": 13, "blue": 14}  # from the problem
id_sum = 0
for id, line in enumerate(file_lines):  # Iterate through each line in the file:
    where_is_the_colon = line.index(":")  # Returns the index of the colon (we don't need the Game 1: text)
    line = line[where_is_the_colon + 2:]  # this removes everything but the list of numbers and colors
    valid_game = True
    list_of_instructions = []
    for marble_pick in line.split("; "):
        list_of_instructions.append([i for i in marble_pick.split(', ')])
    # List_of_instructions is now [["6 blue", "3 red"], ["2 green", "1 blue"]] with each sublist representing a
    # sequence of draws w/out replacment
    valid_game = True  # a boolean to check if the game is still valid
    for instruction in list_of_instructions:
        current_stock_of_marbles = color_limits.copy()  # this is to prevent the original color_limits from being
        # overwritten
        for marble_pick in instruction:
            number = int(marble_pick.split()[0])  # string.split()'s default argument is a space, so we have a list
            # like ["6", "blue"]. This is why we apply the int cast
            color = marble_pick.split()[1]  # same thing here
            current_stock_of_marbles[color] -= number  # remove the marbles from the current stock
            if current_stock_of_marbles[color] < 0:  # if it is now negative, then the game must be invalid
                valid_game = False
                break
        if valid_game is False:  # this exits out of the second for loop
            break
    if valid_game:  # the game was valid!
        id_sum += id + 1  # Add id + 1 (the game ids start at 1 but the enumerate index starts at 0)


sum_of_powers = 0
for id, line in enumerate(file_lines):  # Iterate through each line in the file:
    where_is_the_colon = line.index(":")  # Returns the index of the colon (we don't need the Game 1: text)
    line = line[where_is_the_colon + 2:]  # this removes everything but the list of numbers and colors
    valid_game = True
    list_of_instructions = []
    for marble_pick in line.split("; "):
        list_of_instructions.append([i for i in marble_pick.split(', ')])
    max_stock = {"red": 0, "green": 0, "blue": 0}
    # List_of_instructions is now [["6 blue", "3 red"], ["2 green", "1 blue"]] with each sublist representing a
    # sequence of draws w/out replacement
    for instruction in list_of_instructions:
        current_stock_of_marbles = {"red": 0, "green": 0, "blue": 0}  # this is to prevent the original color_limits
        # from being overwritten
        for marble_pick in instruction:
            number = int(marble_pick.split()[0])  # string.split()'s default argument is a space, so we have a list
            # like ["6", "blue"]. This is why we apply the int cast
            color = marble_pick.split()[1]  # same thing here
            current_stock_of_marbles[color] += number  # add the marbles to the current stock
        for key_var in current_stock_of_marbles.keys():
            if max_stock[key_var] < current_stock_of_marbles[key_var]:
                max_stock[key_var] = current_stock_of_marbles[key_var]
    sum_of_powers += max_stock['red']*max_stock['blue']*max_stock['green']

print(sum_of_powers)  # Print the answer!
