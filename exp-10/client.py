import socket

def udp_chat_client():
    server_ip = "127.0.0.1"
    server_port = 12345
    buffer_size = 1024

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("Client: ")
        client_socket.sendto(message.encode(), (server_ip, server_port))

        response, _ = client_socket.recvfrom(buffer_size)
        print(f"Server: {response.decode()}")

udp_chat_client()
