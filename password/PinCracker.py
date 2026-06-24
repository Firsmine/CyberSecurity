import time, random
from string import digits

print("\nCan this program crack your pin?")
pin = input("\nPin: ")

print("\nTry to crack your pin...\n")

guess = ""
while guess != pin:
  guess = ""
  for i in range(len(pin)):
    guess += random.choice(digits)
    
  print("Trying...", guess)
  time.sleep(0.0001)
print("\npin CRACKED: ", pin)