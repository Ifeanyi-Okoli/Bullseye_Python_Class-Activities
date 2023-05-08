from queue import Queue
import socket
import sys

host = socket.gethostbyname(socket.gethostname()) #we are using IPv4
print (host)
port = 8000

# Create a TCP/IP socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: #we are using SOCK_STREAM because we are using TCP
#when opening a socket without a context manager, we are required to manually close the socket
#we are using AF_INET because we are using IPv4
#we are using AF_INET6 because we are using IPv6
#we are using AF_UNIX because we are using Unix domain sockets
    server.bind((host, port)) #bind the socket to the port. We use tuple becuas the bind takes a single argument and
    server.listen()
    print("Listening for connections")
    while True:
        #2 things are returns:the client and a tuple containeing the ip address and port
        client, addr = server.accept() #accept the connection
        print(f"{addr[0]}:{addr[1]} has connected")
        message = "hi" 
        client.send(message.encode()) #send the message to the client
        while True:
            response = client.recv(1024) #receive the response from the client
            print(response.decode())
            if response == "quit":
                break
            message = input("Chat (server): ")

