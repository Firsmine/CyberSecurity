users = {
  "User":"User1234"
}
failed_attempt = 0

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

  if failed_attempt >= 3:
    print("\nWARNING!")
    print("Too many failed login attempts.")
  
  if input("\nTry Again? (y/n): ").lower() != "y":
    break