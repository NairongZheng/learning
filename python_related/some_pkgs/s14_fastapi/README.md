# FastAPI Web框架

FastAPI是一个现代、快速（高性能）的Web框架，用于构建API。基于Python 3.6+的类型提示。

## 特点

1. **快速**: 性能极高，可与NodeJS和Go媲美
2. **快速开发**: 开发速度提升约200%到300%
3. **更少的bug**: 减少约40%的人为错误
4. **直观**: 完美的编辑器支持，自动补全
5. **简洁**: 减少代码重复
6. **标准化**: 基于并完全兼容API的OpenAPI和JSON Schema

## 基本使用

### 1. 安装
```bash
pip install fastapi
pip install "uvicorn[standard]"  # ASGI服务器
```

### 2. 最小应用
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# 运行: uvicorn server:app --reload
```

### 3. 路径参数
```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

### 4. 查询参数
```python
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

### 5. 请求体
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return item
```

## 核心功能

### 1. 路径操作

```python
@app.get("/")      # GET请求
@app.post("/")     # POST请求
@app.put("/")      # PUT请求
@app.delete("/")   # DELETE请求
@app.options("/")  # OPTIONS请求
@app.head("/")     # HEAD请求
@app.patch("/")    # PATCH请求
```

### 2. 请求参数类型

#### 路径参数
```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

#### 查询参数
```python
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10, q: str = None):
    return {"skip": skip, "limit": limit, "q": q}
```

#### 请求体
```python
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    full_name: str = None

@app.post("/users/")
def create_user(user: User):
    return user
```

### 3. 响应模型

```python
class UserOut(BaseModel):
    username: str
    email: str

@app.post("/users/", response_model=UserOut)
def create_user(user: User):
    # 即使返回完整用户对象，也只返回UserOut定义的字段
    return user
```

### 4. 状态码

```python
from fastapi import status

@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    return item

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    return None
```

### 5. 表单数据

```python
from fastapi import Form

@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}
```

### 6. 文件上传

```python
from fastapi import File, UploadFile

@app.post("/files/")
def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
```

### 7. 依赖注入

```python
from fastapi import Depends

def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
def read_items(commons: dict = Depends(common_parameters)):
    return commons
```

### 8. 中间件

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 自定义中间件
@app.middleware("http")
async def add_process_time_header(request, call_next):
    import time
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

### 9. 异常处理

```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]
```

### 10. 后台任务

```python
from fastapi import BackgroundTasks

def write_notification(email: str, message: str):
    # 发送邮件等耗时操作
    pass

@app.post("/send-notification/{email}")
def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, "消息内容")
    return {"message": "通知已发送"}
```

## 数据验证

FastAPI使用Pydantic进行数据验证：

```python
from pydantic import BaseModel, Field, EmailStr, HttpUrl

class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    description: str = Field(None, max_length=300)
    price: float = Field(..., gt=0, description="价格必须大于0")
    tax: float = Field(None, ge=0, le=100)
    tags: list[str] = []

class User(BaseModel):
    username: str
    email: EmailStr  # 自动验证邮箱格式
    website: HttpUrl  # 自动验证URL格式
```

## 自动文档

FastAPI自动生成交互式API文档：

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

## 示例文件说明

- **server.py**: FastAPI服务器端示例
- **client.py**: 客户端请求示例

更多示例可见：[`python_related/connection/http_connect/fastapi_base/`](../../connection/http_connect/fastapi_base/)

## 运行方式

```bash
# 开发模式（热重载）
uvicorn server:app --reload

# 指定host和port
uvicorn server:app --host 0.0.0.0 --port 8000

# 多worker（生产环境）
uvicorn server:app --workers 4
```

## 最佳实践

1. **使用类型提示**: 充分利用Python类型提示
2. **使用Pydantic模型**: 进行数据验证
3. **使用依赖注入**: 代码复用和关注点分离
4. **使用路由器**: 组织大型应用
5. **添加文档字符串**: 改善自动文档
6. **异步操作**: 使用`async def`提高性能

## 项目结构示例

```
app/
├── __init__.py
├── main.py          # FastAPI应用入口
├── models.py        # Pydantic模型
├── database.py      # 数据库连接
├── routers/         # 路由模块
│   ├── __init__.py
│   ├── users.py
│   └── items.py
└── dependencies.py  # 依赖项
```

## 参考资源

- [FastAPI官方文档](https://fastapi.tiangolo.com/)
- [FastAPI中文文档](https://fastapi.tiangolo.com/zh/)
- [GitHub仓库](https://github.com/tiangolo/fastapi)
- [Pydantic文档](https://pydantic-docs.helpmanual.io/)
