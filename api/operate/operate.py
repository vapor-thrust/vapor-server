from fastapi import APIRouter
from api.operate.response.operate import OperateResponse
from api.operate.request.operate import OperateRequest
from app.operate.operation import Operation

oper_router = APIRouter()


@oper_router.post("/", response_model=OperateResponse)
def operation_plus(request: OperateRequest):
    oper = Operation(request.a, request.b)
    result = oper.plus()
    return {"res": result}
