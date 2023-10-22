import socket
import random

# Server configuration
server_host = '127.0.0.1'
server_port = 12345
server_address = (server_host, server_port)
buffer_size = 1024
received_file = 'received_file.txt'

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_address)

def server():
    with open(received_file, 'wb') as received_file_stream:
        while True:
            data, client_address = server_socket.recvfrom(buffer_size)

            if random.random() < error_probability:
                print(f"Packet loss from {client_address}")
            else:
                print(f"Received: {data.decode()} from {client_address}")
                received_file_stream.write(data)
            if data == b'END':
                break

        

    #received_file_stream.save()
    received_file_stream.close()

def compare_files(original_file, received_file):
    with open(original_file, 'r') as original, open(received_file, 'r') as received:
        original_data = original.read()
        received_data = received.read()
    
    print(received_data[-3:])
    if received_data.endswith('END'):
        received_data = received_data[:-3]

    if original_data == received_data:
        print("File received correctly.")
    else:
        print("File received with errors.")
        	
if __name__ == '__main__':
    error_probability = 0.2  # Set the probability of data loss
    server()
    original_file = 'large_message.txt'  # Replace with your original file name
    compare_files(original_file, received_file)
