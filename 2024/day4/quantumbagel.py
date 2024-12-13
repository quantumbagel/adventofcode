words = [[char for char in line.replace("\n", "")] for line in open("inputs/quantumbagel.txt")]

print(words)
word_to_find = "XMAS"
empty_words = [["." for i in range(len(words[0]))] for _ in range(len(words))]

def check_word_search_part1(starting_row, starting_col):
    found_matches = 8 # /8 possible:
    """
    S..S..S
    .A.A.A.
    ..MMM..
    SAMXMAS
    ..MMM..
    .A.A.A.
    S..S..S
    """
    if words[starting_row][starting_col] != word_to_find[0]: # Only check if this position starts with the first letter
        return 0

    paths = [[0, 1], [0, -1], [1,0], [-1,0], [-1, 1], [-1, -1], [1,1], [1, -1]]  # Use as delta

    for path in paths:
        if path[1] > 0 and starting_col + (len(word_to_find)-1) >= len(words):
            found_matches -= 1
            continue
        if path[1] < 0 and starting_col - (len(word_to_find)-1) < 0:
            found_matches -= 1
            continue
        if path[0] > 0 and starting_row + (len(word_to_find)-1) >= len(words[0]):
            found_matches -= 1
            continue
        if path[0] < 0 and starting_row - (len(word_to_find)-1) < 0:
            found_matches -= 1
            continue
        # 4 0 [-1, 0]
        # print(path)
        broke =False
        for i in range(len(word_to_find)-1):  # Check for [X]MAS
            # print(starting_row+(path[0]*(i+1)), starting_col+(path[1]*(i+1)), words[starting_row+(path[0]*(i+1))][starting_col+(path[1]*(i+1))], word_to_find[i+1])
            if words[starting_row+(path[0]*(i+1))][starting_col+(path[1]*(i+1))] != word_to_find[i+1]:
                found_matches -= 1
                broke = True
                break
        if not broke:
            for i in range(len(word_to_find)):
                empty_words[starting_row+(path[0]*(i))][starting_col+(path[1]*(i))] = word_to_find[i]




    return found_matches

def check_word_search_part2(starting_row, starting_col):
    if words[starting_row][starting_col] != "A": # Only check if this position is A (M[A]S)
        return False

    if starting_col == 0 or starting_col == len(words[0])-1 or starting_row == 0 or starting_row == len(words)-1:
        # on the edge
        return False

    is_left_mas = ((words[starting_row-1][starting_col-1] == "S" and words[starting_row+1][starting_col+1] == "M")
                 or (words[starting_row-1][starting_col-1] == "M" and words[starting_row+1][starting_col+1] == "S"))

    is_right_mas = ((words[starting_row-1][starting_col+1] == "S" and words[starting_row+1][starting_col-1] == "M")
                 or (words[starting_row-1][starting_col+1] == "M" and words[starting_row+1][starting_col-1] == "S"))

    if is_left_mas and is_right_mas:
        return True

matches = 0
for i in range(len(words)):
    for j in range(len(words[i])):
        matches += check_word_search_part1(i, j)
print(matches)
print("\n".join(["".join(l) for l in empty_words]))


matches = 0
for i in range(len(words)):
    for j in range(len(words[i])):
        matches += 1 if check_word_search_part2(i, j) else 0
print(matches)