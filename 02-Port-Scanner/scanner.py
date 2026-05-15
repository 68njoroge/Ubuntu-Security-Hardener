#Simple TCP Port Scanner
import socket
#set the target IP address
target = input("Enter the target IP address: ")
#set the range of ports to scan
port_range = [22,80,443,3306]
print(f"\nscanning{target}....")
#loop through the specified ports and check if they are open
for port in port_range:
    #create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #set a timeout for the connection attempt
    s.settimeout(1)
    #Try connecting to the port
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"port {port} is open")
    else:
        print(f"port {port} is closed")
    #close the socket
    s.close()
    print("\nscan complete")

