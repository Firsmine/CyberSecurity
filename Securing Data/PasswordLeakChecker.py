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
  password = input("\nCheck Password: ").lower
  
  if password in leaked_pass:
    print("WARNING!\nPassword found in the leaked database.")
  else:
    print("Password not found in the leaked database.")
  
  if input("\nCheck another password? (y/n: )").lower() != "y":
    print("\nExit the program\n")
    break