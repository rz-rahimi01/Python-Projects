# Importing random module to select numbers randomly
import random

print("Welcome to the guessing game!")

# Generate a random number between 0 and 10 (inclusive)
secret_number = random.randint(0, 10)
'''randint is used here instead of randrange to make it clearer that both endpoints are included'''

print("Guess my number! (Hint: it's between 0 and 10)")

while True:
    try:
        user_guess = int(input("Enter your guess: "))
        
        if user_guess == secret_number:
            print(f"Congrats! You guessed it right. My number was {secret_number}!")
            break
        elif user_guess > secret_number:
            print("My number is lower than your guess!")
        else:
            print("My number is higher than your guess!")
            
    except ValueError:
        print("Please enter a valid number between 0 and 10.")
