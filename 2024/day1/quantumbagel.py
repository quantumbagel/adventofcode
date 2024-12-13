input_file = 'inputs/quantumbagel.txt'
sep = " "*3
numbers = [(int((line.split(sep)[0])), int(line.split(sep)[1].replace('\n', ""))) for line in open(input_file)]

first_numbers = sorted([number_set[0] for number_set in numbers])

second_numbers = sorted([number_set[1] for number_set in numbers])


total_difference = 0
total_multiplication = 0
for first_number, second_number in zip(first_numbers, second_numbers):
    difference = abs(first_number - second_number)
    mult = second_numbers.count(first_number) * first_number
    total_difference += difference
    total_multiplication += mult

print(total_difference, total_multiplication)




