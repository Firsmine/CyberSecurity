breach_database = {
    "LinkedIn": [
        "123456",
        "password",
        "linkedin123"
    ],
    "Google": [
        "qwerty",
        "welcome123"
        '12345678',
        'pass1234',
        'qwerty',
        '654321',
        '87654321'
    ],
    "Instagram": [
        "letmein",
        "admin123"
    ]
}

while True:
  print("\n"+"#="*3 + " Password Leak Checker " + "=#"*3)
  print("1. Check Password")
  print("2. View Database")
  print("3. Exit")
  
  try:
    menu = int(input("Select menu (1-3): "))
  except ValueError:
    print(">>> Please select a valid number of the menu.")
    continue
  
  if menu == 1:
    print("\n"+"#="*3 + " Check Password " + "=#"*3)
    
    password = input("\nPassword: ").lower()
    
    found_in = []
    
    for company in breach_database:
      if password in breach_database[company]:
        found_in.append(company)

    if found_in:
        print("WARNING!\nPassword found in the leaked database.")
    for company in found_in:
      print(f"Found in {company}")
      
    else: print("\nSAFE\nPassword not found in the leaked database.")

    if input("\nTry another menu? (y/n): ").lower() != "y":
        print("\nExit the program\n")
        break
  elif menu == 2:
    print("\n"+"#="*3 + " Leaked Password Database " + "=#"*3)
    
    for company in breach_database:
      print(f"\n{company}")
      
      for password in breach_database[company]:
        print(f"  - {password}")
    
    if input("\nTry another menu? (y/n): ").lower() != "y":
      print("\nExit the program\n")
      break
  
  elif menu == 3:
    print("\nExit the program\n")
    break
  else:
    print("\n>>> Please select a valid number of menu.")