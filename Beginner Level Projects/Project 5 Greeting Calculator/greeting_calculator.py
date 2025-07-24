# greeting_calculator.py

# Greet the user
print("Hello! Welcome to the Greeting Calculator 😊")

# Ask for user's name
name = input("What is your name? ")

# Respond to the user
print(f"Nice to meet you, {name}!")

# Ask for two numbers and add them
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

# Convert input strings to integers
num1 = int(num1)
num2 = int(num2)

# Perform addition
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}.")

# Optional: Use a loop to count down from 5
print("\nLet's do a countdown!")
for i in range(5, 0, -1):
    print(i)

print("🎉 Done! Have a great day!")
