lines = [i.replace("\n", "") for i in open("inputs/quantumbagel.txt").readlines()]


rules = {}
books = []
is_rules = True
for line in lines:
    if line == "":
        is_rules = False
        continue

    if is_rules:
        first_page = int(line.split("|")[0])
        second_page = int(line.split("|")[1])
        if first_page not in rules:
            rules[first_page] = [second_page]
        else:
            rules[first_page].append(second_page)
    else:
        books.append([int(i) for i in line.split(",")])

valid_books_sum = 0
invalid_books = []
for book in books:
    already_occurred = []
    valid = True
    for page in book:
        if page not in rules:
            already_occurred.append(page)
            continue
        for must_be_after in rules[page]:
            if must_be_after in already_occurred:
                valid = False
                break
        already_occurred.append(page)
        if not valid:
            invalid_books.append(book)
            break
    if valid:
        valid_books_sum += book[int((len(book)-1)/2)]

print(valid_books_sum)

updated_invalid_books = []
for book in invalid_books:
    book_loop = book[:]
    book_iteration = book[:]
    while True:
        updated = False
        for index, page in enumerate(book_loop[::-1]):
            if page not in rules:
                continue
            for new_index, previous_number in enumerate(book_loop[:len(book)-index]):
                if previous_number in rules[page]:
                    book_iteration.remove(page)
                    book_iteration.insert(new_index, page)

                    updated = True
                    break
            if updated:
                book_loop = book_iteration[:]
                break
        if not updated:
            break
    updated_invalid_books.append(book_iteration)

print(updated_invalid_books)
p2_score = 0
for b in updated_invalid_books:
    p2_score += b[int((len(b) - 1) / 2)]

print(p2_score)





