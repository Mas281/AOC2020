with open("input.txt") as file:
    lines = file.read().splitlines()

p1_cards = [int(x) for x in lines[1:lines.index("")]]
p2_cards = [int(x) for x in lines[lines.index("Player 2:")+1:]]

def find_score(cards):
    return sum([cards[i] * (len(cards) - i) for i in range(len(cards))])

def find_winner_score():
    while True:
        p1_num = p1_cards.pop(0)
        p2_num = p2_cards.pop(0)

        if p1_num > p2_num:
            p1_cards.append(p1_num)
            p1_cards.append(p2_num)

            if len(p2_cards) == 0:
                print(find_score(p1_cards))
                return
        else:
            p2_cards.append(p2_num)
            p2_cards.append(p1_num)

            if len(p1_cards) == 0:
                print(find_score(p2_cards))
                return

find_winner_score()
