import random

choices = ["rock", "paper", "scissors"]

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        return "player"
    else:
        return "computer"

def main():
    print("🎮 Welcome to Rock–Paper–Scissors!")
    player_score = 0
    computer_score = 0

    while True:
        print("\n===== MENU =====")
        print("1. Play")
        print("2. Show Score")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            player_move = input("Enter rock, paper, or scissors: ").strip().lower()
            if player_move not in choices:
                print("❌ Invalid choice!")
                continue

            computer_move = random.choice(choices)
            print(f"🤖 Computer chose: {computer_move}")

            winner = get_winner(player_move, computer_move)
            if winner == "draw":
                print("😐 It's a draw!")
            elif winner == "player":
                print("🎉 You win!")
                player_score += 1
            else:
                print("💀 Computer wins!")
                computer_score += 1

        elif choice == "2":
            print(f"\n📊 Score: You {player_score} - {computer_score} Computer")
        elif choice == "3":
            print("👋 Thanks for playing!")
            break
        else:
            print("❌ Invalid menu option.")

if __name__ == "__main__":
    main()
