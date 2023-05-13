from pydantic import BaseModel

class ResponseBase(BaseModel):
    message: str

class ErrorBase(BaseModel):
    error: str