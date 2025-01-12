# Guess the Number Game

## Overview
This project is a simple "Guess the Number" game implemented in Python. The program selects a random number between 0 and 10, and the user tries to guess it. The program provides hints to guide the user until they guess the number correctly.

## Features
- Random number generation using Python's `random` module.
- User-friendly hints to indicate if the guess is too high or too low.
- A congratulatory message when the user guesses the correct number.

## How It Works
1. The program imports the `random` module.
2. It uses `random.randrange(0, 11)` to generate a random number between 0 and 10 (excluding 11 because of rangrange).
3. The user is prompted to guess the number.
4. A `while` loop checks the user's guess and provides feedback until the correct number is guessed.

## Code Explanation
```python
#importing random module so that we can select numbers randomly
import random

print("Welcome to guess game!")

random_nbr = random.randrange(0, 11)
'''randrange is used to select number from the starting range till ending range (excluding end).'''

print("Guess my number! (hint : between 0 and 10)")
user_nbr = int(input("Enter your guess: "))

while user_nbr != random_nbr:  # Our loop will run until the user guesses it correctly.
    if user_nbr > random_nbr:
        print("My number is below your guess!")
    else:
        print("My number is above your guess!")
    user_nbr = int(input("Enter your guess: "))
else:
    print("Congrats! You guessed it right, my number is", random_nbr)
```

### Key Points
- **`random.randrange(0, 11)`**: Generates a random integer between 0 and 10 (inclusive).
- **Hints**: If the guessed number is higher than the actual number, the program hints that the number is lower, and vice versa.
- **`while` Loop**: Ensures the program continues until the correct number is guessed.

## How to Run
1. Ensure you have Python installed on your system.
2. Copy the code into a Python file, e.g., `guess_game.py`.
3. Run the file using the command:
   ```bash
   python guess_game.py
   ```
4. Follow the prompts to play the game.

## Example Output
```
Welcome to guess game!
Guess my number! (hint : between 0 and 10)
Enter your guess: 5
My number is below your guess!
Enter your guess: 2
My number is above your guess!
Enter your guess: 3
Congrats! You guessed it right, my number is 3
```

## Future Enhancements
- Add an option to limit the number of guesses.
- Implement difficulty levels with different ranges (e.g., 0-50 for hard mode).
- Provide the option to play multiple rounds.
---

Enjoy playing "Guess the Number"! Feel free to modify and improve the code to add your own twists to the game.

