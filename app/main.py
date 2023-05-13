from fastapi import FastAPI, Depends
import db.session as db
#from models.Tasks import Tasks
from routes import tasks


app = FastAPI()

@app.on_event("startup")
def startup():
    print("startup")
    db.Base.metadata.create_all(db.engine)

@app.on_event("shutdown")
def shutdown():
    print("shutdown")
    db.SessionLocal.close_all()

def get_db():
    # Lógica para obtener la base de datos
    db = ...
    return db

#@app.get("/tasks")
#def get_tasks():
#    print(db)
#    tasks = db.SessionLocal.query(Tasks).all()
#    return tasks

app.include_router(tasks.router, tags=["tasks"], prefix="/tasks")