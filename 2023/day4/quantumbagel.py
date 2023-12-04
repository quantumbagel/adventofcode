sum_of_games = 0
for game, line in enumerate(open("inputs/quantumbagelinput.txt")):  # thanks max :D
    line = line.replace('\n', '')  # Remove trailing newline
    game += 1  # Use the real game ID
    winning_numbers = line.split(": ")[1].split(" |")[0]  # Get the winning numbers using string magic
    my_numbers = line.split("| ")[1]  # Our numbers are anything to the right of the bar
    winning_numbers = [int(i) for i in winning_numbers.split(" ") if i != ""]  # Turn them into a list of ints
    my_numbers = [int(i) for i in my_numbers.split(" ") if i != ""]  # Same
    game_total = 0
    for number in my_numbers:
        if number in winning_numbers:
            if game_total == 0:  # If the game total is 0, we have to manually set it to 1
                game_total = 1
            else:
                game_total *= 2  # Otherwise, multiply by 2
    sum_of_games += game_total  # Add the game to the total
print(sum_of_games)

# Part B
NUM_CARDS = 207  # Change this based on input
copies_held = {i: 1 for i in range(NUM_CARDS)}


def calculate_copies(winning, my):
    return sum([1 for num in my if num in winning])  # This is so slick lol


def add_one_to(ind):
    if ind in copies_held.keys():
        copies_held[ind] += 1
    else:
        copies_held[ind] = 1


for game_id, line in enumerate(open("inputs/quantumbagelinput.txt")):
    # Same code again
    winning_numbers = line.split(": ")[1].split(" |")[0]  # Get the winning numbers using string magic
    my_numbers = line.split("| ")[1]  # Our numbers are anything to the right of the bar
    winning_numbers = [int(i) for i in winning_numbers.split(" ") if i != ""]  # Turn them into a list of ints
    my_numbers = [int(i) for i in my_numbers.split(" ") if i != ""]  # Same
    for x in range(calculate_copies(winning_numbers, my_numbers)):
        for _ in range(copies_held[game_id]):
            add_one_to(x+1+game_id)
print(sum(copies_held.values()))
