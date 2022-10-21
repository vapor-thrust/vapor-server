from pydantic import BaseModel


class OperateRequest(BaseModel):
    a: str
    b: str
