import random

choices = ["rock","paper","scissors"]

computer = random.choice(choices)

player = None
while player not in choices:
    player = input("rock,paper or scissors?: ").lower()
if player == computer:
    print("computer: ",computer)
    print("player: ",player)
    print("tie!")

elif player == "rock":
    if computer == "paper":

        print("computer: ", computer)
        print("player: ", player)
        print("player lose")
    if computer == "scissors":

        print("computer: ", computer)
        print("player: ", player)
        print("player win")