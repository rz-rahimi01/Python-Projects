# Welcome message
print("""
*************************************
*  Welcome to the Python Quiz Game! *
*  Test your knowledge of computer  *
*        acronyms and terms.        *
*************************************
""")

# Initialize score
score = 0
total_questions = len(questions)

# Main quiz loop
for q_num, q_data in questions.items():
    print(f"\nQuestion {q_num}/{total_questions}:")
    print(q_data["question"])
    user_answer = input("Your answer: ").strip().lower()
    
    # Check answer
    if user_answer == q_data["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is: {q_data['answer']}")

# Display final results
percentage = (score / total_questions) * 100
print("\n" + "="*40)
print(f"Quiz Complete!\nYour score: {score}/{total_questions} ({percentage:.1f}%)")

# Add some fun feedback based on score
if percentage == 100:
    print("🌟 Perfect! You're a computer whiz!")
elif percentage >= 75:
    print("👍 Great job! You know your tech!")
elif percentage >= 50:
    print("😊 Good effort! Keep learning!")
else:
    print("📚 Time to brush up on your computer terms!")
print("="*40 + "\n")

# Ask if user wants to play again
play_again = input("Would you like to play again? (yes/no): ").lower()
if play_again == "yes":
    run_quiz()
else:
    print("\nThanks for playing! Goodbye!")
