import socket
import time

# Client configuration
server_host = '127.0.0.1'
server_port = 12345
server_addr = (server_host, server_port)
message_file = 'large_message.txt'
packet_size = 128
buffer_size = 4096

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)




def client():

    with open(message_file, 'r') as file:
        start_time = time.time()
        total_data_sent = 0
        
        while True:
            data = file.read(packet_size)
            client_socket.settimeout(1)
            if not data:
                print('ENDING transmission')
                break
            client_socket.sendto(data.encode(), server_addr)

            total_data_sent += len(data)
            
            while True:

                try:

                    response,other = client_socket.recvfrom(buffer_size*3)

                    if b'good' in response:
                        print('correct transmission')
                        break

                    if  b'NACK' in response:

                        client_socket.sendto(data.encode(), server_addr)
                        print('retransmitting from client')
                except:
                    socket.timeout()
                    print('TIMEOUT')
                    client_socket.sendto(data.encode(), server_addr)

    client_socket.sendto("END".encode(), server_addr)
    client_socket.close()

    end_time = time.time()
    transfer_time = end_time - start_time
    throughput = total_data_sent / transfer_time
    print(f"Transfer Time: {transfer_time} seconds")
    print(f"Throughput: {throughput} bytes/second")

if __name__ == '__main__':
    client()


