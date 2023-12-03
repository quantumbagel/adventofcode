# define total number of cubes (12 red cubes, 13 green cubes, and 14 blue cubes)
redMax = 12
greenMax = 13
blueMax = 14

# establish counter to sum possible Game IDs
possibleGames = 0

# For each line in input txt
for line in open('inputs/maxinput.txt'):
    # homogenize seperators
    mod = line.replace('; ',',')
    mod = mod.replace(': ', ',')
    mod = mod.replace(', ', ',')
    # split on ,
    terms = mod.split(',')
    # flag for violations
    violation = 0

    redTotal = 0
    greenTotal = 0
    blueTotal = 0

    for term in terms:
        subterm = term.split(' ')
        if subterm[1] == 'green':
            greenTotal = greenTotal + int(subterm[0])
        if subterm[1] == 'red':
            redTotal = redTotal + int(subterm[0])
        if subterm[1] == 'blue':
            blueTotal = blueTotal + int(subterm[0])

    if greenTotal > greenMax:
        violation = 1
    if redTotal > redMax:
        violation = 1
    if blueTotal > blueMax:
        violation = 1


    if violation == 0:
        print('nonviolation' + ' ' + terms[0].split()[1])
    if violation == 0:
        gameid = terms[0].split()[1]
        print('Adding ' + gameid + ' to ' + str(possibleGames))
        possibleGames = int(gameid) + possibleGames
        print('Total: ' + str(possibleGames) + '\n')

print(possibleGames)





# read game id by removing word ("game") for first term

# for each term, detect which color each number is related to by detecting words ("green, red, blue")

# find maximum value for each color, compare to maximum limits for each color, determining which games are possible

# add game ids for the possible games to the possible games counter