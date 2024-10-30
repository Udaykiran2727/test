import socket

def udp_chat_server():
    server_ip = "127.0.0.1"
    server_port = 12345
    buffer_size = 1024

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))
    print(f"Server started at {server_ip}:{server_port}")

    while True:
        message, client_address = server_socket.recvfrom(buffer_size)
        print(f"Client: {message.decode()} from {client_address}")
        
        response = input("Server: ")
        server_socket.sendto(response.encode(), client_address)
udp_chat_server()
