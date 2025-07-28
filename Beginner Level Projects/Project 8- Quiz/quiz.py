def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
            "answer": "B"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippo"],
            "answer": "B"
        }
    ]

    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong. The correct answer was {q['answer']}.")

    print(f"\n🎉 Quiz finished! You got {score} out of {len(questions)} correct.")

if __name__ == "__main__":
    run_quiz()
  
