import random

print("Welcome to the Ludo game!")

while True:  # Loop to allow multiple rolls
    input("Press Enter to roll the dice...") # User presses enter to roll

    random_nbr = random.randint(1, 6)
    print(f"Hey! You rolled a {random_nbr} on the dice.")

    # Ask the user if they want to roll again
    play_again = input("Roll again? (yes/no): ").lower()
    if play_again != 'yes':
        break # Exit the loop if the user doesn't say 'yes'

print("Thanks for playing!")
