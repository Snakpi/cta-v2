from pydantic import BaseModel


class Meta(BaseModel):
    code: int
    message: str


class Data(BaseModel):
    result: list
    count: int


class Response(BaseModel):
    meta: Meta
    data: Data
