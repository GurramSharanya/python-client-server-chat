import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("localhost", 9999))


server_socket.listen(1)

print("Server started... Waiting for connections")


conn, addr = server_socket.accept()
print("Connected with", addr)

while True:
    
    data = conn.recv(1024).decode()

    if not data:
        break

    print("Client:", data)

    # send reply
    message = input("Server: ")
    conn.send(message.encode())

conn.close()
