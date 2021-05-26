# game.py

import random # loads the random module


print("Rock, Paper, Scissors, Shoot!")

#prompt user to enter a choice and capture their input
player_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

print("Player chose: ", player_choice)

# validate user input
if (player_choice == "rock") or (player_choice == "paper") or (player_choice == "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
    exit()

# list of valid choices
valid_choices = ["rock","paper","scissors"]

computer_choice = random.choice(valid_choices)

print("Computer chose: ", computer_choice)

print("THIS IS THE END OF THE GAME. PLEASE PLAY AGAIN.")
