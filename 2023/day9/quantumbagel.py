def difference_of(int_list):
    return_list = []
    for ind, i in enumerate(int_list[1:]):
        return_list.append(i-int_list[ind])
    return return_list


def part_1():
    sum_of_things = 0
    for line in open('inputs/quantumbagelinput.txt'):
        nums = [int(i) for i in line.replace('\n', '').split()]
        cascade = []
        while True:
            cascade.append(nums)
            nums = difference_of(nums)
            done = True
            for i in nums:
                if i != 0:
                    done = False
                    break
            if not done:
                continue
            break
        cascade = cascade[::-1]
        start_add = 0
        for item in cascade:
            item.append(item[-1] + start_add)
            start_add = item[-1]
        sum_of_things += cascade[-1][-1]
    print(sum_of_things)
def part_2():
    sum_of_things = 0
    for line in open('inputs/quantumbagelinput.txt'):
        nums = [int(i) for i in line.replace('\n', '').split()]
        cascade = []
        while True:
            cascade.append(nums)
            nums = difference_of(nums)
            done = True
            for i in nums:
                if i != 0:
                    done = False
                    break
            if not done:
                continue
            break
        cascade = cascade[::-1]
        start_add = 0
        for item in cascade:
            item.insert(0, item[0] - start_add)
            start_add = item[0]
        sum_of_things += cascade[-1][0]
    print(sum_of_things)


part_1()
part_2()
