from pydantic import BaseModel


class OperateRequest(BaseModel):
    a: float
    b: float
