# Ludo Dice Program

## Overview
This program simulates rolling a dice for the popular game of Ludo. It generates a random number between 1 and 6, mimicking the behavior of a physical dice. The program is simple and serves as a great starting point for beginners learning Python.

## Features
- Generates a random number between 1 and 6.
- Displays the result to the user in a friendly message.

## How It Works
1. The program imports the `random` module to generate random numbers.
2. It uses the `random.randint()` function to select a random integer between 1 and 6 (inclusive).
3. The result is printed to the console with a welcoming message.

## Code Explanation
```python
#importing random module so that we can select numbers randomly
import random

print("Welcome to ludo game !")

random_nbr = random.randint(1, 6)
'''randint is used to select number from the starting range till ending range
you can also use random_nbr = random.randrange(1,7) to get the above thing here we write 7
because the randrange exclusive the ending number'''

print("Hey! you have got a", random_nbr, "number dice.")
```

### Key Points
- **`random.randint(1, 6)`**: Generates a random integer between 1 and 6, inclusive.
- **Alternative**: You can use `random.randrange(1, 7)` to achieve the same result. Note that `randrange` excludes the ending number.
- **Print Statement**: The result is displayed in a user-friendly message.

## How to Run
1. Ensure you have Python installed on your system.
2. Copy the code into a Python file, e.g., `ludo_dice.py`.
3. Run the file using the command:
   ```bash
   python ludo_dice.py
   ```
4. Follow the instructions and view the random dice roll output.

## Example Output
```
Welcome to ludo game !
Hey! you have got a 4 number dice.
```

## Future Enhancements
- Add functionality to simulate rolling multiple dice.
- Allow users to roll the dice multiple times in a single run.
- Include a graphical representation of the dice result.

---

Enjoy playing with your virtual Ludo dice! Feel free to modify and enhance the code to suit your needs.

