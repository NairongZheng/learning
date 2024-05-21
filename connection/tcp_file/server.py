import socket
from message_pb2 import Message

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

    def run(self):
        print(f"Server listening on {self.host}:{self.port}")
        while True:
            client_socket, address = self.server_socket.accept()
            print(f"Connection from {address}")
            with client_socket.makefile('rb') as file:
                size_bytes = file.read(4)
                size = int.from_bytes(size_bytes, 'big')
                received_data = file.read(size)
                if received_data:
                    msg = Message()
                    msg.ParseFromString(received_data)
                    print("Received(len):", len(msg.content))
                    response_msg = self.process_data(msg)
                    response_data = response_msg.SerializeToString()
                    size_bytes = len(response_data).to_bytes(4, 'big')
                    client_socket.sendall(size_bytes + response_data)
            client_socket.close()

    def process_data(self, msg):
        return Message(content=msg.content.upper())

if __name__ == "__main__":
    server = Server('127.0.0.1', 8888)
    server.run()