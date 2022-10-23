card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
dict_card = {'c': 0, 'd': 13, 'h': 26, 's': 39}
d_c = {0: 'c', 1: 'd', 2: 'h', 3: 's'}


def encode(cards):
    return sorted([card.index(x[0]) + dict_card[x[1]] for x in cards])


def decode(cards):
    cards.sort()
    return [card[x % 13] + d_c[x // 13] for x in cards]