import hashlib, os

HASH_FILE = "hash.txt"

def get_hash(filename):
  with open(filename, "rb") as file:
    data = file.read()
  return hashlib.sha256(data).hexdigest()

while True:
  print("\n" + "#="*5 + " FILE INTEGRITY " + "=#"*5)
  print("1. Register File")
  print("2. Verify File")
  print("3. Modify File")
  print("4. View Hash")
  print("5. Exit")
  
  try:
    menu = int(input("Select Menu (1-5): "))
  except ValueError:
    print(">>> Please enter a valid number of menu.")
    continue
  
  if menu == 1:
    print("\n" + "#="*5 + " Register File " + "=#"*5)
    
    filename = input("Filename: ")

    if not os.path.exists(filename):
      print(">>> File not found in your device.")
      continue

    file_hash = get_hash(filename)
    
    with open(HASH_FILE, "w") as file:
      file.write(file_hash)
    
    print("\n>>> File Registered.")
    print(file_hash)
    
    if input(f"\nTry Another Menu? (y/n): ").lower() != "y":
      print("\nProgram Ended.\n")
      break
  
  elif menu == 2:
    print("\n" + "#="*5 + " Verify File " + "=#"*5)
    
    filename = input("Filename: ")
    
    if not os.path.exists(filename):
      print(">>> File not found in your device.")
      continue
    
    if not os.path.exists(HASH_FILE):
      print(">>> No registered hash.\nPlease register the file first.")
      continue
    
    current_hash = get_hash(filename)
    
    with open(HASH_FILE) as file:
      saved_hash = file.read()
      
    if current_hash == saved_hash:
      print("\nVALID")
      print("File has not been modified.")
    else:
      print("\nWARNING")
      print("File modified!")
    
    if input(f"\nTry Another Menu? (y/n): ").lower() != "y":
      print("\nProgram Ended.\n")
      break
    
  elif menu == 3:
    print("\n" + "#="*5 + " Modify File " + "=#"*5)
    
    filename = input("Filename: ")
    
    if not os.path.exists(filename):
      print(">>> File not found in your device.")
      continue
    
    text = input("New content: ")

    with open(filename, "w") as file:
      file.write(text)
      
    print("File Modified.")
    
    if input(f"\nTry Another Menu? (y/n): ").lower() != "y":
      print("\nProgram Ended.\n")
      break
    
  elif menu == 4:
    print("\n" + "#="*5 + " View Hash " + "=#"*5)
    
    if os.path.exists(HASH_FILE):
      with open(HASH_FILE) as file:
        print(file.read())
    else:
      print(">>> No hash saved.")
    
    if input(f"\nTry Another Menu? (y/n): ").lower() != "y":
      print("\nProgram Ended.\n")
      break
    
  elif menu == 5:
    if input(f"Exit the program? (y/n): ").lower() == "y":
      print("\nProgram Ended.\n")
      break
    
  else:
    print(">>> Please select the available menu.")
    continue