from task_executor import db, base
from sqlalchemy.orm import  Mapped, mapped_column


class User(db.Model, base.JsonMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)