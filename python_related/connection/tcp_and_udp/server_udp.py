import socket


def start_udp_server(server_addr):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(server_addr)

    print("UDP server listening on", server_addr)

    while True:
        message, client_address = server_socket.recvfrom(1024)
        print("Received message from,", client_address, ":", message.decode())
        # response_message = f"Echo: {message.decode()}"
        response_message = message.decode()
        server_socket.sendto(response_message.encode(), client_address)


if __name__ == "__main__":
    # server_addr = ("0.0.0.0", 40009)
    # server_addr = ("0.0.0.0", 12346)
    server_addr = ("127.0.0.1", 12345)
    start_udp_server(server_addr)
