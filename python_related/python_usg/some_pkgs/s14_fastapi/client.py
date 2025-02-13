import asyncio
import websockets
import requests


HTTP_URL = "http://127.0.0.1:12345" # HTTP 客户端
WS_URL = "ws://127.0.0.1:12345" # websockets

def test_http():
    # GET 请求
    response = requests.get(f"{HTTP_URL}/")
    print(f"GET Response: {response.json()}")

    # POST 请求
    response = requests.post(
        f"{HTTP_URL}/items/", json={"name": "Laptop", "price": 999.99}
    )
    print(f"POST Response: {response.json()}")


# WebSocket 客户端
async def test_websocket():
    try:
        async with websockets.connect(f"{WS_URL}/ws") as websocket:
            while True:
                # 从用户输入接收字符
                message = input("Enter a message to send to the server (type 'exit' to quit): ")

                if message == "exit":
                    print("Closing connection...")
                    break

                await websocket.send(message)  # 发送用户输入的消息
                response = await websocket.recv()  # 接收服务器的响应
                print(f"Server response: {response}")
    # 长时间没有往server发消息就会断开连接，可以使用心跳消息来保持连接（是原来的连接）
    # 也可以在断开的时候重新连接（但是已经不是原来那个连接了），如下：
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed: {e}. Trying to reconnect...")
        # 尝试重新连接
        await test_websocket()


if __name__ == "__main__":
    test_http()
    asyncio.run(test_websocket())
