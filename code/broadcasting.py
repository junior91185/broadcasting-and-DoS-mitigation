import socket

# Client setup for router broadcast
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)      #UDP 
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # client setup socket socket.SO_BROADCAST
client_socket.settimeout(5)

message = b"Broadcasting message to the network"
client_socket.sendto(message, ('<broadcast>', 5007))  # Assume router is on port 5007

try:
    # Receive response from any network device
    data, addr = client_socket.recvfrom(1024)       #client receive on port 1024
    print(f"Received response from {addr}: {data.decode()}")
except socket.timeout:
    print("No response received from the router.")
