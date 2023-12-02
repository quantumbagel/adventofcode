import string

f = open('input.txt')
# part 1
g = f.readlines()
x = 0
numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
number_dict = {'zero': "0", 'one': "1", 'two': "2", 'three': "3", 'four': "4", 'five': "5", 'six': "6", 'seven': "7", 'eight': "8", 'nine': "9"}
def get_next_word_from_string(string: str, index):
    string = string[index:]
    minimum_index = 10000000
    minimum_number = ''
    for number in numbers:
        try:
            index_found = string.index(number)
        except ValueError:
            continue
        if index_found < minimum_index:
            minimum_index = index_found
            minimum_number = number
    return minimum_number, minimum_index
r_strings = []
for item in g:
    r_string = ''
    track = 0
    item = item.replace('\n', "").replace(" ", "")
    for i, char in enumerate(item):
        next_word, ind = get_next_word_from_string(item, track)
        if ind > 0 or ind == -1:
            track += 1
            r_string += char
            continue
        else:
            r_string += number_dict[next_word]
            track += 1
    r_strings.append(r_string)
tot = 0
for line in r_strings:
    for letter in string.ascii_letters:
        line = line.replace(letter, "")
    tot += int(line[0] + line[-1])
print(tot)
