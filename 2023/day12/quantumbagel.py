part_answer = 0


def process(line, counts):
    global part_answer
    if "?" not in line:
        if counts == [x.count('#') for x in line.split(".") if x]:
            part_answer += 1
    else:
        process(line.replace("?", ".", 1), counts)
        process(line.replace("?", '#', 1), counts)


def part_1():  # very unoptimized lol
    for spring_line in open('inputs/quantumbagelinput.txt'):
        spring = spring_line.split()[0]
        counts = [int(j) for j in spring_line.split()[1].split(",")]
        process(spring, counts)


def get_clusters(springs):
    return [s for s in springs.split('.') if s]


def count_placements(counts, clusters, cache):
    key = "|".join(map(str, counts))
    key += "#" + ":".join(clusters)
    if key in cache:
        return cache[key]

    if not counts:
        for cluster in clusters:
            if "#" in cluster:
                return 0
        return 1

    if not clusters:
        return 0

    placements = 0
    count = counts[0]
    cluster = clusters[0]
    len_cluster = len(cluster)

    if count > len_cluster and "#" in cluster:
        return 0

    for i in range(len_cluster - count + 1):
        left = cluster[:i]

        if "#" in left:
            break

        right = cluster[i + count:]

        if right.startswith("#"):
            continue

        new_clusters = clusters[1:]
        if len(right) > 1:
            new_clusters.insert(0, right[1:])
        placements += count_placements(counts[1:], new_clusters, cache)

    if "#" not in cluster:
        placements += count_placements(counts, clusters[1:], cache)

    cache[key] = placements
    return placements


def part_2():
    total = 0
    for cr, spring_line in enumerate(open('input.txt')):
        spring = ((spring_line.split()[0] + "?") * 5)[:-1]
        counts = [int(j) for j in spring_line.split()[1].split(",")*5]
        clusters = get_clusters(spring)
        total += count_placements(counts, clusters, {})
    print(total)


part_2()
