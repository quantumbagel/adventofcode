# This is a manual version. I just typed the numbers in. It was faster than creating a readlines file lol
import math
def count_ways_to_beat_record(T, D):
    count = 0
    for t in range(1, T):
        if t * (T - t) > D:
            count += 1
    return count
races = [(48938595,296192812361391)]
ways_to_win = [count_ways_to_beat_record(T, D) for T, D in races]
result = math.prod(ways_to_win)
print(result)
