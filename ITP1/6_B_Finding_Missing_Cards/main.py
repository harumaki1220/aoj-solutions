SUITS_ORDER = ['S', 'H', 'C', 'D']

SUIT_TO_INDEX = {'S': 0, 'H': 1, 'C': 2, 'D': 3}

all_cards = [[False for rank in range(14)] for suit in range(4)]

n = int(input())

for _ in range(n):
    suit_char, rank_str = input().split()
    rank = int(rank_str)
    suit_index = SUIT_TO_INDEX[suit_char]
    all_cards[suit_index][rank] = True

for suit_index in range(4):
    for rank in range(1, 14):
        if not all_cards[suit_index][rank]:
            suit_char = SUITS_ORDER[suit_index]
            print(f"{suit_char} {rank}")