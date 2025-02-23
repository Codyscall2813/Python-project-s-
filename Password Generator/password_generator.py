import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+=?><[]"

while True:
    try:
        length = int(input("Enter a length (must be between 8 and 32): "))
        if length < 8 or length > 32:
            raise ValueError("Password length must be between 8 and 32.")
        break
    except ValueError as e:
        print(e)

# Generate at least 2 of each type of character
password = (
    random.sample(lower, 2) +
    random.sample(upper, 2) +
    random.sample(numbers, 2) +
    random.sample(symbols, 2)
)

# If the length is greater than 8, add random characters to meet the desired length
if length > 8:
    remaining_length = length - 8
    password += random.choices(lower + upper +
                               numbers + symbols, k=remaining_length)

# Shuffle the list to ensure randomness and convert to a string
random.shuffle(password)
password = ''.join(password)

print(f"Generated Password: {password}")
