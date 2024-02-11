from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

class JsonMixin(object):
  def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}