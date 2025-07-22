import random
import string

def generate_password(length=12):
    if length < 6:
        return "Password too short! Use at least 6 characters."

    # All possible characters: letters + digits + punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Use random.choices for better randomness
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    print("🔐 Random Password Generator")
    try:
        length = int(input("Enter desired password length (min 6): "))
        pwd = generate_password(length)
        print("\nGenerated Password: ", pwd)
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()
