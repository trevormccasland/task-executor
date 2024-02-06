from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://task_executor:secret@localhost:5432/task-executor"
class Base(DeclarativeBase):
  pass
db = SQLAlchemy(app, model_class=Base)

class User(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)

with app.app_context():
    db.create_all()

    db.session.add(User(name="example"))
    db.session.commit()

    users = db.session.execute(db.select(User)).scalars()

@app.route("/")
def hello_world():
    return db.one_or_404(db.select(User).filter_by(username="example"))

def main():
    app.run(debug=True, host='127.0.0.1', port=5000)


if __name__ == '__main__':
   main()
