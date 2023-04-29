"""
A very simple rock paper, scissors game to get 
familiar with the basics of python3 
"""
#inport random lib, to set up computer use 
import random 
#function that uses a list and a dictionary to hold places choices
#as well as error hanld extra spaces and upper case letters
def getChoices():
    playerChoice = input("Enter a choice (rock, paper, scissors): ") 
    playerChoice = playerChoice.replace(".", "")
    playerChoice = playerChoice.replace(" ","")
    playerChoice=playerChoice.lower()
    options = ["rock", "paper", "scissors"] 
    compChoice = random.choice(options)
    choices = {"Player": playerChoice, "Computer": compChoice}
    return choices
#function that checks for wining condition, using nested if, elif, and else staments
def checkWin(player, computer):
    print(f"You chose {player} and computer chose {computer}")
    if player == computer:
        return "Its a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You Won"
        else:
            return "Paper covers rock! You lose"
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock! You Won!"
        else:
            return "Scissors cut paper, you lose!"  
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut paper! You Won!"
        else:
            return "Rock smashes Scissors, you lose!"

#call functions for choice and get result, then display result
choices = getChoices()
result = checkWin(choices["Player"], choices["Computer"])
print(result)
