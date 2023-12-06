import math
def count_ways_to_beat_record(T, D):
    count = 0
    for t in range(1, T):
        if t * (T - t) > D:
            count += 1
    return count
races = []
length = input('How many times/distances are there?')
for i in range(int(length)):
    races.append([int(input('time? ')),int(input('distance? '))])    

ways_to_win = [count_ways_to_beat_record(T, D) for T, D in races]
result = math.prod(ways_to_win)
print(result)

# BOOOOOOM! #
# 15 Lines #
# This accepts all inputs and variables, all in 15 lines. #
# Let's gooooo! #
