UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"

while True:
    print()
    print("#="*5 + " Secure Your Data " + "=#"*5)
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    menu = int(input("Select Menu: "))
        
    if menu == 1:
        print("\nEncrypt Your Text")
        text = input("text\t\t: ")
        shift = int(input("Shift\t\t: "))

        encrypted = ""

        for char in text:
            if char in UPPERCASE:
                position = UPPERCASE.index(char)
                new_position = (position+shift)%26
                encrypted += UPPERCASE[new_position]
            elif char in LOWERCASE:
                position = LOWERCASE.index(char)
                new_position = (position+shift)%26
                encrypted += LOWERCASE[new_position]
            else:
                encrypted += char
        print("Encrypted\t:", encrypted)
        
        if input("Save to history.txt? (y/n)").lower() == "y":
            print("Saved into history.txt file")
            with open("history.txt", "a") as file:
                file.write(
                    f"{record_no} | {text} | {encrypted} | Encrypt\n"
                )
            record_no = 1
        else:
            continue
        
        if input("Try another menu? (y/n): ").lower() != "y": 
            print("\nExit the program")
            break
    elif menu == 2:
        print("\nDecrypt Your Encrypted Text")
        text = input("Encrypted text\t: ").upper()
        shift = int(input("Shift\t\t: "))
        
        decrypt = ""
        for char in text:
            if char in UPPERCASE:
                position = UPPERCASE.index(char)
                new_position = (position-shift)%26
                decrypt += UPPERCASE[new_position]
            elif char in LOWERCASE:
                position = LOWERCASE.index(char)
                new_position = (position-shift)%26
                decrypt += LOWERCASE[new_position]
            else:
                decrypt += char
        print("Decrypted\t:", decrypt)
        
        if input("Try another menu? (y/n): ").lower() != "y": 
            print("\nExit the program")
            break
    else:
        print("\nExit the program")
        break