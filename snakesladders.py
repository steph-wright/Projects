import random 

class Player:
    def __init__ (self, name, place):
        self.name = name
        self.place = place
    
    def name_get(self, str):
        self.name = str
    
    def roll_dice(self):
        roll = random.randrange(1, 6)
        self.place += roll
        return roll
    
    def place_is(self):
        return self.place


# generate players
num_players = int(input("How many players? "))
players = []
for n in range(num_players):
    print("Player" + str(n + 1) + ", enter your name:")
    n = Player("name", 1)
    n.name_get(input())
    players.append(n)

# generate snakeladders
sample = random.sample([n for n in range(2,100)], 24)

# the game 
maxscore = 0 
while maxscore < 100:
    for player in players:
        print(player.name + ", roll the dice by pressing enter.")
        input()
        dice_roll = player.roll_dice()
        print(player.name + " rolled a " + str(dice_roll) + "!")
        # check if player has won
        if player.place_is() >= 100:
            maxscore = player.place_is()
            print(player.name + " has won the game!")
            break
        # check if player has landed on a snakeladder
        check = player.place_is()
        if check in sample:
            check_index = sample.index(check)
            if check_index in range(1, 24, 2):
                player.place = sample[check_index - 1]
                if check > sample[check_index - 1]:
                    print(player.name + " has encountered a snake! " + player.name + " fell to " + str(player.place) + ".")
                else:
                    print(player.name + " found a ladder! " + player.name + " climbed to " + str(player.place) + "!")
        print(player.name + " is at space " + str(player.place) + ".")
        print(" ")

