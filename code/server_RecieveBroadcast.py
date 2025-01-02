import socket

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) #this socket designed to accept broadcasting
server_socket.bind(("", 5005))  # Bind to all interfaces on server port 5005 (hypothetical port)

print("Server is listening for broadcasts...")

while True:
    # Receive message from client
    data, addr = server_socket.recvfrom(1024)    ##buffer size 1024
    print(f"Received message: {data.decode()} from {addr}")

    # Respond to client
    server_socket.sendto(b"Hello from server!", addr)   # server will share her IP address with the client


