import os
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"

FILE_NAME = "history.txt"

def save_history(text, cipher, method):
    # if there's no file named history.txt yet, then make it
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            file.write(
                f"{"no":^3} | {"text":^20} | {"cipher":^20} | {"method":^10}\n"
            )
            file.write("-" * 65 + "\n")
        
    # number
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
        record_no = len(lines)-1
    
    # save data
    with open(FILE_NAME, "a") as file:
        file.write(
            f"{record_no:^3} | "
            f"{text:^20} | "
            f"{cipher:^20} | "
            f"{method:^10}\n"
        )

while True:
    print()
    print("#="*5 + " Secure Your Data " + "=#"*5)
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. View History")
    print("4. Exit")
    
    try: 
        menu = int(input("Select Menu: "))
    except ValueError:
        print(">>> Please enter a valid number of menu")
        continue
        
    if menu == 1:
        print("\nEncrypt Your Text")
        text = input("text\t\t: ")
        try:
            shift = int(input("Shift\t\t: "))
        except ValueError:
            print(">>> Shift must be a number.")
            continue

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
        
        if input("Save to history.txt? (y/n): ").lower() == "y":
            save_history(
                text=text,
                cipher=encrypted,
                method="Encrypt"
            )
            print("Saved into history.txt")
        else:
            continue
        
        if input("Try another menu? (y/n): ").lower() != "y": 
            print("\nExit the program")
            break
    elif menu == 2:
        print("\nDecrypt Your Encrypted Text")
        text = input("Encrypted text\t: ")
        try:
            shift = int(input("Shift\t\t: "))
        except ValueError:
            print(">>> Shift must be a number.")
            continue
        
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
        
        if input("Save to history.txt? (y/n): ").lower() == "y":
            save_history(
                text=text,
                cipher=decrypt,
                method="Decrypt"
            )
            print("Saved into history.txt")
        else:
            continue
        
        if input("Try another menu? (y/n): ").lower() != "y": 
            print("\nExit the program")
            break
    elif menu == 3:
        if not os.path.exists(FILE_NAME):
            print("\nNo history found.")
        else:
            print()
            with open(FILE_NAME, "r") as file:
                print(file.read())
    else:
        print("\nExit the program")
        break