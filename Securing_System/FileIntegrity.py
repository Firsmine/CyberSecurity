import hashlib, os
from datetime import datetime

HASH_FILE = "hash.txt"

def current_time():
  return datetime.now().strftime("%Y-%m-%d %H:%M")

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
  print("5. View Registered File")
  print("6. Delete File")
  print("7. Verify All Files")
  print("8. Exit")
  
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
    time = current_time()
    
    if not os.path.exists(HASH_FILE):    
      with open(HASH_FILE, "w") as file:
        file.write(f"{"TIME":^16} | {"FILE":^20} | {"HASH"}")
        file.write("\n" + "-"*100 + "\n")
    
    with open(HASH_FILE, "a") as file:
      file.write(f"{time!s:<16} | {filename:^20} | {file_hash}\n")
    
    print("\n>>> File Registered.")
    print("File\t: " + filename )
    print("Hash\t: " + file_hash)
    print("Time\t: " + time)
    
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
    saved_hash = None
    
    with open(HASH_FILE, "r") as file:
      lines = file.readlines()
      for line in lines[2:]:
        parts = line.strip().split("|")
        file_name = parts[1].strip()
        file_hash = parts[2].strip()
        if file_name == filename:
          saved_hash = file_hash
          break
        
    if saved_hash is None:
      print(">>> File has not been registered.")
    elif current_hash == saved_hash:
      print("\nVALID")
      print("File has not been modified.")
    else:
      print("\nWARNING")
      print("File has been modified.")
    
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
    print("\n" + "#="*5 + " View Registered File " + "=#"*5)
    
    # incoming
    
    if input(f"\nTry Another Menu? (y/n): ").lower() != "y":
      print("\nProgram Ended.\n")
      break
    
  elif menu == 6:
    print("\n" + "#="*5 + " Delete File " + "=#"*5)
    
    # incoming
    
    if input(f"\nTry Another Menu? (y/n): ").lower() != "y":
      print("\nProgram Ended.\n")
      break
  
  elif menu == 7:
    print("\n" + "#="*5 + " Verify All File " + "=#"*5)
    
    # incoming
    
    if input(f"\nTry Another Menu? (y/n): ").lower() != "y":
      print("\nProgram Ended.\n")
      break
    
  elif menu == 8:
    if input(f"Exit the program? (y/n): ").lower() == "y":
      print("\nProgram Ended.\n")
      break
    
  else:
    print(">>> Please select the available menu.")
    continue