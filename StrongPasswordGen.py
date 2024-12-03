import random
import string
def generate_password():
    
    length = int(input("Enter The Password Length: "))
    include_digits = input("Include Digits? (yes or no): ").lower() in ['yes', 'y']
    include_special_chars = input("Include Special Characters? (yes or no): ").lower() in ['yes', 'y']

    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
password = generate_password()
print("Generated Password:", password)

# Code By MrNobody...