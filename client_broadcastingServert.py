import socket

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) 
client_socket.settimeout(2)

message = b"Broadcasting message to server"
client_socket.sendto(message, ('<broadcast>', 5005))  # Send broadcast for all devices listening to port 5005

try:
    # Receive response from server
    data, addr = client_socket.recvfrom(1024)
    print(f"Received response: {data.decode()} from {addr}")
except socket.timeout:
    print("No response received.")


