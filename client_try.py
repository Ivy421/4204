import socket
import time

# Client configuration
server_host = '127.0.0.1'
server_port = 12345
server_address = (server_host, server_port)
message_file = 'large_message.txt'
packet_size = 1024

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        
def client():
    start_time = time.time()
    total_data_sent = 0
    with open(message_file, 'r') as file:
        while True:
            data = file.read(packet_size)
            if not data:
                break
            client_socket.sendto(data.encode(), server_address)
            print(f"Sent: {data}")
            total_data_sent += len(data)
            #time.sleep(0.1)
    
    client_socket.sendto("END".encode(), server_address)
    client_socket.close()

    end_time = time.time()
    transfer_time = end_time - start_time
    throughput = total_data_sent / transfer_time
    print(f"Transfer Time: {transfer_time} seconds")
    print(f"Throughput: {throughput} bytes/second")

if __name__ == '__main__':
    client()


