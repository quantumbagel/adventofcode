import string

f = open('input.txt')
g = f.readlines()
x = 0
numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
number_dict = {'zero': "0", 'one': "1", 'two': "2", 'three': "3", 'four': "4",
               'five': "5", 'six': "6", 'seven': "7", 'eight': "8", 'nine': "9"}


def get_next_word_from_string(search: str, index):
    """
    Calculate how far away the next index of a number is
    :param search: The string to search
    :param index: The index from which to start from
    :return: The name of the next number, and how far it is (0 is next char)
    """
    search = search[index:]
    minimum_index = 10000000
    minimum_number = ''
    for number in numbers:
        try:
            index_found = search.index(number)  # Where is this number
        except ValueError:  # The number doesn't exist, continue on to the next one
            continue
        if index_found < minimum_index:  # If the index is smaller than the previous value
            minimum_index = index_found  # Update it
            minimum_number = number
    return minimum_number, minimum_index  # Return smallest value


r_strings = []
for item in g:
    r_string = ''
    track = 0
    item = item.replace('\n', "").replace(" ", "")
    for i, char in enumerate(item):
        next_word, ind = get_next_word_from_string(item, track)
        if ind > 0 or ind == -1:  # If the next text-based number isn't the next character
            r_string += char  # Add the char
        else:
            r_string += number_dict[next_word]  # Add the translated text-based number
        track += 1
    r_strings.append(r_string)  # Add the final string
tot = 0
for line in r_strings:
    for letter in string.ascii_letters:  # Make sure there are no letters left
        line = line.replace(letter, "")
    tot += int(line[0] + line[-1])  # Add the first and last chars
print(tot)
