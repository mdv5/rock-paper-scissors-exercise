# game.py

print("Rock, Paper, Scissors, Shoot!")

player_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

print("Player chose: ", player_choice)

# Validate user input
if (player_choice == "rock") or (player_choice == "paper") or (player_choice == "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
    exit()

print("THIS IS THE END OF THE GAME. PLEASE PLAY AGAIN.")
