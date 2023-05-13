from fastapi import APIRouter, Depends, status

from typing import List, Union
from schemas.tasks import TaskBase, TaskCreate, TaskUpdate
from schemas.response import ResponseBase, ErrorBase

from sqlalchemy.orm import Session
from db.models.Tasks import Tasks
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=ResponseBase)
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task.

    - **task**: Task object containing title, description and due_datetime.

    Returns:
    - **message**: Task created successfully.
    """
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

@router.get("/{task_id}", response_model=Union[TaskBase, ResponseBase])
async def get_task(task_id: int, db: Session = Depends(get_db)):
    """
    Get a task by task ID.

    - **task_id**: ID of the task.

    Returns:
    - **task**: Retrieved task object.
    """
    db_task = db.query(Tasks).filter(Tasks.id == task_id).first()
    db.close()
    if db_task is None:
        return {"error": "Task not found"}
    return db_task

@router.get("/", response_model=List[TaskBase])
def get_all_tasks(db: Session = Depends(get_db)):
    """
    Get all tasks.

    Returns:
        List[Task]: List of tasks object.
    """
    tasks = db.query(Tasks).all()
    db.close()
    return tasks

@router.put("/{task_id}", response_model=Union[ResponseBase, ErrorBase])
async def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    """
    Update a task by task ID.

    - **task_id**: ID of the task.
    - **task**: Task object containing updated fields.

    Returns:
    - **message**: Task updated successfully.
    - **error**: Task not found.
    """
    db_task = db.query(Tasks).filter(Tasks.id == task_id).first()
    if db_task is None:
        return {"error": "Task not found"}
    db_task.title = task.title
    db_task.description = task.description
    db.commit()
    db.refresh(db_task)
    db.close()
    return {"message": "Task updated successfully"}

@router.delete("/{task_id}", response_model=Union[ResponseBase, ErrorBase])
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Delete a task by task ID.

    - **task_id**: ID of the task.

    Returns:
    - **message**: Task deleted successfully.
    - **error**: Task not found.
    """
    db_task = db.query(Tasks).filter(Tasks.id == task_id).first()
    if db_task is None:
        return {"error": "Task not found"}
    db.delete(db_task)
    db.commit()
    db.close()
    return {"message": "Task deleted successfully"}