from task_executor import db_integration
from sqlalchemy.orm import  Mapped, mapped_column

class Task(db_integration.Model):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(db_integration.Integer, primary_key=True)
    command: Mapped[str] = mapped_column(db_integration.String, nullable=False)