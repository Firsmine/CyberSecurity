import time, os
from datetime import datetime

users = {
  "User":"User1234",
  "ADMIN":"Admin123",
  "Guest":"Guest123",
}
failed_attempt = 0
is_locked = False

now = datetime.now()
timer = now.strftime("%Y-%m-%d %H:%M:%S")

LOG = "login_log.txt"
def save_log(time, username, status):
  if not os.path.exists(LOG):
      with open(LOG, "w") as file:
        file.write(
          f"{"TIME":^20} | {"USERNAME":^10} | {"STATUS":<8}"
        )
        file.write("\n" + "-"*50 + "\n")
        
  with open(LOG, "a") as file:
    file.write(
      f"{time!s:<20} | {username:<10} | {status:<8}\n"
    )

while True:
  print("\n" + "#="*5 + " LOGIN MONITORING SYSTEM " + "=#"*5 + "\n")
  print("1. Login")
  print("2. View Login Logs")
  print("3. Clear Logs")
  print("4. Exit")
  
  try:
    menu = int(input("Select Menu: "))
  except ValueError:
    print("Please input a number of the available menu.")
    continue
    
  if menu == 1:
    print("\n" + "#="*5 + " LOGIN " + "=#"*5 + "\n")
    
    username = input("Username: ")
    password = input("Password: ")
    
    if username in users:
      if users[username] == password:
        print("\nLogin Succeed!")
        print(timer)
        failed_attempt = 0
        
        save_log(time=timer, username=username, status="SUCCEED")
      else:
        failed_attempt += 1
        print("\nWrong Password.")
        print(timer)
        
        save_log(time=timer, username=username, status="FAILED")
    else:
      failed_attempt += 1
      print("\nUsername Not Found.")
      print(timer)
      save_log(time=timer, username=username, status="FAILED")
    
    print(f"Failed attempts: {failed_attempt}")

    if failed_attempt >= 3:
      print("\nWARNING!")
      print("### Account Locked ###")
      print("Too many failed login attempts.")
      is_locked = True
    
    if input("\nTry Again? (y/n): ").lower() == "y":
      if is_locked == True:
        is_locked = False
        print("Wait...")
        for i in range(5, 0, -1):
          print(i)
          time.sleep(1)
          continue
      else:
        continue
    else:
      if input(f"Try Another Menu? (y/n): ").lower() != "y":
        print("\nProgram Ended.\n")
        break
      
  elif menu == 2:
    print("#="*5 + " LOGIN LOG " + "=#"*5)
    if os.path.exists(LOG):
      with open(LOG, "r") as file:
        content = file.read()
        print(content)
    else:
      print("Login Log Not Found.")
      continue
    
    if input(f"Try Another Menu? (y/n): ").lower() != "y":
      print("\nProgram Ended.\n")
      break
  
  elif menu == 3:
    if input("\nClear all the login log? (y/n): ").lower() != "y":
      continue
    else:
      if os.path.exists(LOG):
        with open(LOG, "w"):
          pass
        print("Login log cleared")
      else:
        print("Login Log Not Found.")
        continue
    
    if input(f"Try Another Menu? (y/n): ").lower() != "y":
      print("\nProgram Ended.\n")
      break
    
  elif menu == 4:
    if input("\nExit the program? (y/n): ").lower() == "y":
      print("\nProgram Ended.\n")
      break
  
  else:
    print("Please select the available menu.")
    continue