import random

# create deck
card_matrix = [list(range(1, 14)) for i in range(4)]
suits = [0, 1, 2, 3]

# player class
class Player:
    def __init__ (self, no, name):
        self.no = no
        self.name = name
    
    def take_card(self):
        print(self.name + ", take a card by pressing enter.")
        input()
        draw_suit = random.choice(suits)
        card = random.choice(card_matrix[draw_suit])
        card_matrix[draw_suit].remove(card)
        if len(card_matrix[draw_suit]) == 0:
            suits.remove(draw_suit)
        return card
    
    def card_announce(self, num):
        print(self.name + " has taken a card!")
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

    def name_get(self, str):
        self.name = str

print("Welcome to Cardless King's Cup!")

num_players = int(input("How many players? "))

players = []

for n in range(num_players):
    print("Player" + str(n + 1) + ", enter your name:")
    n = Player(n, "name")
    n.name_get(input())
    players.append(n)

turns = 0
while turns < 52:
    for player in players:
        card_taken = player.take_card()
        player.card_announce(card_taken)
        turns += 1
        if turns == 52:
            print("No more cards. End of game.")
            break

