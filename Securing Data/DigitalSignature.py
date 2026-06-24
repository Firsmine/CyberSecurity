import hashlib

while True:
  print("\n" + "#="*3 + " Digital Signature " + "=#"*3)
  print("1. Create Signature")
  print("2. Verify Signature")
  print("3. Exit")
  
  try:
    menu = int(input("Select Menu (1-3): "))
  except ValueError:
    print(">>> Please choose a valid number of menu!")
    continue
  
  if menu == 1:
    print("\n\n" + "#="*3 + " Create Signature " + "=#"*3)
    message = input("\nYour secret message: ")

    signature = hashlib.sha256(
      message.encode()  # encode the text so it becomes unreadable
    ).hexdigest()       # hash made a binary data, to make it readable with hexdigest()

    with open("signature.txt", "w") as file:
      file.write(signature)

    print("\nSignature created")
    print(signature)
    
    if input("\nTry another program? (y/n): ").lower() != "y":
      print(">>> Exit the program")
      break
    
  elif menu == 2:
    print("\n\n" + "#="*3 + " Verify Signature " + "=#"*3)
    message = input("\nMessage to verify: ")
    
    current_hash = hashlib.sha256(
      message.encode()
    ).hexdigest()
    
    with open("signature.txt", "r") as file:
      saved_hash = file.read()
      
    if current_hash == saved_hash:
      print("\nVALID")
    else:
      print("\nMODIFIED")
    
  elif menu == 3:
    print(">>> Exit the program\n")
    break
  
  else:
    print(">>> Please choose the available menu\n")
    continue