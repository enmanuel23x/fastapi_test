from pydantic import BaseModel
from datetime import date

class TaskBase(BaseModel):
    id: int
    title: str
    description: str
    due_datetime: date

    class Config:
        orm_mode = True