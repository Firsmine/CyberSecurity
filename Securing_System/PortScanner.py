import socket                   # network library
import time, ipaddress

while True:
  print("\n" + "#="*8 + " Port Scanner " + "=#"*8)
  
  # menu
  print("Choose Target IP Address")
  print("1. Localhost")
  print("2. Custom IP Address")
  print("3. Exit")
  
  # target
  try:
    target = int(input("\nTarget IP (1-3): "))
    
    if target == 1:
      host = "127.0.0.1"              # scan target port (localhost)
    elif target == 2:
      try:
        host = input("IP Address: ")
        ipaddress.ip_address(host)
      except ValueError:
        print(">>> Input a valid IP address. Example: 192.168.1.1")
        continue
    elif target == 3:
      print("\nExit the program.\n")
      break
    else:
      print(">>> Please choose the available menu.")
      continue
  except ValueError:
    print(">>> Please input a valid number of the menu")
    continue
    
  # range port
  try:
    start = int(input("Start Port: "))
    end = int(input("End Port: "))
  except ValueError:
    print(">>> Please input a valid number of port")
    continue
  
  # confirm action
  if input(f"Scan port {host} from port {start} until port {end}? (y/n): ").lower() != "y":
    print("\nScan Canceled.\n")
    break

  
  # start scanning
  print(f"\nScanning {host}...\n")

  # logic scan port
  start_time = time.time()
  for port in range(start, end+1):
    sock = socket.socket(         # made a call to port
      socket.AF_INET,             # using IPv4
      socket.SOCK_STREAM          # using TCP 
    )
    sock.settimeout(0.01)
    
    result = sock.connect_ex(     # return number with connect_ex(), not connect()
      (host, port)                # if succeed, result 0, else result != 0
    )
    
    if result == 0:
      try:
        service = socket.getservbyport(port)
      except OSError:
        service = "Unknown"
      print(f"Port {port:<5} : OPEN ({service})")
      
    sock.close()
  # timer
  end_time = time.time()
  duration = end_time - start_time
  print(f"\nScan Finished in {duration:.2f} seconds.")
  
  # end program
  if input("Scan Port Again? (y/n): ").lower() != "y":
    print("\nExit the program\n")
    break