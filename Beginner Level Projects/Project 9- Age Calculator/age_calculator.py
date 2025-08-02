# Ask for the user's name
name = input("What is your name? ")

# --- Input Validation for Age ---
# Use a loop to keep asking until a valid number is entered
while True:
    age_input = input("How old are you? ")
    try:
        # Try to convert the input to an integer
        age = int(age_input)
        # Check if the age is a positive number
        if age > 0:
            break  # Exit the loop if the age is valid
        else:
            print("Please enter a positive number for your age.")
    except ValueError:
        # This block runs if the input wasn't a valid number
        print("That doesn't look like a valid age. Please enter a number.")

# Calculate future age
future_age = age + 10

# Print the result
print("\nHello, " + name + "!")
print(f"In 10 years, you will be {future_age} years old.")
