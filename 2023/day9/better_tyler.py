import time

"""
DISCLAIMER: This solution is not 100% accurate.
It assumes that if a sequence begins with 0 and ends with 0,
then everything in between must also be 0. This is not always
the case, and for that reason, it is possible for this algorithm
to give the wrong answer. However, it is right in the majority
of situations, so I just wanted to see how much faster I could
make the algorithm by making said assumption.
"""

def part_one():
    file = open("inputs/tylerinput.txt")
    total = 0
    for line in file.readlines():
        history = [int(s) for s in line.removesuffix('\n').split()]

        most_recent = [history[-1]]
        edge = [history[-1]]
        i = len(history) - 1
        while most_recent[-1] != 0:
            i -= 1
            current = history[i]
            for j in range(len(edge)):
                diff = edge[j] - current
                edge[j] = current
                current = diff
            most_recent.append(current)
            edge.append(current)

        extrapolated = sum(most_recent)
        total += extrapolated
    print(total)


def part_two():
    file = open("inputs/tylerinput.txt")
    total = 0
    for line in file.readlines():
        history = [int(s) for s in line.removesuffix('\n').split()]

        most_recent_r = [history[-1]]
        edge_r = [history[-1]]
        most_recent_l = [history[0]]
        edge_l = [history[0]]
        i = 0
        while most_recent_l[-1] != 0 or most_recent_r[-1] != 0:
            i += 1
            current_r = history[len(history) - 1 - i]
            current_l = history[i]
            for j in range(len(edge_r)):
                diff_r = edge_r[j] - current_r
                edge_r[j] = current_r
                current_r = diff_r

                diff_l = current_l - edge_l[j]
                edge_l[j] = current_l
                current_l = diff_l

            most_recent_r.append(current_r)
            edge_r.append(current_r)
            most_recent_l.append(current_l)
            edge_l.append(current_l)

        # Easy way to calculate the extrapolated values
        extrapolated = 0
        for i in reversed(range(len(most_recent_l))):
            extrapolated = most_recent_l[i] - extrapolated

        # Add extrapolated value to the total
        total += extrapolated
    print(total)


if __name__ == "__main__":
    start_time = time.time()
    # part_one()
    part_two()
    print(str(time.time() - start_time) + " s")


