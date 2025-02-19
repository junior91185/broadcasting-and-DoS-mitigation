import socket
import time
from collections import defaultdict
import threading

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server_socket.bind(("", 5005))  # Bind to all interfaces on port 5005

print("Server is listening for broadcasts...")

# Rate limiting parameters
MAX_REQUESTS_PER_SECOND = 5
BLOCK_TIME_SECONDS = 1 # Duration for which a client is blacklisted
client_requests = defaultdict(list)  # Track request timestamps for each client
blacklist = defaultdict(float)  # Track blacklisted clients and their unban time
client_lock = threading.Lock()  # Lock for thread-safe access to shared resources

def handle_request(data, addr):
    """Handle incoming requests from clients."""
    global client_requests, blacklist

    # Check if the client is blacklisted
    with client_lock:
        if addr in blacklist:
            if time.time() < blacklist[addr]:
                print(f"Request from {addr} is blocked (blacklisted).")
                return  # Ignore request as client is blacklisted
            else:
                del backlist[addr] #remove from backlist when time expires

    # Rate limiting: Check if the client is sending too many requests
    current_time = time.time()
    with client_lock:
        client_requests[addr].append(current_time)

        # Remove timestamps older than 1 second
        client_requests[addr] = [t for t in client_requests[addr] if current_time - t < 1]

        if len(client_requests[addr]) > MAX_REQUESTS_PER_SECOND:
            print(f"Rate limit exceeded for {addr}. Blacklisting for {BLOCK_TIME_SECONDS} seconds.")
            blacklist[addr] = current_time + BLOCK_TIME_SECONDS  # Blacklist the client
            return  # Ignore the request if rate limit exceeded

    # Respond to client
    server_socket.sendto(b"Hello from server!", addr)
    print(f"Responded to {addr}.")

while True:
    try:
        # Receive message from client
        data, addr = server_socket.recvfrom(1024)  # Buffer size is 1024 bytes
        print(f"Received message: {data.decode()} from {addr}")

        # Create a new thread to handle the request
        threading.Thread(target=handle_request, args=(data, addr)).start()

    except Exception as e:
        print(f"Error occurred: {e}")
