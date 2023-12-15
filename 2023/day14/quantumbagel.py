import copy
import time

starting_map = []

for line in open("inputs/quantumbagelinput.txt"):
    t_map = []
    for char in line:
        if char == ".":
            t_map.append(0)
        elif char == "O":
            t_map.append(1)
        elif char == "#":
            t_map.append(2)
    starting_map.append(t_map)


new_map = starting_map[:]


def get_ahead_north(row, col, m):
    low_r = row
    for r in range(row-1, -1, -1):
        if m[r][col] == 0:
            low_r = r
            continue
        else:
            break
    return low_r, col


def get_ahead_west(row, col, m):
    low_c = col
    for c in range(col-1, -1, -1):
        if m[row][c] == 0:
            low_c = c
            continue
        else:
            break
    return row, low_c


def p_map(m):
    d = {0: ".", 1: "O", 2: "#"}
    for l in m:
        for c in l:
            print(d[c], end='')
        print()


def score(m):
    cnt = len(m)
    answer = 0
    for line in m:
        answer += line.count(1) * cnt
        cnt -= 1
    return answer


def part_1():
    for ro, line in enumerate(starting_map):
        for co, char in enumerate(line):
            if char == 1:
                nr, nc = get_ahead_north(ro, co, new_map)
                if nr != ro or nc != co:
                    new_map[nr][nc] = 1
                    new_map[ro][co] = 0

    print(score(new_map))


def encode_map(m):
    d = {0: ".", 1: "O", 2: "#"}
    return ''.join([''.join([d[j] for j in i]) for i in m])


def part_2():
    global new_map
    occurred_states = {}
    iteration = 0
    to_watch = None
    first_hit = None
    while True:
        trgd = False
        if encode_map(new_map) not in occurred_states:
            occurred_states.update({encode_map(new_map): iteration})
        elif to_watch is None:
            to_watch = encode_map(new_map[:])
            trgd = True
        if to_watch is not None and encode_map(new_map) == to_watch and not trgd:
            for i in range((1000000000-iteration) % (iteration - occurred_states[to_watch])):
                new_map = run_cycle(new_map)
            print(score(new_map))
            break
        new_map = run_cycle(new_map)
        iteration += 1


def run_cycle(m):
    current_action = 0
    actions = [get_ahead_north, get_ahead_west, get_ahead_north, get_ahead_west]
    for _ in range(4):
        if current_action == 2:  # south
            m = m[::-1]
        if current_action == 3:  # east
            m = [i[::-1] for i in m]
        b_map = copy.copy(m)
        while True:
            for ro, line in enumerate(b_map):
                for co, char in enumerate(line):
                    if char == 1:
                        nr, nc = actions[current_action](ro, co, m)
                        if nr != ro or nc != co:
                            m[nr][nc] = 1
                            m[ro][co] = 0
            if b_map == m:
                break
            else:
                b_map = m[:]
        if current_action == 2:
            m = m[::-1]
        if current_action == 3:  # east
            m = [i[::-1] for i in m]
        current_action += 1
    return m

t = time.time()
part_2()
print(time.time()-t)
