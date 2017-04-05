import time
from socket import *

# input IP address and message
ip = raw_input("Enter IP address or \'localhost\': ")
if ip == 'localhost':
    ip = '127.0.0.1'

serverAddr = (ip, 12000)
pings = 1

# Send ping 10 times
while pings <= 10:

    # Create a UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    # Set a timeout value of 1 second
    clientSocket.settimeout(1)

    # Send ping
    start = time.time()
    message = 'Ping '+ str(pings) + ' ' + str(start)
    clientSocket.sendto(message, serverAddr)

    #If data is received back from server, print
    try:
        message, address = clientSocket.recvfrom(1024)
        end = time.time()
        rtt = end - start
        print("Respond: " + message)
        print("RTT: " + str(rtt*1000) + "ms\n")

    #If data is not received back from server, print it has timed out
    except timeout:
        print("Requset timed out\n")

    pings += 1
