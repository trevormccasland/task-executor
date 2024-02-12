from task_executor import db_integration, base
from sqlalchemy.orm import  Mapped, mapped_column


class User(db_integration.Model, base.JsonMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(db_integration.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db_integration.String, unique=True, nullable=False)