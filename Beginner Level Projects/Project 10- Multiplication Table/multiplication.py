# Ask the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))

# Print the multiplication table from 1 to 10
print(f"\nMultiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
