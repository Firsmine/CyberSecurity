import socket                   # network library
import time

while True:
  print("\n" + "#="*3 + " Port Scanner " + "=#"*3)
  
  print("Choose Target IP Address")
  print("1. Localhost")
  print("2. Custom IP address")
  print("3. Exit")
  try:
    target = int(input("\nTarget IP (1-3): "))
    
    if target == 1:
      host = "127.0.0.1"              # scan target port (localhost)
    elif target == 2:
      host = input("IP Address: ")
    elif target == 3:
      print("\nExit the program.\n")
      break
    else:
      print(">>> Please choose the available menu.")
      continue
  except ValueError:
    print(">>> Please input a valid number of the menu")
    continue
    
  try:
    start = int(input("Start Port: "))
    end = int(input("End Port: "))
  except ValueError:
    print(">>> Please input a valid number of port")
  
  if input(f"Scan port {host} from port {start} until port {end}? (y/n): ").lower() != "y":
    print("\nScan Canceled.\n")
    break

  print(f"\nScanning {host}...\n")

  for port in range(start, end+1):
    sock = socket.socket(         # made a call to port
      socket.AF_INET,             # using IPv4
      socket.SOCK_STREAM          # using TCP 
    )
    sock.settimeout(0.1)
    
    result = sock.connect_ex(     # return number with connect_ex(), not connect()
      (host, port)                # if succeed, result 0, else result != 0
    )
    
    if result == 0:
      print(f"Port {port} : OPEN")
      
    sock.close()
  print("\nScan Finished.")
  
  if input("Scan Port Again? (y/n): ").lower() != "y":
    print("\nExit the program\n")
    break