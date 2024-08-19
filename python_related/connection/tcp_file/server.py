import socket
from message_pb2 import Message

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
    
    def send_data(self, client_socket, send_msg: Message):
        serialized_data = send_msg.SerializeToString()
        size_bytes = len(serialized_data).to_bytes(4, 'big')
        with client_socket.makefile('wb') as file:
            file.write(size_bytes)
            file.write(serialized_data)
            file.flush()

    def receive_data(self, client_socket):
        with client_socket.makefile('rb') as file:
            size_bytes = file.read(4)
            size = int.from_bytes(size_bytes, 'big')
            recv_data = file.read(size)
            recv_msg = Message()
            recv_msg.ParseFromString(recv_data)
        return recv_msg
    
    def process_data(self, msg: Message):
        content = msg.content               # 收到的请求数据的实际内容
        send_content = content.upper()      # 处理
        send_msg = Message()
        send_msg.content = send_content
        return send_msg

    def run(self):
        print(f"server listening on {self.host}:{self.port}")
        while True:
            client_socket, address = self.server_socket.accept()
            print(f"connection from {address}")
            recv_msg = self.receive_data(client_socket)
            # print("recv_data:", recv_msg.content)
            print("received(len):", len(recv_msg.content))
            send_msg = self.process_data(recv_msg)
            # print("send_data:", send_msg.content)
            print("send(len):", len(send_msg.content))
            self.send_data(client_socket, send_msg)
            client_socket.close()
    

if __name__ == "__main__":
    server = Server('127.0.0.1', 8888)
    server.run()