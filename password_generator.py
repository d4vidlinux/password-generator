# Simple local password generator using Python standard library

import secrets

print("="*6," Password Generator ","="*6)

char1 = "abcdefghijklmnopqrstuvwxyz"
upper_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%*()"
numbers = "0123456789"

try:
    length = int(input("How much letters your password should be? "))
    if length <= 0:
        raise ValueError
except ValueError:
    print("Please enter a valid positive number!")

for i in range(length):
    letter_char1 = secrets.choice(char1)
    letter_upper = secrets.choice(upper_char)
    letter_symbols = secrets.choice(symbols)
    num_numbers = secrets.choice(numbers)

    final = [letter_char1,letter_symbols,letter_upper,num_numbers]
    result = secrets.choice(final)
    print(result,end="")