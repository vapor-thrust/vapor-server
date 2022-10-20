from pydantic import BaseModel


class OperateResponse(BaseModel):
    res: float
