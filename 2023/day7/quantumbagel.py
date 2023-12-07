
# hands:
# five oak = 6
# four oak = 5
# full house = 4
# three oak = 3
# two pair = 2
# one pair = 1
# high card = 0


def classify_hand(hand: str):
    if hand.count(hand[0]) == 5:
        return 6
    hand_count_d = {}
    for item in hand:
        if item in hand_count_d.keys():
            hand_count_d[item] += 1
        else:
            hand_count_d[item] = 1
    if max(hand_count_d.values()) == 4:
        return 5
    if len(hand_count_d) == 2:
        return 4
    if len(hand_count_d) == 3 and max(hand_count_d.values()) == 3:
        return 3
    if len(hand_count_d) == 3 and min(hand_count_d.values()) == 1:
        return 2
    if len(hand_count_d) == 4:
        return 1
    return 0
def part_1():
    def decision(char1: str, char2: str):
        """
        :param char1:
        :param char2:
        :return: 0 if equal, 1 if char1, 2 if char2
        """
        transform = {"T": "10", "J": "11", "Q": "12", "K": "13", "A": '14'}
        if char1 in transform.keys():
            char1 = transform[char1]
        if char2 in transform.keys():
            char2 = transform[char2]
        if int(char1) > int(char2):
            return 1
        if int(char1) < int(char2):
            return 2
        return 0


    def rank_same_level(hands: list[str]):
        ranked = [hands[0]]
        for hand in hands[1:]:
            hand_done = False
            added = False
            for i, h in enumerate(ranked):
                for index, c in enumerate(hand):
                    choice = decision(c, h[index])
                    if not choice:  # equal, so keep going
                        continue
                    elif choice == 1:  # hand we are parsing is *better*, so insert directly before
                        ranked.insert(i, hand)
                        added = True
                        hand_done = True
                        break
                    else:  # hand already there is better,
                        break
                if hand_done:
                    break
            if not added:
                ranked.insert(len(ranked), hand)  # the worst hand
        return ranked


    lines = [i.removesuffix('\n') for i in open('inputs/quantumbagelinput.txt').readlines()]
    categorized = {}
    conversion = {}
    for line in lines:
        line = line.split()
        line[1] = int(line[1])
        conversion.update({line[0]: line[1]})
        hand_rank = classify_hand(line[0])
        if hand_rank in categorized.keys():
            categorized[hand_rank].update({line[0]: line[1]})
        else:
            categorized[hand_rank] = {line[0]: line[1]}

    total_winnings = 0
    place = 1
    for item in sorted(categorized.keys()):
        val = categorized[item]
        ranked = rank_same_level(list(val.keys()))[::-1]  # reverse list because I'm lazy
        for hand in ranked:
            total_winnings += place * conversion[hand]
            place += 1


    print(total_winnings)


def part_2():
    def classify_hand_part2(hand: str):
        if "J" not in hand:
            return classify_hand(hand)
        else:
            chars = "TQKA98765432"
            new_hand = hand[:]
            highest = 0
            for thing in chars:
                sc = classify_hand_part2(new_hand.replace("J", thing))
                if sc > highest:
                    highest = sc
            return highest
    def decision(char1: str, char2: str):
        """
        :param char1:
        :param char2:
        :return: 0 if equal, 1 if char1, 2 if char2
        """
        transform = {"T": "10", "J": "1", "Q": "12", "K": "13", "A": '14'}
        if char1 in transform.keys():
            char1 = transform[char1]
        if char2 in transform.keys():
            char2 = transform[char2]
        if int(char1) > int(char2):
            return 1
        if int(char1) < int(char2):
            return 2
        return 0

    def rank_same_level(hands: list[str]):
        ranked = [hands[0]]
        for hand in hands[1:]:
            hand_done = False
            added = False
            for i, h in enumerate(ranked):
                for index, c in enumerate(hand):
                    choice = decision(c, h[index])
                    if not choice:  # equal, so keep going
                        continue
                    elif choice == 1:  # hand we are parsing is *better*, so insert directly before
                        ranked.insert(i, hand)
                        added = True
                        hand_done = True
                        break
                    else:  # hand already there is better,
                        break
                if hand_done:
                    break
            if not added:
                ranked.insert(len(ranked), hand)  # the worst hand
        return ranked

    lines = [i.removesuffix('\n') for i in open('inputs/quantumbagelinput.txt').readlines()]
    categorized = {}
    conversion = {}
    for line in lines:
        line = line.split()
        line[1] = int(line[1])
        conversion.update({line[0]: line[1]})
        hand_rank = classify_hand_part2(line[0])
        if hand_rank in categorized.keys():
            categorized[hand_rank].update({line[0]: line[1]})
        else:
            categorized[hand_rank] = {line[0]: line[1]}

    total_winnings = 0
    place = 1
    for item in sorted(categorized.keys()):
        val = categorized[item]
        ranked = rank_same_level(list(val.keys()))[::-1]  # reverse list because I'm lazy
        for hand in ranked:
            total_winnings += place * conversion[hand]
            place += 1

    print(total_winnings)


# part_1()
part_2()
