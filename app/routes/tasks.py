from fastapi import APIRouter, Depends

from typing import List
from schemas.tasks import TaskBase

from sqlalchemy.orm import Session
from db.models.Tasks import Tasks
from db.session import get_db

router = APIRouter()


@router.get("/", response_model=List[TaskBase])
def get_tasks(db: Session = Depends(get_db)):
    """
    Get all tasks.

    Returns:
        List[Task]: List of tasks.
    """
    tasks = db.query(Tasks).all()
    return tasks
