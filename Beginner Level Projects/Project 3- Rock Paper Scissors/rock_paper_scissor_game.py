import random  # Importing random module for generating computer's choice

print("Welcome to the Rock-Paper-Scissors Game!")

while True:  # Main game loop
    pc_choice = random.randint(1, 3)  # Computer randomly chooses between 1 and 3

    # Prompt user for their choice
    user_choice = int(input("Enter Your Choice: \n1: Rock \n2: Scissor \n3: Paper \n"))

    # Validating user input to ensure it's between 1 and 3
    while user_choice > 3 or user_choice < 1:
        print("Invalid input! Please enter a valid number (1, 2, or 3).")
        user_choice = int(input("Enter Your Choice: \n1: Rock \n2: Scissor \n3: Paper \n"))

    # Determine the outcome of the game
    if pc_choice == 1:  # Computer chooses Rock
        if user_choice == 1:
            print("It's a draw! PC also chose Rock.")
        elif user_choice == 2:
            print("You lose! PC chose Rock and Rock beats Scissor.")
        else:
            print("You win! PC chose Rock and Paper beats Rock.")

    elif pc_choice == 2:  # Computer chooses Scissor
        if user_choice == 1:
            print("You win! PC chose Scissor and Rock beats Scissor.")
        elif user_choice == 2:
            print("It's a draw! PC also chose Scissor.")
        else:
            print("You lose! PC chose Scissor and Scissor beats Paper.")

    elif pc_choice == 3:  # Computer chooses Paper
        if user_choice == 1:
            print("You lose! PC chose Paper and Paper beats Rock.")
        elif user_choice == 2:
            print("You win! PC chose Paper and Scissor beats Paper.")
        else:
            print("It's a draw! PC also chose Paper.")

    # Ask user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thank you for playing Rock-Paper-Scissors! Goodbye!")
        break
