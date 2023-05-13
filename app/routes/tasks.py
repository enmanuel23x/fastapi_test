from fastapi import APIRouter, Depends

from typing import List
from schemas.tasks import TaskBase, TaskModel

from sqlalchemy.orm import Session
from db.models.Tasks import Tasks
from db.session import get_db

router = APIRouter()

@router.post("/")
async def create_task(task: TaskModel, db: Session = Depends(get_db)):
    db_task = Tasks(
        title=task.title, 
        description=task.description,
        due_datetime=task.due_datetime
        )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    db.close()
    return {"message": "Task created successfully"}

@router.get("/{task_id}")
async def get_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Tasks).filter(Tasks.id == task_id).first()
    db.close()
    if db_task is None:
        return {"error": "Task not found"}
    return db_task

@router.get("/", response_model=List[TaskBase])
def get_tasks(db: Session = Depends(get_db)):
    """
    Get all tasks.

    Returns:
        List[Task]: List of tasks.
    """
    tasks = db.query(Tasks).all()
    db.close()
    return tasks

@router.put("/{task_id}")
async def update_task(task_id: int, task: TaskModel, db: Session = Depends(get_db)):
    db_task = db.query(Tasks).filter(Tasks.id == task_id).first()
    if db_task is None:
        return {"error": "Task not found"}
    db_task.title = task.title
    db_task.description = task.description
    db.commit()
    db.refresh(db_task)
    db.close()
    return {"message": "Task created successfully"}

@router.delete("/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Tasks).filter(Tasks.id == task_id).first()
    if db_task is None:
        return {"error": "Task not found"}
    db.delete(db_task)
    db.commit()
    db.close()
    return {"message": "Task deleted successfully"}