import random

characters = ["a wizard", "a dragon", "an alien", "a pirate", "a detective", "a robot"]
settings = ["in a haunted castle", "on Mars", "at the bottom of the ocean", "in a jungle", "inside a video game", "in the future"]
problems = [
    "lost their magical staff",
    "forgot how to fly",
    "was being chased by chickens",
    "needed to solve a mysterious puzzle",
    "was stuck in a time loop",
    "had to win a dance battle"
]
solutions = [
    "asked a talking cat for advice",
    "found a hidden treasure map",
    "invented a silly gadget",
    "made a new friend",
    "learned a powerful spell",
    "realized the answer was inside them all along"
]

def generate_story():
    char = random.choice(characters)
    set_ = random.choice(settings)
    prob = random.choice(problems)
    sol = random.choice(solutions)

    story = f"Once upon a time, {char} was {set_}. They {prob}, but luckily they {sol}. The end!"
    return story

def main():
    print("📖 Welcome to the Random Story Generator!")
    while True:
        input("\nPress Enter to generate a story (or type 'exit' to quit): ")
        if 'exit' in input().lower():
            print("👋 Goodbye!")
            break
        print("\n" + generate_story())

if __name__ == "__main__":
    main()
