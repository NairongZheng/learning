"""
server
可以用不同的方式写
1. 自己定义请求跟返回的格式
2. 直接用简单的Request跟JSONResponse
第二种比较简单方便
具体说明查看README
"""
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class SumRequest(BaseModel):
    para_a: int
    para_b: int

class SumResponse(BaseModel):
    errcode: int
    data: int
    msg: str

class UpperRequest(BaseModel):
    para_str: str

class UpperResponse(BaseModel):
    errcode: int
    data: str
    msg: str

# 第一种写法
@app.post("/sumHandler", response_model=SumResponse)
async def sum_handler(request: SumRequest, http_request: Request):
    print(f"debug damonzheng, sumHandler接收来自{http_request.client.host}:{http_request.client.port}的请求")
    print(f"debug damonzheng, sumHandler接收的请求内容是:{request}")
    try:
        res = request.para_a + request.para_b
        return SumResponse(errcode=200, data=res, msg="")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# upperHandler第二种写法，注意async跟await
@app.post("/upperHandler")
async def upper_handler(request: Request):
    print(f"debug damonzheng, upperHandler接收来自{request.client.host}:{request.client.port}的请求")
    request = await request.json()
    print(f"debug damonzheng, upperHandler接收的请求内容是:{request}")
    result = request.get("para_str").upper()
    response = {"errcode": 200, "data": result, "msg": ""}
    return JSONResponse(content=response)

# upperHandler第一种写法
# @app.post("/upperHandler", response_model=UpperResponse)
# async def upper_handler(request: UpperRequest):
#     print(f"debug damonzheng, UpperHandler_request:{request}")
#     try:
#         upper_case_data = request.para_str.upper()
#         return UpperResponse(errcode=200, data=upper_case_data, msg="Successful parameter passing")
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app="server:app", host="0.0.0.0", port=12300)
