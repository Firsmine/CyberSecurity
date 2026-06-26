from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os, hashlib

def get_hash(message):
  return hashlib.sha256(
    message.encode()
  ).hexdigest()

while True:
  print("\n"+"#="*3 + " Digital Signature " + "+#"*3)
  print("1. Create Signed Message")
  print("2. Verify Message")
  print("3. Modify Message")
  print("4. View Message")
  print("5. View Hash")
  print("6. Exit")

  try:
    menu = int(input("Select Menu (1-5): "))
  except ValueError:
    print(">>> Please enter a valid number.")
    continue
  
  # create signed message
  if menu == 1:
    message = input("\nMessage: ")

    # generate private key
    private_key = rsa.generate_private_key(
      public_exponent=65537,
      key_size=2048
    )
    public_key = private_key.public_key()
    
    # save private key
    with open("private_key.pem", "wb") as file:
      file.write(
        private_key.private_bytes(
          encoding=serialization.Encoding.PEM,
          format=serialization.PrivateFormat.PKCS8,
          encryption_algorithm=serialization.NoEncryption()
        )
      )
    # save public key
    with open("public_key.pem", "wb") as file:
      file.write(
        public_key.public_bytes(
          encoding=serialization.Encoding.PEM,
          format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
      )
    # save message
    with open("message.txt", "w") as file:
      file.write(message)
    
    # create signature
    signature = private_key.sign(
      message.encode(),
      padding.PKCS1v15(),
      hashes.SHA256()
    )
    # save signature
    with open("signature.bin", "wb") as file:
      file.write(signature)
    
    print("\nMessage Signed Successfully!")
    
    if input("\nTry another menu? (y/n): ").lower() != "y":
      print(">>> Exit the program.\n")
      break
    
  # verify message
  elif menu == 2:
    required_files = [
      "message.txt",
      "signature.bin",
      "public_key.pem"
    ]
    missing = False
    
    for file in required_files:
      if not os.path.exists(file):
        print(f"{file} not found.")
        missing = True
    if missing:
      continue
    
    with open("message.txt", "r") as file:
      message = file.read()
    with open("signature.bin", "rb") as file:
      signature = file.read()
    with open("public_key.pem", "rb") as file:
      public_key = serialization.load_pem_public_key(
        file.read()
      )
      
    try:
      public_key.verify(
        signature,
        message.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
      )
      print("\nVALID")
      print("Message has not been modified.")
    except:
      print("\nINVALID")
      print("Message has been modified")
    
    if input("\nTry another menu? (y/n): ").lower() != "y":
      print(">>> Exit the program.\n")
      break

  # modify message
  elif menu == 3:
    if not os.path.exists("message.txt"):
      print("message.txt not found.")
      continue
    
    new_message = input("\nNew Message: ")
    
    with open("message.txt", "w") as file:
      file.write(new_message)

    print("\nMessage Modified.")
    
    if input("\nTry another menu? (y/n): ").lower() != "y":
      print(">>> Exit the program.\n")
      break
  
  # view message
  elif menu == 4:
    if not os.path.exists("message.txt"):
      print("No message found.")
      continue

    with open("message.txt", "r") as file:
      print("\nCurrent Message: ")
      print(file.read())
    if input("\nTry another menu? (y/n): ").lower() != "y":
      print(">>> Exit the program.\n")
      break

  # view hash
  elif menu == 5:
    if not os.path.exists("message.txt"):
      print("\nNo message found.")
      continue

    with open("message.txt", "r") as file:
      message = file.read()

    hash_value = get_hash(message)

    print("\nCurrent message: ")
    print(message)

    print("\nSHA256 Hash: ")
    print(hash_value)

    if input("\nTry another menu? (y/n): ").lower() != "y":
      print(">>> Exit the program.\n")
      break

  # exit
  elif menu == 6:
    print("\nExit the program\n")
    break
  else:
    print("Invalid menu.")
    
"""
Notes:
- hash        --> check the integrity
- signature   --> check the authenticity
- private key --> make signature
- public key  --> verify the signature
"""