import random

# create deck
card_matrix = [list(range(1, 14)) for i in range(4)]
suits = [0, 1, 2, 3]

def card_draw():
    # draw card from deck and remove it, and return card
    draw_suit = random.choice(suits)
    card = random.choice(card_matrix[draw_suit])
    card_matrix[draw_suit].remove(card)
    if len(card_matrix[draw_suit]) == 0:
        suits.remove(draw_suit)
    return card

def card_announce(num):
    if num == 1:
        print("Ace! Waterfall!")
    elif num == 2:
        print("Two is for you!")
    elif num == 3: 
        print("Three is for me!")
    elif num == 4:
        print("Four is whores!")
    elif num == 5:
        print("Five! Thumb master!")
    elif num == 6:
        print("Six is dicks!")
    elif num == 7:
        print("Seven! Heaven!")
    elif num == 8:
        print("Eight! Mate!")
    elif num == 9:
        print("Nine! Rhyme!")
    elif num == 10:
        print("Ten! Categories!")
    elif num == 11:
        print("Jack! Make a rule!")
    elif num == 12:
        print("Queen! Question master!")
    elif num == 13 and 13 in card_matrix[0] or ( 13 in card_matrix[1] or 13 in card_matrix[2] or 13 in card_matrix[3] ):
        print("King! Fill the King's cup!")
    else: 
        print("King! Drink the King's cup!")
    print(" ")

num_players = int(input("How many players? "))

name_list = []
for n in range(num_players):
    print("Player" + str(n) + ", enter your name:")
    name_list.append(input())

turns = 0
while turns < 52:
    for n in range(num_players):
        print(str(name_list[n]) + ", take a card by pressing enter.")
        input()
        card_drawn = card_draw()
        card_announce(card_drawn)
        turns += 1
        if turns == 52:
            print("No more cards. End of game.")
            break