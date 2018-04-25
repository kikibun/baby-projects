from random import randint

comp_choice = randint(1,3)

def comp_turn(comp_choice):
    if comp_choice == 1:
        rps = "rock"
    elif comp_choice == 2:
        rps = "paper"
    elif comp_choice == 3:
        rps = "scissors"
    return rps

player_choice = raw_input("rock, paper, or scissors?: ")

def rps_game(player_choice, comp_choice):
    if comp_choice == 1:
        if player_choice == "rock":
            print "You tied!"
        elif player_choice == "paper":
            print "You win!"
        elif player_choice == "scissors":
            print "You lose!"
        else:
            print "Choose one of the options!"
    if comp_choice == 2:
        if player_choice == "rock":
            print "You lose!"
        elif player_choice == "paper":
            print "You tied!"
        elif player_choice == "scissors":
            print "You win!"
        else:
            print "Choose one of the options!"
    if comp_choice == 3:
        if player_choice == "rock":
            print "You win!"
        elif player_choice == "paper":
            print "You lose!"
        elif player_choice == "scissors":
            print "You tied!"
        else:
            print "Choose one of the options!"

print "the player chose",player_choice
print "the computer chose",comp_turn(comp_choice)
rps_game(player_choice, comp_choice)
