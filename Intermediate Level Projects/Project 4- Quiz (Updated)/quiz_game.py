import json
import os
import random
from datetime import datetime

QUESTIONS_FILE = "questions.json"
SCORES_FILE = "scores.json"

# Load questions
def load_questions():
    if not os.path.exists(QUESTIONS_FILE):
        # Default questions
        default_questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Berlin", "Madrid", "Paris", "Rome"],
                "answer": 3
            },
            {
                "question": "Which language is used for web apps?",
                "options": ["Python", "JavaScript", "C++", "Java"],
                "answer": 2
            },
            {
                "question": "What is 7 × 8?",
                "options": ["54", "56", "64", "72"],
                "answer": 2
            }
        ]
        with open(QUESTIONS_FILE, "w") as f:
            json.dump(default_questions, f, indent=4)
    with open(QUESTIONS_FILE, "r") as f:
        return json.load(f)

# Load scores
def load_scores():
    if not os.path.exists(SCORES_FILE):
        return []
    with open(SCORES_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# Save scores
def save_scores(scores):
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=4)

# Add a new score
def add_score(player, score):
    scores = load_scores()
    scores.append({
        "player": player,
        "score": score,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    scores.sort(key=lambda x: x["score"], reverse=True)
    save_scores(scores)

# Show leaderboard
def show_leaderboard():
    scores = load_scores()
    if not scores:
        print("\n🏆 No scores yet.")
        return
    print("\n===== LEADERBOARD =====")
    for i, entry in enumerate(scores[:10], start=1):
        print(f"{i}. {entry['player']} - {entry['score']} points on {entry['date']}")

# Play quiz
def play_quiz():
    player = input("\nEnter your name: ").strip()
    questions = load_questions()
    random.shuffle(questions)
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for i, opt in enumerate(q["options"], start=1):
            print(f"{i}. {opt}")

        try:
            answer = int(input("Your answer (1-4): "))
            if answer == q["answer"]:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer was {q['options'][q['answer'] - 1]}")
        except ValueError:
            print("❌ Invalid input. Moving on.")

    print(f"\n🎯 Quiz Over! Your Score: {score}")
    add_score(player, score)

# Menu
def main():
    while True:
        print("\n===== QUIZ GAME =====")
        print("1. Play Quiz")
        print("2. View Leaderboard")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            play_quiz()
        elif choice == "2":
            show_leaderboard()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
