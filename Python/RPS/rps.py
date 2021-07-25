# Rock Paper Scissors
from random import randint

ComputerOptions = ["Rock", "Paper", "Scissors"]
ComputerChoice = ComputerOptions[randint(0, 2)]
UserChoice = str(input("Rock, Paper Or Scissors: "))

if UserChoice == ComputerChoice:
    print("Cancelled Out")
else:
    if UserChoice == "Rock":
        if ComputerChoice == "Paper":
            print("Paper beats rock. Computer Won!")
        elif ComputerChoice == "Scissors":
            print("Rock beats scissors. You win!")
        else:
            print("Option not recognized. Please try again")
    elif UserChoice == "Paper":
        if ComputerChoice == "Rock":
            print("Paper beats rock. You Won!")
        elif ComputerChoice == "Scissors":
            print("Scissors beats paper. Computer Won!")
    elif UserChoice == "Scissors":
        if ComputerChoice == "Paper":
            print("Scissors beats paper. You win!")
        elif ComputerChoice == "Rock":
            print("Rock beats scissors. Computer Won!")

# Tells user game has ended
print("Thanks for playing!")
