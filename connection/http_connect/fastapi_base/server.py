from fastapi import FastAPI, HTTPException, Request
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

@app.post("/sumHandler", response_model=SumResponse)
async def sum_handler(request: SumRequest):
    print(f"debug damonzheng, SumHandler_request:{request}")
    try:
        res = request.para_a + request.para_b
        return SumResponse(errcode=200, data=res, msg="")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/upperHandler", response_model=UpperResponse)
async def upper_handler(request: UpperRequest):
    print(f"debug damonzheng, UpperHandler_request:{request}")
    try:
        upper_case_data = request.para_str.upper()
        return UpperResponse(errcode=200, data=upper_case_data, msg="Successful parameter passing")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=12300)
