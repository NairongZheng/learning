import socket


def start_server(server_addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(server_addr)
        s.listen(1)
        print("Server listening on ", server_addr)

        while True:
            conn, client_addr = s.accept()
            try:
                print("Connected by ", client_addr)
                data = conn.recv(1024)
                if data:
                    print("Received from client: ", data.decode())
                    conn.sendall(b"Successful connection")
            finally:
                conn.close()
    finally:
        s.close()


if __name__ == "__main__":
    # server_addr = ("0.0.0.0", 60009)
    # server_addr = ("0.0.0.0", 12346)
    server_addr = ("127.0.0.1", 12345)
    start_server(server_addr)
