import socket
host = "192.168.137.1"
# host = "socket.gethostbyname(socket.gethostname())"
port = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: # we don't have to bind here
    host = socket.gethostbyname(socket.gethostname())
    port = 8000
    client.connect((host, port))
    # settimeout(60)
    while True:
        response = client.recv(1024)
        print(response.decode())
        if response == "quit":
            break
        message = input("Chat (client): ")
        client.send(message.encode())
        



# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: # we don't have to bind here
#     # host = socket.gethostbyname(socket.gethostname())
#     # port = 8000
#     client.connect((host, port))
#     response = client.recv(1024)
#     print(response.decode())
#     while True:        
#         message = input("Chat (client): ")
#         client.send(message.encode())
#         response = client.recv(1024)
#         print(response.decode())