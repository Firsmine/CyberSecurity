"""
### password strength generator ###
check:
- password length (>=8)
- uppercase
- lowercase
- number
- symbol
"""

from string import ascii_lowercase, ascii_uppercase, digits, punctuation

print("\nREMINDER")
print("To make a strong password, please use the combination of lowercase, uppercase, digits of number, and symbols.")
print("Make sure the password is more than 8 letters.")

while True:
    password = input("\nCheck password: ").strip()

    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False

    for char in password:
        if char in ascii_lowercase:
            has_lower = True
        
        if char in ascii_uppercase:
            has_upper = True
        
        if char in digits:
            has_digit = True
            
        if char in punctuation:
            has_symbol = True

    score = 0
    if has_lower: score += 1
    if has_upper: score += 1
    if has_digit: score += 1
    if has_symbol: score += 1

    if len(password) < 8:
        print("Very Weak")
    elif score == 4:
        print("Very Strong")
    elif score == 3:
        print("Strong")
    else:
        print("Weak")
        
    check = input("\nCheck other password? (y/n): ").lower()
    if check == "y":
        continue
    else:
        break