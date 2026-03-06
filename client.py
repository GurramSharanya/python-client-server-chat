import socket

# create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
client_socket.connect(("localhost", 9999))

while True:
    # send message
    message = input("Client: ")
    client_socket.send(message.encode())

    # receive reply
    data = client_socket.recv(1024).decode()
    print("Server:", data)

client_socket.close()