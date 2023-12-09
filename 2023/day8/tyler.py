import math


def part_one():
    file = open("inputs/tylerinput.txt")
    file_lines = [line.removesuffix('\n') for line in file]
    path_segment = file_lines[0]

    graph = {}
    for i in range(2, len(file_lines)):
        line = file_lines[i]
        start_node = line.split(" = ")[0]
        neighbors = line.split(" = ")[1][1:-1].split(', ')
        graph[start_node] = neighbors

    steps = 0
    current_node = "AAA"
    while current_node != "ZZZ":
        dir = path_segment[steps % len(path_segment)]
        if dir == 'L':
            current_node = graph[current_node][0]
        else:
            current_node = graph[current_node][1]
        steps += 1
    print(steps)


def part_two():
    file = open("inputs/tylerinput.txt")
    file_lines = [line.removesuffix('\n') for line in file]
    path_segment = file_lines[0]

    start_nodes = []
    loop_lengths = []
    graph = {}
    for i in range(2, len(file_lines)):
        line = file_lines[i]
        src_node = line.split(" = ")[0]
        neighbors = line.split(" = ")[1][1:-1].split(', ')
        graph[src_node] = neighbors
        if src_node[-1] == 'A':
            start_nodes.append(src_node)
            loop_lengths.append(0)

    for i, start in enumerate(start_nodes):
        current_node = start
        steps = 0
        while current_node[-1] != 'Z':  # Keep going till we found an end for this path
            direction = path_segment[steps % len(path_segment)]
            steps += 1
            if direction == 'L':
                current_node = graph[current_node][0]
            else:
                current_node = graph[current_node][1]
        # Based on observation, we guess that it will take this many steps
        # to loop back around. This assumes that it won't run into another
        # valid ending before that time. We can't prove this, and it isn't
        # guaranteed, but it seems to be the case for this problem.
        # If it works, it works. :D
        loop_lengths[i] = steps

    min_required_steps = 1
    for length in loop_lengths:
        min_required_steps = min_required_steps * length // math.gcd(min_required_steps, length)
    print(min_required_steps)


if __name__ == "__main__":
    # part_one()
    part_two()
