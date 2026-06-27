import time

users = {
  "User":"User1234"
}
failed_attempt = 0
is_locked = False

while True:
  print("\n" + "#="*5 + " LOGIN " + "=#"*5 + "\n")
  
  username = input("Username: ")
  password = input("Password: ")
  
  if username in users:
    if users[username] == password:
      print("\nLogin Succeed!")
      failed_attempt = 0
    else:
      failed_attempt += 1
      print("\nWrong Password.")
  else:
    failed_attempt += 1
    print("\nUsername Not Found.")
  
  print(f"Failed attempts: {failed_attempt}")

  if failed_attempt >= 1:
    print("\nWARNING!")
    print("### Account Locked ###")
    print("Too many failed login attempts.")
    is_locked = True
  
  if input("\nTry Again? (y/n): ").lower() != "y":
    break
  else:
    if is_locked == True:
      is_locked = False
      print("Wait...")
      for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
      continue
    else:
      continue