from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from task_executor import repository
from flask_login import UserMixin


class Base(DeclarativeBase):
    pass


class JsonMixin(object):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class User(repository.Model, JsonMixin, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(repository.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(repository.String, unique=True, nullable=False)


class Task(repository.Model):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(repository.Integer, primary_key=True)
    command: Mapped[str] = mapped_column(repository.String, nullable=False)
