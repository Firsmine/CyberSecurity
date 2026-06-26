import socket                   # network library

host = "127.0.0.1"              # scan target port (localhost)

print(f"\nScanning {host}...\n")

for port in range(1, 101):
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