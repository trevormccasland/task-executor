from task_executor import db
from sqlalchemy.orm import  Mapped, mapped_column

class Task(db.Model):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    command: Mapped[str] = mapped_column(db.String, nullable=False)