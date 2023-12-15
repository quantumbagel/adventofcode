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
    file = open("input.txt")


if __name__ == "__main__":
    part_one()
    # part_two()
