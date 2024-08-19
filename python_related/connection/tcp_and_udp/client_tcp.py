import socket


def start_client(server_addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(server_addr)
        s.sendall(b"Hello, server")
        data = s.recv(1024)
        print("Received from server: ", data.decode())
    finally:
        s.close()


if __name__ == "__main__":
    # server_addr = ("106.55.219.209", 12346) # dev01
    # server_addr = ("192.168.18.13", 12346) # dev01
    # server_addr = ("106.55.216.245", 12346) # street
    # server_addr = ("192.168.18.5", 12346) # street
    server_addr = ("127.0.0.1", 12345)
    start_client(server_addr)
