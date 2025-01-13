# Quiz Game

## Overview
This project is a simple **Quiz Game** implemented in Python. It asks the user a series of multiple-choice questions, evaluates their answers, and displays the final score. The game is designed to test basic computer science knowledge with questions about abbreviations.

## Features
- A dictionary-based structure to store questions and answers.
- Case-insensitive input handling for user answers.
- Immediate feedback on whether the user’s answer is correct.
- A final score summary displayed at the end.

## How to Run
1. Ensure Python is installed on your system.
2. Save the code in a file named `quiz_game.py`.
3. Run the file using:
   ```bash
   python quiz_game.py
   ```
4. Answer each question when prompted.

## Example Output
```
What is the full form of CPU?
Your answer: central processing unit
Correct!

What is the full form of RAM?
Your answer: random access memory
Correct!

What is the full form of ROM?
Your answer: read-only storage
Wrong! The correct answer is: read-only memory

You answered 2 out of 3 questions correctly.
```

## Customization
- You can add more questions to the `questions` dictionary by following the existing structure:
  ```python
  questions[6] = {"question": "Your question here", "answer": "correct answer here"}
  ```
- Modify the existing questions or answers to suit your needs.

## Future Enhancements
- Add a scoring system that assigns different weights to questions.
- Allow multiple-choice questions instead of free-text answers.
- Implement a timer for each question to increase difficulty.
- Display detailed statistics at the end (e.g., percentage of correct answers).

---

Enjoy the Quiz Game! Feel free to modify and enhance it as per your preferences.

