from pydantic import BaseModel
from datetime import date
from typing import Optional

class TaskBase(BaseModel):
    id: int
    title: str
    description: str
    due_datetime: date

    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    title: str
    description: str
    due_datetime: date

    class Config:
        orm_mode = True

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    due_datetime: Optional[date]
    class Config:
        orm_mode = True