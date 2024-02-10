from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from task_executor.db.models import base

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://task_executor:secret@localhost:5432/task-executor"


db = SQLAlchemy(app, model_class=base.Base)