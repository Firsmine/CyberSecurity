UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"

def decrypt(text, shift):
    result = ""
    
    for char in text:
        if char in UPPERCASE:
            position = UPPERCASE.index(char)
            new_position = (position-shift)%26
            result += UPPERCASE[new_position]
        elif char in LOWERCASE:
            position = LOWERCASE.index(char)
            new_position = (position-shift)%26
            result += LOWERCASE[new_position]
        else:
            result += char
    return result

print("\n" + "#="*5 + " Caesar Cipher Cracker " + "=#"*5)
print("Try to crack a secret? \nMake sure you won't regret it.")

while True:
    ciphertext = input("\nCiphertext: ")
    print("\nPossible Plaintext: \n")

    for shift in range (1, 26):
        plaintext = decrypt(ciphertext, shift)
        print(f"Shift {shift:2}: {plaintext}")
    
    while True:
        try:
            correct = int(input("\nCorrect shift (1-25): "))
            if 1 <= correct <= 25:
                break
            print("Please enter a number between 1 and 25.")
        except ValueError:
            print("Please enter a valid number")
            
    final = decrypt(ciphertext, correct)
    print("\nCorrect plaintext: ")
    print(final)
    
    if input("\nDecrypt another encrypted text? (y/n): ").lower() != "y":
        print("Well, bye!")
        break
