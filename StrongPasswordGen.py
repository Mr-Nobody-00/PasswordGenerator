import random
import string

def generate_password():
    
    length = int(input("Enter the desired password length: "))
    include_digits = input("Include digits? (yes or no): ").lower() in ['yes', 'y']
    include_special_chars = input("Include special characters? (yes or no): ").lower() in ['yes', 'y']

    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
password = generate_password()
print("Generated Password:", password)