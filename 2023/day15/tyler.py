def hash(s: str) -> int:
    ret = 0
    for char in s:
        ret += ord(char)
        ret *= 17
        ret %= 256
    return ret


def part_one():
    file = open("inputs/tylerinput.txt")
    total = 0
    for inst in file.readline().removesuffix('\n').split(','):
        total += hash(inst)
    print(total)


def part_two():
    file = open("inputs/tylerinput.txt")
    boxes = [{} for _ in range(256)]
    for inst in file.readline().removesuffix('\n').split(','):
        if '=' in inst:
            label = inst.split('=')[0]
            focal_length = int(inst.split('=')[1])
            box_num = hash(label)
            boxes[box_num][label] = focal_length
            continue

        label = inst.split('-')[0]
        box_num = hash(label)
        boxes[box_num].pop(label, None)

    total_power = 0
    for box_num, box in enumerate(boxes):
        slot = 0
        for label in box:
            slot += 1
            total_power += (box_num + 1) * slot * box[label]

    print(total_power)


if __name__ == "__main__":
    # part_one()
    part_two()
