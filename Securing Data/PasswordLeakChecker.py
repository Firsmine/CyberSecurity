leaked_pass = [
  '12345678',
  '123456',
  'admin123',
  'qwerty',
  'password'
  '654321',
  '87654321'
]

while True:
  print("\n"+"#="*3 + " Password Leak Checker " + "=#"*3)
  print("1. Check Password")
  print("2. View Database")
  print("3. Add Leaked Password")
  print("4. Exit")
  
  try:
    menu = int(input("Select menu (1-4): "))
  except ValueError:
    print(">>> Please select a valid number of the menu.")
    continue
  
  if menu == 1:
    print("\n"+"#="*3 + " Check Password " + "=#"*3)
    
    password = input("\nPassword: ").lower
    
    if password in leaked_pass:
      print("WARNING!\nPassword found in the leaked database.")
    else:
      print("SAFE.\nPassword not found in the leaked database.")
    
    if input("\nTry another menu? (y/n: )").lower() != "y":
      print("\nExit the program\n")
      break
    
  elif menu == 2:
    print("\n"+"#="*3 + " Leaked Password Database " + "=#"*3)
    
    for i, password in enumerate(
      leaked_pass,
      start=1
    ):
      print(f"{i}. {password}")
    
    if input("\nTry another menu? (y/n: )").lower() != "y":
      print("\nExit the program\n")
      break
    
  else:
    print("\n>>> Please select a valid number of menu.")