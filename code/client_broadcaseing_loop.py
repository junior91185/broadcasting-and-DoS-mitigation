import socket
import time

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Allow broadcasting
#client_socket.settimeout(2)  # Set timeout for receiving response

message = b"Broadcasting message to server"  # Message to send

try:
    while True:  # Keep broadcasting indefinitely
        client_socket.sendto(message, ('<broadcast>', 5005))  # Send to broadcast address on port 5005
        print("Message sent to server.")

        try:
            # Receive response from server
            data, addr = client_socket.recvfrom(1024)  # Buffer size is 1024 bytes
            print(f"Received response: {data.decode()} from {addr}")
        except socket.timeout:
            print("No response received.")
        
        #time.sleep(2)  # Wait for 2 seconds before the next broadcast
except KeyboardInterrupt:
    print("Client stopped by user.")

# Optionally close the socket after communication
finally:
    client_socket.close()

