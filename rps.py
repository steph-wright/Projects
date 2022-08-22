import random
from secrets import choice

fighters = ["rock", "paper", "scissors"]
user_score = 0
comp_score = 0

def round():
    x = input("Type 'rock', 'paper', or 'scissors' here, then press enter: ")
    y = random.choice(fighters)

    rock = "Computer chose rock! "
    paper = "Computer chose paper! "
    scissors = "Computer chose scissors! "
    win = "You win this round!"
    lose = "You lose this round."

    if x != "rock" and x != "paper" and x != "scissors":
        print("Sorry, you spelled something wrong, try again.")
    if x == y:
        print("You both chose " + str(x) + ". Tie!")
        return "tie"
    else:
        if x == "rock":
            if y == "paper":
                print(paper + lose)
                return "lose"
            else:
                print(scissors + win)
                return "win"
        elif x == "paper":
            if y == "rock":
                print(rock + win)
                return "lose"
            else: 
                print(scissors + lose)
                return "lose"
        else:
            if y == "rock":
                print(rock + lose)
                return "lose"
            else:
                print(paper + win)
                return "win"


while True:   
    gametype = input("Choose |VERSION 1: FIRST TO| by entering f, or |VERSION 2: BEST OF| by entering b: ")
    if gametype == "f":
        print("First to version selected.")
        # first to version
        max_score = int(input("First to how many points? "))

        while user_score < max_score and comp_score < max_score:
            result = round()
            if result == "win":
                user_score += 1
            elif result == "lose":
                comp_score += 1
            else: 
                continue


        if user_score == max_score:
            print("User wins the game!")
            break
        else:
            print("Computer wins the game!")
            break

    elif gametype == "b":
        print("Best of version selected.")
        # best of version
        max_rounds = int(input("Best of how many rounds? "))
        rounds = 0

        while rounds < max_rounds:
            result = round()
            rounds += 1
            if result == "win":
                user_score += 1
            elif result == "lose":
                comp_score += 1
            else: 
                continue

        if user_score > comp_score:
            print("User wins the game!")
            break
        elif comp_score > user_score:
            print("Computer wins the game!")
            break
        else: 
            print("User and computer tie!")
            break
    else: 
        print("Incorrect character entered. Try again.")




