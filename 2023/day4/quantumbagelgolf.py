# This is my solution to day 4 (codegolf)
# Don't expect me to do this for most days, but this one was so ez I had to try

# Part a (11 lines)
sum_of_games = 0
for game, line in enumerate([i.replace('\n', '') for i in open("inputs/quantumbagelinput.txt")]):  # thanks max :D
    game_total = 0
    for number in [int(i) for i in  line.split("| ")[1] .split(" ") if i != ""]:
        if number in [int(i) for i in line.split(": ")[1].split(" |")[0].split(" ") if i != ""]:
            if game_total == 0:  # If the game total is 0, we have to manually set it to 1
                game_total = 1
            else:
                game_total *= 2  # Otherwise, multiply by 2
    sum_of_games += game_total  # Add the game to the total
print(sum_of_games)


# Part b (6 lines)
copies_held = {i: 1 for i in range(207)}
for game_id, line in enumerate(open("inputs/quantumbagelinput.txt")):
    for x in range(sum([1 for num in [int(i) for i in line.split("| ")[1].split(" ") if i != ""] if num in [int(i) for i in  line.split(": ")[1].split(" |")[0].split(" ") if i != ""]])):
        for _ in range(copies_held[game_id]):
            copies_held[x+1+game_id] += 1
print(sum(copies_held.values()))
