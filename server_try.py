import socket
import random

# Server configuration
server_host = '127.0.0.1'
server_port = 12345
server_address = (server_host, server_port)
buffer_size = 1024

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_address)

def server():
    while True:
        data, client_address = server_socket.recvfrom(buffer_size)
        if random.random() < error_probability:
            print(f"Packet loss from {client_address}")
        else:
            print(f"Received: {data.decode()} from {client_address}")
            # You can save the received data to a file or process it as needed.

if __name__ == '__main__':
    error_probability = 0.1  # Set the probability of data loss
    server()

