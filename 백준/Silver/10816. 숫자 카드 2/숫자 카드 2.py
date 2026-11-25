# 상근이가 들고 있는 숫자 카드 N
N = int(input())

# 상근이의 패
cards = sorted(list(map(int, input().split())))
card_keys = set(cards)

card_dict = {key : 0 for key in card_keys}
for card in cards:
    card_dict[card] += 1

# 상근아 몇 개 들고있어?
M = int(input())

card_count = map(int, input().split())
for card in card_count:
    if card in card_dict.keys():
        print(card_dict.get(card), end=" ")
    else:
        print(0, end=" ")