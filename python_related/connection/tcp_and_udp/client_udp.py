import socket


def send_message_to_server(server_addr, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        client_socket.sendto(message.encode(), server_addr)
        response, server_address = client_socket.recvfrom(1024)
        print("Received response from server", server_address, ":", response.decode())
    finally:
        client_socket.close()


if __name__ == "__main__":
    # server_addr = ("106.55.219.209", 12346) # dev01
    # server_addr = ("192.168.18.13", 12346) # dev01
    # server_addr = ("106.55.216.245", 12346) # street
    # server_addr = ("192.168.18.5", 12346) # street
    server_addr = ("127.0.0.1", 12345)
    message = "Hello, UDP server!"
    send_message_to_server(server_addr, message)
