with open("input.txt") as file:
    lines = file.read().splitlines()

p1_cards = [int(x) for x in lines[1:lines.index("")]]
p2_cards = [int(x) for x in lines[lines.index("Player 2:") + 1:]]

def find_score(cards):
    return sum([cards[i] * (len(cards) - i) for i in range(len(cards))])

def find_winner_score(p1, p2):
    while True:
        p1_num = p1.pop(0)
        p2_num = p2.pop(0)

        if p1_num > p2_num:
            p1.append(p1_num)
            p1.append(p2_num)

            if len(p2) == 0:
                print(find_score(p1))
                return
        else:
            p2.append(p2_num)
            p2.append(p1_num)

            if len(p1) == 0:
                print(find_score(p2))
                return

def determine_recursive_winner(p1, p2):
    states = []

    while True:
        if (p1, p2) in states:
            return 1
        states.append((p1.copy(), p2.copy()))

        p1_num = p1.pop(0)
        p2_num = p2.pop(0)

        if len(p1) >= p1_num and len(p2) >= p2_num:
            winner = determine_recursive_winner(p1[:p1_num], p2[:p2_num])
        else:
            winner = 1 if p1_num > p2_num else 2

        if winner == 1:
            p1.append(p1_num)
            p1.append(p2_num)

            if len(p2) == 0:
                return 1
        else:
            p2.append(p2_num)
            p2.append(p1_num)

            if len(p1) == 0:
                return 2
    
find_winner_score(p1_cards.copy(), p2_cards.copy())

w = determine_recursive_winner(p1_cards, p2_cards)
print(find_score(p1_cards) if w == 1 else find_score(p2_cards))
