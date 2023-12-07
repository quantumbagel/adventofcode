from functools import cmp_to_key

p1_letter_card_values = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
p2_letter_card_values = {"J": 1, "T": 10, "Q": 11, "K": 12, "A": 13}
def compare_hands(letter_card_values: dict[str, int], hand1: str, hand2: str) -> int:
    """
    Returns positive if hand1 ranks higher than hand2 in Camel Cards.
    Assumes both hands are of the same type.
    :param letter_card_values:
    :param hand1:
    :param hand2:
    :return:
    """
    for i in range(len(hand1)):
        card_1_value = hand1[i]
        card_2_value = hand2[i]

        if card_1_value in letter_card_values:
            card_1_value = letter_card_values[card_1_value]
        else:
            card_1_value = int(card_1_value)

        if card_2_value in letter_card_values:
            card_2_value = letter_card_values[card_2_value]
        else:
            card_2_value = int(card_2_value)

        comparison = card_1_value - card_2_value
        if comparison != 0:
            return comparison
    return 0


def insert_hand_bid_pair(letter_card_values: dict[str, int], hand_list: list, pair: (str, int)):
    if len(hand_list) == 0:
        hand_list.append(pair)
        return

    low = 0
    high = len(hand_list) - 1
    while low < high:
        mid = (low + high) // 2
        compare_to = hand_list[mid][0]
        comparison = compare_hands(letter_card_values, pair[0], compare_to)
        if comparison > 0:
            high = mid - 1
            continue
        if comparison < 0:
            low = mid + 1
            continue
        hand_list.insert(mid, pair)  # If we get here, the hands are equal so it doesn't matter
        return
    if compare_hands(letter_card_values, pair[0], hand_list[low][0]) > 0:
        hand_list.insert(low, pair)
    else:
        hand_list.insert(low + 1, pair)


def part_one():
    file = open("inputs/tylerinput.txt")
    hand_rankings = [[], [], [], [], [], [], []]

    for line in file:
        line = line.removesuffix('\n')
        hand = line.split()[0]
        bid = int(line.split()[1])

        counts = {}
        for char in hand:
            if char not in counts:
                counts[char] = 1
                continue
            counts[char] += 1

        counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        hand_type = -1
        if counts[0][1] == 5:
            hand_type = 0
        elif counts[0][1] == 4:
            hand_type = 1
        elif counts[0][1] == 3:
            if counts[1][1] == 2:
                hand_type = 2
            else:
                hand_type = 3
        elif counts[0][1] == 2:
            if counts[1][1] == 2:
                hand_type = 4
            else:
                hand_type = 5
        else:
            hand_type = 6
        insert_hand_bid_pair(p1_letter_card_values, hand_rankings[hand_type], (hand, bid))

    # Ranking is done, calculate points
    rank = 0
    winnings = 0
    for hand_type in reversed(hand_rankings):
        for hand_bid_pair in reversed(hand_type):
            rank += 1
            winnings += rank * hand_bid_pair[1]
    print(winnings)


def part_two():
    file = open("inputs/tylerinput.txt")
    hand_rankings = [[], [], [], [], [], [], []]

    for line in file:
        line = line.removesuffix('\n')
        hand = line.split()[0]
        bid = int(line.split()[1])

        counts = {}
        J_count = 0
        for char in hand:
            if char == 'J':
                J_count += 1
                continue
            if char not in counts:
                counts[char] = 1
                continue
            counts[char] += 1
        counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        if len(counts) == 0:
            counts.append(('J', 5))
        else:
            counts[0] = counts[0][0], counts[0][1] + J_count

        hand_type = -1
        if counts[0][1] == 5:
            hand_type = 0
        elif counts[0][1] == 4:
            hand_type = 1
        elif counts[0][1] == 3:
            if counts[1][1] == 2:
                hand_type = 2
            else:
                hand_type = 3
        elif counts[0][1] == 2:
            if counts[1][1] == 2:
                hand_type = 4
            else:
                hand_type = 5
        else:
            hand_type = 6
        insert_hand_bid_pair(p2_letter_card_values, hand_rankings[hand_type], (hand, bid))

    # Ranking is done, calculate points
    rank = 0
    winnings = 0
    for hand_type in reversed(hand_rankings):
        for hand_bid_pair in reversed(hand_type):
            rank += 1
            winnings += rank * hand_bid_pair[1]
    print(winnings)


if __name__ == "__main__":
    # part_one()
    part_two()
