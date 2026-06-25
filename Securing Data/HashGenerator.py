import hashlib
from cryptography.hazmat.primitives import hashes

while True:
  print("\n" + "#="*3 + " Hash Simulation " + "+#"*3)
  print("1. Hash Message")
  print("2. Hash Password")
  print("3. Register & Login")
  print("4. Exit")
  
  try:
    menu = int(input("Select Menu (1-4): "))
  except ValueError:
    print(">>> Please select a valid number of menu")
    continue
  
  if menu == 1:
    print("\n" + "#="*3 + " Hash Your Message " + "+#"*3)
    message = input("\nMessage: ")

    hash_message = hashlib.sha256(
      message.encode()
    ).hexdigest()
    print("Hashed Message:\n", hash_message)
    
    if input("\nSelect another menu? (y/n): ").lower() != "y":
      print("\nExit the program\n")
      break
    
  elif menu == 2:
    print("\n" + "#="*3 + " Password Checker " + "+#"*3)
    password = input("\nPassword\t\t: ")

    hash_password = hashlib.sha256(
      password.encode()
    ).hexdigest()
    
    while True:
      confirm_pass = input("Confirm password\t: ")
      
      confirmed = hashlib.sha256(
        confirm_pass.encode()
      ).hexdigest()
      
      if hash_password == confirmed:
        print(">>> Password Confirmed.\n")
        break
      else:
        print(">>> Wrong password!\n")
        continue
    
    if input("Select another menu? (y/n): ").lower() != "y":
      print("\nExit the program\n")
      break
    
  elif menu == 3:
    print("\n" + "#="*3 + " Register & Login " + "+#"*3)
    
    print("\n=== REGISTER ===")
    username = input("Username\t\t: ")
    password = input("Password\t\t: ")
    while True: 
      con_pass = input("Confirm Password\t: ")
      
      if password != con_pass:
        print(">>> The confirmed password must be same as the first password.")
        continue
      else:
        print("\n>>> Register Successful!")
        break
    
    def hashed(data):
      return hashlib.sha256(
        data.encode()
      ).hexdigest()
      
    reg_name = hashed(username)
    reg_pass = hashed(password)
    
    print("\n+++++ LOGIN +++++")
    while True:
      name = input("Username\t\t: ")
      log_name = hashed(name)
      
      if log_name != reg_name:
        print(">>> Username Invalid.")
        continue
      else:
        break
    
    while True:
      password = input("Password\t\t: ")
      log_pass = hashed(password)
      
      if log_pass != reg_pass:
        print(">>> Wrong Password.")
        continue
      else:
        break
    print("\n>>> Login Successful!")
    
    if input("Select another menu? (y/n): ").lower() != "y":
      print("\nExit the program\n")
      break
    
  elif menu == 4:
    if input("\nAre you sure wanna exit the program? (y/n): ").lower() == "y":
      print("\nExit the program\n")
      break
    else: continue
  else:
    print(">>> Please select a valid menu.")