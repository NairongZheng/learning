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
            received_data = self.receive_data(client_socket)
            if received_data:
                msg = Message()
                msg.ParseFromString(received_data)
                print("Received(len):", len(msg.content))
                response_msg = self.process_data(msg)
                self.send_data(client_socket, response_msg)
            client_socket.close()

    def receive_data(self, client_socket):
        received_data = b""
        while True:
            chunk = client_socket.recv(1024)
            if not chunk:
                break
            received_data += chunk
            if len(chunk) < 1024:
                break
        return received_data

    def send_data(self, client_socket, msg):
        client_socket.sendall(msg.SerializeToString())

    def process_data(self, msg):
        return Message(content=msg.content.upper())

if __name__ == "__main__":
    server = Server('127.0.0.1', 8888)
    server.run()