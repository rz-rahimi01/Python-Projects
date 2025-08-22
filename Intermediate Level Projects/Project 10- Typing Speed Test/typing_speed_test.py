import time
import random

sentences = [
    "Python is a powerful programming language.",
    "Typing fast is a useful skill to practice.",
    "Artificial intelligence is shaping the future.",
    "Always write clean and readable code.",
    "The quick brown fox jumps over the lazy dog."
]

def typing_test():
    sentence = random.choice(sentences)
    print("\n📝 Type the following sentence:\n")
    print(f"👉 {sentence}\n")

    input("Press Enter when you are ready to start...")
    start_time = time.time()
    typed = input("\nStart typing: ")
    end_time = time.time()

    elapsed = end_time - start_time
    words = len(sentence.split())
    wpm = round((words / elapsed) * 60)

    # Accuracy
    correct_chars = sum(1 for a, b in zip(sentence, typed) if a == b)
    accuracy = round((correct_chars / len(sentence)) * 100, 2)

    print("\n===== RESULTS =====")
    print(f"⏱ Time: {elapsed:.2f} seconds")
    print(f"⚡ Speed: {wpm} WPM")
    print(f"🎯 Accuracy: {accuracy}%")

def main():
    print("⌨️ Welcome to the Typing Speed Test!")
    while True:
        print("\n1. Start Test")
        print("2. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            typing_test()
        elif choice == "2":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
