import time
import socket
import random
import string
from message_pb2 import Message

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.host, self.port))

    def send_random_data(self, msg_len):
        random_data = ''.join(random.choices(string.ascii_lowercase, k=msg_len))
        msg = Message()
        msg.content = random_data
        self.send_data(msg)

    def send_data(self, msg):
        serialized_msg = msg.SerializeToString()
        total_sent = 0
        while total_sent < len(serialized_msg):
            sent = self.client_socket.send(serialized_msg[total_sent:])
            if sent == 0:
                raise RuntimeError("Socket connection broken")
            total_sent += sent

    def receive_data(self):
        received_data = b""
        while True:
            chunk = self.client_socket.recv(1024)
            if not chunk:
                break
            received_data += chunk
            if len(chunk) < 1024:
                break
        return received_data

    def close(self):
        self.client_socket.close()

if __name__ == "__main__":
    client = Client('127.0.0.1', 8888)
    client.connect()
    ttt1 = time.time()
    client.send_random_data(msg_len=10000000)
    ttt2 = time.time()
    print(f"debug damonzheng, send msg cost time:{(ttt2-ttt1)*1000}")
    received_data = client.receive_data()
    ttt3 = time.time()
    print(f"debug damonzheng, recv msg cost time:{(ttt3-ttt2)*1000}")
    response_msg = Message()
    response_msg.ParseFromString(received_data)
    print("Received from server (len):", len(response_msg.content))
    client.close()