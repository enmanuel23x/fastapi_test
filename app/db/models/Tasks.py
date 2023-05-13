import db.session as db
from sqlalchemy import Column, Integer, String, Text, Date


class Tasks(db.Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    due_datetime = Column(Date)
