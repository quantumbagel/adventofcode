import time


def part_one():
    file = open("inputs/tylerinput.txt")
    total = 0
    for line in file.readlines():
        history = [[int(s) for s in line.removesuffix('\n').split()]]

        # Compute the differences between all the previous entries
        diff_list = [history[0][i + 1] - history[0][i] for i in range(len(history[0]) - 1)]
        history.append(diff_list)  # Keep track of them
        check = sum([diff ** 2 for diff in diff_list]) == 0  # Check to see if they are all zero

        while not check:  # while the previous row isn't all zeroes
            # Compute the differences between all the previous entries
            diff_list = [history[-1][i + 1] - history[-1][i] for i in range(len(history[-1]) - 1)]
            history.append(diff_list)  # Keep track of them
            check = sum([diff ** 2 for diff in diff_list]) == 0  # Check to see if they are all zero

        # Easy way to calculate the extrapolated values
        extrapolated = 0
        for i in reversed(range(len(history) - 1)):
            extrapolated += history[i][-1]

        # Add extrapolated value to the total
        total += extrapolated

    print(total)


def part_two():
    file = open("inputs/tylerinput.txt")
    total = 0
    for line in file.readlines():
        history = [[int(s) for s in line.removesuffix('\n').split()]]

        # Compute the differences between all the previous entries
        diff_list = [history[0][i + 1] - history[0][i] for i in range(len(history[0]) - 1)]
        history.append(diff_list)  # Keep track of them
        check = sum([diff ** 2 for diff in diff_list]) == 0  # Check to see if they are all zero

        while not check:  # while the previous row isn't all zeroes
            # Compute the differences between all the previous entries
            diff_list = [history[-1][i + 1] - history[-1][i] for i in range(len(history[-1]) - 1)]
            history.append(diff_list)  # Keep track of them
            check = sum([diff ** 2 for diff in diff_list]) == 0  # Check to see if they are all zero

        # Easy way to calculate the extrapolated values
        extrapolated = 0
        for i in reversed(range(len(history) - 1)):
            extrapolated = history[i][0] - extrapolated

        # Add extrapolated value to the total
        total += extrapolated

    print(total)


if __name__ == "__main__":
    start_time = time.time()
    # part_one()
    part_two()
    print(str(time.time() - start_time) + " s")
