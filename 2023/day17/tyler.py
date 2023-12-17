class Block:
    def __init__(self, x, y, dir, straight_cnt, parent):
        self.x = x
        self.y = y
        self.straight_cnt = straight_cnt
        self.dir = dir
        self.parent = parent

    def __eq__(self, other):
        if other is not Block:
            return False
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "(" + str(self.x) + " ," + str(self.y) + ")"

def part_one():
    file = open("input.txt")
    layout = [[int(char) for char in line.removesuffix('\n')] for line in file]


def part_two():
    file = open("input.txt")


if __name__ == "__main__":
    part_one()
    # part_two()
