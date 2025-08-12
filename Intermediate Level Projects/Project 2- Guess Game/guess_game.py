import random
import json
import os
from datetime import datetime

LEADERBOARD_FILE = "leaderboard.json"

# Load leaderboard
def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# Save leaderboard
def save_leaderboard(data):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add score to leaderboard
def add_score(player, attempts):
    leaderboard = load_leaderboard()
    leaderboard.append({
        "player": player,
        "attempts": attempts,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    leaderboard.sort(key=lambda x: x["attempts"])  # Sort by fewest attempts
    save_leaderboard(leaderboard)

# Show leaderboard
def show_leaderboard():
    leaderboard = load_leaderboard()
    if not leaderboard:
        print("\n🏆 No scores yet.")
        return
    print("\n===== LEADERBOARD =====")
    for i, entry in enumerate(leaderboard[:10], start=1):
        print(f"{i}. {entry['player']} - {entry['attempts']} attempts on {entry['date']}")

# Main game loop
def play_game():
    print("\n🎯 Welcome to the Number Guessing Game!")
    player = input("Enter your name: ").strip()
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            if guess < number:
                print("📉 Too low!")
            elif guess > number:
                print("📈 Too high!")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                add_score(player, attempts)
                break
        except ValueError:
            print("❌ Please enter a valid number.")

# Menu
def main():
    while True:
        print("\n===== NUMBER GUESSING GAME =====")
        print("1. Play Game")
        print("2. View Leaderboard")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            show_leaderboard()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
