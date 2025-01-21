import random
import string

def password_generator():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of the password: "))
    include_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    include_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated Password: {password}")

password_generator()