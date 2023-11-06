import random
import string

def generate_password(length, include_digits=True, include_special_chars=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length and complexity
length = int(input("Enter the desired password length: "))
include_digits = input("Include digits (yes/no)? ").lower() == "yes"
include_special_chars = input("Include special characters (yes/no)? ").lower() == "yes"

password = generate_password(length, include_digits, include_special_chars)
print("Generated password:", password)