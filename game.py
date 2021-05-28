# game.py

import random # loads the random module
import os
from dotenv import load_dotenv

load_dotenv()

print("Rock, Paper, Scissors, Shoot!")
print("----------------------")

#capture player name
player_name = os.getenv('PLAYER_NAME')
print ("Hi ",player_name,". Welcome to my game.")

#prompt user to enter a choice and capture their input
player_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")
print("----------------------")
print("Player chose: ", player_choice)
# validate user input
if (player_choice == "rock") or (player_choice == "paper") or (player_choice == "scissors"):
    message = "Choice received successfully."
else:
    print("OOPS, invalid input. Please try again.")
    exit()

# list of valid choices
valid_choices = ["rock","paper","scissors"]

computer_choice = random.choice(valid_choices)
print("Computer chose: ", computer_choice)

winner = "" #set the winner to empty before evaluating the winner

#evaluate the winner
if (player_choice == "rock"):
    if (computer_choice == "scissors"):
        winner = player_name
    elif (computer_choice == "paper"):
        winner = 'the computer'
elif (player_choice == "scissors"):
    if (computer_choice == "paper"):
        winner = player_name
    elif (computer_choice == "rock"):
        winner = 'the computer'
elif (player_choice == "paper"):
    if (computer_choice == "scissors"):
        winner = 'the computer'
    elif (computer_choice == "rock"):
        winner = player_name

print("----------------------")
# if there is a winner say who won, otherwise declare a tie
if winner:
    print('The winner is', winner)
    print("----------------------")
    print("THIS IS THE END OF THE GAME. PLEASE PLAY AGAIN.")
else:
    print("The game is a tie! Please Play again.")
