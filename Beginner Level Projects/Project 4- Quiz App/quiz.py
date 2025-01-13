# Dictionary of questions and answers
questions = {
    1: {"question": "What is the full form of CPU?", "answer": "central processing unit"},
    2: {"question": "What is the full form of RAM?", "answer": "random access memory"},
    3: {"question": "What is the full form of ROM?", "answer": "read-only memory"},
    4: {"question": "What is the full form of HTTP?", "answer": "hypertext transfer protocol"},
    5: {"question": "What is the full form of URL?", "answer": "uniform resource locator"}
}

# Initialize score and total number of questions
correct_answers = 0
total_questions = len(questions)

# Loop through the dictionary to ask questions
for key, value in questions.items():
    print(value["question"])
    user_answer = input("Your answer: ").strip().lower()
    
    # Check if the answer is correct
    if user_answer == value["answer"]:
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Wrong! The correct answer is: {value['answer']}")

# Display the results
print(f"\nYou answered {correct_answers} out of {total_questions} questions correctly.")
