import numpy as np


def check_numbers_for_safe(numbers):
    arr = np.array(numbers)
    # calculate the difference between adjacent elements of the array
    diff = np.diff(arr)
    # check if all differences are positive
    # using the np.all() function
    is_increasing = np.all(diff > 0) and np.all(3 >= diff)
    is_decreasing = np.all(diff < 0) and np.all(-3 <= diff)
    return is_increasing or is_decreasing



input_file = 'inputs/quantumbagel.txt'

numbers = [[int(i.replace('\n', '')) for i in condition.split(" ")] for condition in open(input_file)]

safe = 0
for number in numbers:
    if check_numbers_for_safe(number):
        safe += 1

print(safe)


safe = 0
for number in numbers:
    if check_numbers_for_safe(number):
        safe += 1
    else:
        for i in range(len(number)):
            partial_number = number[:i] + number[i+1:]
            if check_numbers_for_safe(partial_number):
                safe += 1
                break

print(safe)
