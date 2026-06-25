"""
This program is used to make a strong password randomly.
Strong password must have at least 8 letters, a lowercase, an uppercase, digit, and symbol
"""

from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import secrets, random


while True: 
    while True:
        try:
            length = int(input("\nPassword length (>=8): "))
            
            if length < 8:
                print("A strong password must have at least 8 characters")
                continue
            break 
        except ValueError:
            print("Please enter a number")
    
    password = [
        secrets.choice(ascii_lowercase),
        secrets.choice(ascii_uppercase),
        secrets.choice(digits),
        secrets.choice(punctuation)
    ]
    characters = (ascii_lowercase+ascii_uppercase+digits+punctuation)
    
    for i in range(length -4):
        password.append(
            secrets.choice(characters)
        )
    random.shuffle(password)
    
    password = "".join(password)
    
    print(f"\nGenerated Password: {password}\n")
    
    make = input("Generate another password? (y/n): ").lower()
    if make != "y":
        print("Stay Secure!")
        break