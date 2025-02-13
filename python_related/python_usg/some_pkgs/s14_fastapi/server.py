from typing import List
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
import uvicorn
import traceback


app = FastAPI()

# 用于存储 WebSocket 连接的客户端
clients: List[WebSocket] = []


# 定义 Pydantic 数据模型
class Item(BaseModel):
    name: str
    price: float


# GET 请求
@app.get("/")
async def read_root(request: Request):
    client_ip, client_port = request.client
    print(f"GET request from {client_ip}:{client_port}")
    return {"message": "Hello, FastAPI!"}


# POST 请求
@app.post("/items/")
async def create_item(request: Request, item: Item):
    client_ip, client_port = request.client
    print(f"POST request from {client_ip}:{client_port}")
    return {"message": f"Item {item.name} created with price {item.price}"}


# 定义处理不同输入的函数
def handle_input(data: str) -> str:
    if data == "hello":
        return "Hello, client!"
    elif data == "bye":
        return "Goodbye, client!"
    else:
        return f"You said: {data}"


# WebSocket 端点
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    # 打印客户端的 ip 和 port
    client_ip, client_port = websocket.client
    print(f"Client connected from {client_ip}:{client_port}")
    try:
        while True:
            data = await websocket.receive_text()  # 接收客户端发送的消息
            print(f"Received({websocket.client.host}:{websocket.client.port}): {data}")
            response = handle_input(data)  # 根据输入处理返回内容
            await websocket.send_text(response)  # 发送处理结果
    except WebSocketDisconnect:
        if websocket in clients:
            clients.remove(websocket)
            print(
                f"WebSocket disconnected. ({websocket.client.host}:{websocket.client.port})"
            )
    except Exception as e:
        traceback.print_exc()
        print(f"An error occurred: {e}")
        if websocket in clients:
            clients.remove(websocket)  # 发生异常时，也从集合中移除客户端


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=12345, log_level="error")
