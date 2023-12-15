import pprint

horiz_maps = []
vert_maps = []
temp_map = []
for line in open('inputs/quantumbagelinput.txt'):
    line = line.replace('\n', '')
    if not line:
        horiz_maps.append(temp_map)
        temp_map = []
    else:
        temp_map.append(line)
horiz_maps.append(temp_map)
for mp in range(len(horiz_maps)):
    vert_map = []
    for i in range(len(horiz_maps[mp][0])):
        vert_map.append(''.join([j[i] for j in horiz_maps[mp]]))
    vert_maps.append(vert_map)
hits = [0, 0]
maps = [horiz_maps, vert_maps]
for s_to in range(2):
    for nm, check_map in enumerate(maps[s_to]):
        check_ind = []
        for ind, item in enumerate(check_map):
            try:
                if item == check_map[ind+1]:
                    check_ind.append(ind)
                    continue
            except IndexError:
                break
        if not len(check_ind):
            continue
        pprint.pprint(check_map)
        for indice in check_ind:
            bottom = indice
            top = indice+1
            while True:
                bottom -= 1
                top += 1
                if bottom < 0 or top >= len(check_map):
                    hits[s_to] += indice + 1
                    break
                if check_map[bottom] != check_map[top]:
                    break



